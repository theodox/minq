import itertools
import operator
import re
from collections import namedtuple, Iterable

import maya.cmds as cmds


class QueryError(ValueError):
    """
    Raised when a query is incorrectly assembled (NOT at execution time!)
    """
    pass


# these functions are used to avoid Maya's annoying habit of returning everything
# when you're trying to filter but the stream you wish to filter is already empty

def non_empty_stream(stream):
    """yields a single None if the previous stream is exhausted"""
    return itertools.chain(stream, (None,))


def ensure_iterable(value):
    """ensure that the results of a command are always iterable"""
    if isinstance(value, Iterable):
        return value
    return tuple((value,))


def command_stream(stream, cmd, **kwargs):
    """convenience wrapper for commands that need non_empty_streams"""
    safe = non_empty_stream(stream)
    return iter(ensure_iterable(cmd(*safe, **kwargs) or []))


def get_list(stream, **kwargs):
    """return ls() on <stream> without ever returning everything"""
    return command_stream(stream, cmds.ls, **kwargs)


def get_relatives(stream, **kwargs):
    """return listRelatives() on <stream> without ever returning everything"""
    return command_stream(stream, cmds.listRelatives, **kwargs)


def get_history(stream, **kwargs):
    """return listHistory() on <stream> without ever returning everything"""
    try:
        return command_stream(stream, cmds.listHistory, **kwargs)
    except RuntimeError as err:
        if err.args == (u'Found no items to list the history for.\n',):
            return iter(tuple())
        raise


def get_connections(stream, **kwargs):
    """return listConnections() on <stream> without ever returning everything"""
    return command_stream(stream, cmds.listConnections, **kwargs)


def get_values(stream, **kwargs):
    """return getAttr() on a stream of attributes, or empty iterator"""
    try:
        return command_stream(stream, cmds.getAttr, **kwargs)
    except TypeError:
        return iter(tuple())

class Stream(object):
    """
    Represents an arbitrary stream of values.  Usually -- but not always -- this is a stream of Maya node names.
    Usually -- but not always -- this stream is a 'stored query', like a SQL statment: it's not a list of saved
    values but rather a chain of operations.  This allows you to manipulate queries themselves, rather than their
    contents

    Streams can be combined using set-like operators:

        stream1 + stream2

    returns a new stream containing the combined contents of both streams (duplicate values are removed)

        stream1 - stream2

    returns items that are only present in stream1 and not stream2

        stream1 & stream2

    returns only items that are common to both streams.

    Most streams are created by a NodeType-derived class: for example,  Meshes()  will yield all
    of the poly meshes in the scene as a Stream, while Transforms() will yield all the transforms.
    However you can 'initialize' a stream with a list or tuple if you already know the names
    of nodes or objects you're looking for: for example,

       Cameras()

    and

       Stream(['topShape', 'frontShape', 'perspShape', 'sideShape])

    are functionally interchangeable in a typical maya scene.
    """

    def __init__(self, upstream=None):
        self.incoming = upstream or tuple()

    def __iter__(self):
        return (i for i in self.incoming)

    def execute(self):
        """
        evaluate all of the queries in this Stream and return the result as a list
        """
        return [i for i in self]

    def cache(self):
        """
        returns a Stream wrapped around a the cached result of this query.
        """
        return Stream(self.execute())

    def where(self, pred):
        """
        given a callable filter function, returns a new stream containing only  items  for which the filter function
        return a truth-tested value
        """
        if hasattr(pred, 'attribute'):
            return WhereMany(self, pred)
        return Where(self, pred)

    def where_not(self, pred):
        """
        a convenience wrapper for 'where' that inverts the result -- useful for not having to make a lambda
        just to invert a common function
        """
        if hasattr(pred, 'attribute'):
            return WhereMany(self, pred, invert=True)
        return Where(self, pred, invert=True)

    def like(self, regex, exact=False):
        """
        given a string regular expression, returns a new stream containing only items where the regex finds a match.
        By default this allows subset metches using re.search, but if the optional 'exact' flag is set to True,
        the matches must be complete using re.match

        If the incoming stream contains items that can't be converted to strings, will raise an exception
        """
        return Like(self, regex, exact)

    def distinct(self):
        """
        Returns a new stream which contains no duplicate elements.

        If the incoming stream contains items that can't be hashed, will raise an exception
        """
        return Distinct(self)

    def sort(self, key):
        """
        returns a Stream which sorts the incoming stream using the default Python sort. If the optional key function
        is provided, the result will be sorted with that key.

        This operation has to exhaust the incoming stream, so it is more memory and performance intensive than other
        minq operations.
        """
        return Sort(self, key=None)

    def only(self, *pred, **kwargs):
        """
        Returns a new stream containing only items of the supplied types.  The types can be string typenames (such as
        'transforms' or 'shapes') or they can be minq.core.NodeType classes.  So

            this_stream.only('transform')

        and

            this_stream.only(Transform)

        are equivalent.

        A handful of NodeTypes (such as ObjectsOnly or Assemblies) can't be combined with others in a single call:

        if the optional namespace keyword is passed, this limits the stream to a given namespace
        """
        return OfType(self, *pred, **kwargs)

    def get(self, *args, **kwargs):
        """
        Returns a new stream which applies a minq.core.Projection class to this stream.  Projections are operations
        which replace the incoming stream with a new stream (rather than subsetting the original stream). For example:

            transforms.get(Children)

        returns a streams containing the children of the stream <transforms>.
        """
        target_type, args = args[0], args[1:]
        if not issubclass(target_type, Projection):
            raise QueryError, "%s is not a subclass of minq.Projection"
        return target_type(self, *args, **kwargs)

    def foreach(self, func):
        """
        Returns a stream containing the results of <func> applied to everything in the stream
        """
        return ForEach(self, func)

    def having(self, attrib):
        """
        Returns a stream of objects with the supplied attribute
        """
        return Having(self, attrib)

    def split(self, number_of_streams):
        """
        Returns multiple 'copies' of this stream which can be iterated independently without re-calling the query.
        """
        return itertools.imap(Stream, itertools.tee(self, number_of_streams))

    def join(self, **streams):
        """
        given a collection of named streams, return a table-like stream in which each 'row' has named values
        corresponding to the original stream. This is used for coordinating multiple streams: for example:

             bones = Joints()
             bone_parents = bones.get(Parents)
             with_parents = bones.join(parent = bone_parents)

         will produce a list like

            # stream: [dataRow(object=u'joint3', parent=u'joint2'), dataRow(object=u'joint2', parent=u'joint1')....]

        the join process doesn't make any effort to match up the contents, however -- if the different streams have
        different lengths enmpy 'columns' in the row will be filled with None and if the streams don't match up
        the results are not predictable.

        The primary use for join() is for doing bulk queries using Attributes:

            bones = Joints().like('l_')
            tx = bones.get(Attribute, 'tx').get(Values)
            ty = bones.get(Attribute, 'ty').get(Values)
            bone_translations = bones.join(x = tx, y = ty)
            print bone_translations

           # stream: [dataRow(object=u'L_Ankle', x=-5.0, y=-1.39), dataRow(object=u'L_Heel', x=-0.028, y =6.18)....]

        Note in this specific case it would be faster to use `.get(Attribute, 't')` rather than querying .tx and .ty
        separately -- but this pattern works for any arbitrary combination of attributes as long as all the objects
        in the stream have the attribute.  In this form the query is issued to maya only once per stream, which is a big
        advantage over individually calling getAttr many times over.
        """
        return Join(self, **streams)

    def append(self, *args, **kwargs):

        return Append(self, *args, **kwargs)

    def long(self):
        """
        Returns a new stream containing the long names of items in this stream. Any items which are not maya nodes in
        the stream will be filtered out.
        """
        return Long(self)

    def short(self):
        """
        Returns a new stream containing the short names of items in this stream. Any items which are not maya nodes in
        the stream will be filtered out.
        """
        return Short(self)

    def uuid(self):
        """
        Returns a new stream containing the uuids of items in this stream. Any items which are not maya nodes in the
        steeam will be filtered out.
        """
        return UUID(self)

    # operator overloads to support set functionality

    def __add__(self, other):
        return Union(self, other)

    def __iadd__(self, other):
        return Union(self, other)

    def __isub__(self, other):
        return Difference(self, other)

    def __sub__(self, other):
        return Difference(self, other)

    def __and__(self, other):
        return Intersection(self, other)

    def __iand__(self, other):
        return Intersection(self, other)

    def __xor__(self, other):
        return XOr(self, other)

    def __ixor__(self, other):
        return XOr(self, other)

    def __repr__(self):
        return "Stream(%s)" % self.execute().__repr__()


class Append(Stream):
    """
    appends a get() on the current stream
    """

    def __init__(self, incoming, *args, **kwargs):
        super(Append, self).__init__(incoming)
        self.args = args
        self.kwargs = kwargs

    def __iter__(self):
        main_stream, extension = itertools.tee(self.incoming, 2)
        target_type = self.args[0]
        append = target_type(extension, *self.args[1:], **self.kwargs)
        return itertools.chain(main_stream, append)


class Having(Stream):
    """
    Returns a stream of objects with the supplied attribute; equivalent to 'ls -o'
    """

    def __init__(self, incoming, attribute):
        super(Having, self).__init__(incoming)
        self.attribute = "." + attribute

    def __iter__(self):
        _attr = self.attribute
        add_attrib = lambda p: p + _attr
        return get_list(itertools.imap(add_attrib, self.incoming), o=True, long=True)


class Where(Stream):
    """
    Applies the supplied predicate to everything in the stream filtering only items that pass the predicate function

    if the optional invert keyword is provided, returns only items where predicate returns a False-y value
    """

    def __init__(self, upstream=tuple(), predicate=lambda p: True, invert=False):
        super(Where, self).__init__(upstream=upstream)
        if not callable(predicate):
            raise QueryError, "%s must be a callable object" % predicate
        self.predicate = predicate
        self.invert = invert

    def __iter__(self):
        _stream = iter(self.incoming)
        if self.invert:
            return itertools.ifilterfalse(self.predicate, _stream)
        return itertools.ifilter(self.predicate, _stream)


class WhereMany(Stream):
    """
    For bulk queries, this automates the process of creating a large number of attribute queries and issuing them all
    that the same time.  This is noticeably faster than repeated `getAttr` calls.
    """

    def __init__(self, upstream=tuple(), attrib_query=None, invert=False):
        super(WhereMany, self).__init__(upstream=upstream)
        self.invert = invert
        if not hasattr(attrib_query, 'attribute') or not callable(attrib_query):
            raise QueryError, "query object must be a callable object with a a field called 'attribute'"
        self.attrib_query = attrib_query
        query_string = "{0}." + attrib_query.attribute
        self.attribute_factory = lambda p: query_string.format(p)

    def __iter__(self):
        _make_attrib = self.attribute_factory
        op = self.attrib_query.operator
        comp = self.attrib_query.comp
        cached_attrs, cached_objs = itertools.tee(self.incoming, 2)
        attrib_stream = itertools.imap(_make_attrib, cached_attrs)
        value_stream = get_values(attrib_stream)

        inverter = lambda p: operator.xor(self.invert, p)

        for obj, val in itertools.izip(cached_objs, value_stream):
            if inverter(op(val, comp)):
                yield obj


class Like(Stream):
    """
    applies the supplied regex to all elements in the input stream, returning items matching the regex. If the
    optional 'exact' flag is passed, the regex must be a conplete match (re.match) otherwise, partial matches are
    allowed(re.search)
    """

    def __init__(self, upstream=tuple(), regex='.', exact=False):
        super(Like, self).__init__(upstream=upstream)
        self.regex = re.compile(regex, re.I)
        self.exact = exact

    def __iter__(self):
        _stream = iter(self.incoming)
        if self.exact:
            return itertools.ifilter(self.regex.match, _stream)
        else:
            return itertools.ifilter(self.regex.search, _stream)


class OfType(Stream):
    """
    Filters the incoming stream using cmds.ls() to include only items of the supplied type(s).

    Type arguments can be strings or minq.nodes.NodeType instances

    The optional namespace argument allows you to filter responses to only a particular namespace:

        no argument     return all results, regardless of namespaces
        ''              return all results, regardless of namespaces
        '.'             any namespace but the root
        ':"             only objects in root namespace
        <ns>            any namespace path including ns ns:object, xxx:ns:object
        <:ns>           absolute namespace ns, eg :ns:object,  but not xxx:ns:object

    nested namespaces can be passed directly, so  namespace  'rig'  will match |rig:object, |scene:rig:object and
    |rig:scene:object but 'rig:scene', 'scene:rig'
    """

    def __init__(self, upstream=tuple(), *types, **kwargs):
        super(OfType, self).__init__(upstream=upstream)
        self.delegate = None
        self.namespace = kwargs.get('namespace', False)


        # support single or multiple types in a NodeType class
        # mixed with strings
        type_strings = []
        for t in types:
            if hasattr(t, 'TAG'):
                if hasattr(t.TAG, '__iter__'):
                    type_strings.extend(t.TAG)
                else:
                    type_strings.append(t.TAG)
            else:
                type_strings.append(str(t))
        self.types = type_strings

        quasi = [q for q in types if isinstance(q, type) and issubclass(q, QuasiFilter)]
        if not quasi:
            return
        if len(types) > 1:
            raise QueryError, "%s cannot be combined with other filters" % quasi[0].__class__.__name__
        self.delegate = quasi[0].filter

    def __iter__(self):

        output_stream = None
        if self.delegate:
            output_stream = self.delegate(self.incoming)
        else:
            output_stream = iter(get_list(self.incoming, type=self.types or 'entity', long=True))

        if self.namespace:

            if self.namespace == ':':  # returns only unrootd
                namspace_expression = '''(.*\|)([^:]+$)'''
            else:  # return permissive match of namespace, but trim leading / trailing colons
                ns = re.sub('^:', '(?<=\|)', self.namespace)
                ns = re.sub(':$', '', ns)
                namspace_expression = """(?!:.*\|+){0}:[\w:_]*$""".format(ns)
            output_stream = iter(Like(output_stream, namspace_expression))

        return output_stream


class Distinct(Stream):
    """
    Filters the incoming stream, removing duplicate elements
    """

    def __iter__(self):
        _seen = {None}
        _seen_add = _seen.add
        for element in itertools.ifilterfalse(_seen.__contains__, self.incoming):
            _seen_add(element)
            yield element


class SetOp(Stream):
    """
    Base class for set-like operations on streams.
    """
    OP = operator.or_

    def __init__(self, left, right):
        super(SetOp, self).__init__(left)
        self.right = right

    def __iter__(self):
        _left_set = set(self.incoming)
        _right_set = set(self.right)
        return iter(self.OP(_left_set, _right_set))


class Union(SetOp):
    OP = operator.or_


class Difference(SetOp):
    OP = operator.sub


class Intersection(SetOp):
    OP = operator.and_


class XOr(SetOp):
    OP = operator.xor


class Short(Stream):
    """
    returns the short names of the supplied stream. Non-maya values will be filtered out
    """

    def __iter__(self):
        return get_list(self.incoming, sn=True)


class Long(Stream):
    """
    returns the long names of items in the supplied stream.  Non-maya values will be filtered out
    """

    def __iter__(self):
        return get_list(self.incoming, long=True)


class UUID(Stream):
    """
    returns the long names of items in the supplied stream.  Non-maya values will be filtered out
    """

    def __iter__(self):
        return get_list(self.incoming, uuid=True)


class Sort(Stream):
    """
    Sorts the incoming stream. If a key function is supplied, uses the key function

    Note this must run all the upstream queries so it is comparatively expensive.
    """

    def __init__(self, incoming, key=None):
        super(Sort, self).__init__(incoming)
        self.key = key

    def __iter__(self):
        _result = [i for i in self.incoming]
        _result.sort(key=self.key)
        return iter(_result)


class NodeType(Stream):
    """
    Base class for different types of Maya nodes.  NodeTypes can be used as filters on an existing stream or as the
    basis of a new stream:

        Meshes()

    returns a stream with all of the mesh shapes in the scene, while

        Shapes().like('name').only(Meshes)

    will filter the stream of shapes with 'name' in their names down to only meshes.

    there's a complete list of pre-made NodeTypes in minq.nodes
    """
    TAG = tuple()

    def __iter__(self):

        if self.incoming == tuple():
            return iter(cmds.ls(type=self.TAG, long=True))
        else:
            return get_list(self.incoming, type=self.TAG, long=True)

    def __str__(self):
        return self.TAG


class QuasiFilter(object):
    """
    A Mixin Base class for items which are not covered by ls -type, to make them have the same behavior as NodeTypes.
     So, for example

        Assemblies()

    is a stream of top-level transforms while

        stream_of_nodes.only(Assemblies)

    will return only the nodes in <stream_of_nodes> which are also assemblies.


    """

    @classmethod
    def filter(cls, stream):
        raise NotImplementedError, "override in derived class"


class NodeTypeSet(Stream, QuasiFilter):
    """
    This allows you to combine several type filters into one for speed
    """

    def __init__(self, upstream=tuple(), *node_types):
        super(NodeTypeSet, self).__init__(upstream)
        self.node_types = node_types

    def __iter__(self):
        return cmds.ls(type=self.node_types, long=True)

    def filter(self, stream):
        return get_list(stream, type=self.node_types, long=True)


class Selected(NodeType, QuasiFilter):
    """
    Returns of filters the currently selected nodes
    """
    TAG = 'selected'

    def __iter__(self):
        return iter(cmds.ls(selection=True, long=True))

    @classmethod
    def filter(cls, stream):
        return get_list(stream, selection=True, long=True)


class Objects(NodeType, QuasiFilter):
    """
    Applies the 'objectsOnly' filter to the current stream which will convert strings including attributes to node
    names.
    """
    TAG = 'objectsOnly'

    def __iter__(self):
        return iter(get_list([None], objectsOnly=True, long=True))

    @classmethod
    def filter(cls, stream):
        return get_list(stream, objectsOnly=True, long=True)


class Assemblies(NodeType, QuasiFilter):
    TAG = 'assembly'

    def __iter__(self):
        return iter(cmds.ls(assemblies=True, long=True))

    @classmethod
    def filter(cls, stream):
        return get_list(stream, assemblies=True, long=True)


class Intermediates(NodeType, QuasiFilter):
    TAG = 'intermediates'

    def __iter__(self):
        return iter(cmds.ls(io=True, long=True))

    @classmethod
    def filter(cls, stream):
        return get_list(stream, io=True, long=True)


class NoIntermediates(NodeType, QuasiFilter):
    TAG = 'noIntermediates'

    def __iter__(self):
        return non_empty_stream(cmds.ls(ni=True, long=True))

    @classmethod
    def filter(cls, stream):
        return get_list(stream, ni=True, long=True)


class Templated(NodeType, QuasiFilter):
    # note by default 'ls -tm' includes a lot of junk which is not actually
    # templated.  This applies ls -type dag as well to prune that out.
    # it does not however try to account for the difference between
    # templated transforms and templated shapes
    TAG = 'templated'

    def __iter__(self):
        return non_empty_stream(cmds.ls(tm=True, type='dagNode', long=True))

    @classmethod
    def filter(cls, stream):
        return get_list(stream, tm=True, type='dagNode', long=True)


class Projection(Stream):
    """
    Base class for operations which change the contents of the current stream
    """

    def __init__(self, upstream=tuple(), *args, **kwargs):
        self.incoming = upstream
        self.args = args
        self.kwargs = kwargs


class ForEach(Projection):
    """
    Runs an arbitrary callable function on every item in a stream
    """

    def __iter__(self):
        return itertools.imap(self.args[0], self.incoming)


class Zip(Stream):
    """
    return a stream of tuples with this stream as the key values and supplied Projection as the field values.

    """

    def __init__(self, upstream=tuple(), **streams):
        self.incoming = upstream
        self.streams = streams.items()

    def __iter__(self):
        names = ['index'] + [item[0] for item in self.streams]
        result_row = namedtuple('dataRow', ' '.join(names))

        out_streams = [self.incoming]
        for k, v in self.streams:
            out_streams.append(self.incoming.get(v))

        for result in itertools.izip_longest(*out_streams, fillvalue=None):
            yield result_row(*result)


class Join(Projection):
    """
    Return a stream of tuples with this stream as the key value and the other streams as named fields
    """

    def __init__(self, upstream=tuple(), **streams):
        self.incoming = upstream
        self.streams = sorted(streams.items())

    def __iter__(self):

        names = ['index'] + [item[0] for item in self.streams]
        result_row = namedtuple('dataRow', ' '.join(names))

        out_streams = [self.incoming]
        for k, v in self.streams:
            out_streams.append(v)

        for result in itertools.izip_longest(*out_streams):
            yield result_row(*result)
