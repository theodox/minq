import itertools
import operator
import re
from collections import namedtuple

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
    post = False
    for item in stream:
        yield item
        post = True
    if not post:
        yield None


def command_stream(stream, cmd, **kwargs):
    """convenience wrapper for commands that need non_empty_streams"""
    safe = non_empty_stream(stream)
    return iter(cmd(*safe, **kwargs))


def get_list(stream, **kwargs):
    """return ls() on <stream> without ever returning everything"""
    return command_stream(stream, cmds.ls, **kwargs)


def get_relatives(stream, **kwargs):
    """return listRelatives() on <stream> without ever returning everything"""
    return command_stream(stream, cmds.listRelatives, **kwargs)


def get_history(stream, **kwargs):
    """return listHistory() on <stream> without ever returning everything"""
    return command_stream(stream, cmds.listHistory, **kwargs)


def get_connections(stream, **kwargs):
    """return listConnections() on <stream> without ever returning everything"""
    return command_stream(stream, cmds.listConnections, **kwargs)


def get_values(stream, **kwargs):
    """return listConnections() on <stream> without ever returning everything"""
    return command_stream(stream, cmds.getAttr, **kwargs)


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

    returns only items that are common to both streams
    """

    def __init__(self, upstream=tuple()):
        self.incoming = upstream

    def __iter__(self):
        return (i for i in self.incoming)

    def execute(self):
        """
        invcke the chain of queries whi
        """
        return [i for i in self]

    def cache(self):
        """
        returns a Stream wrapped around a the cached result of this query.  This is very useful to prevent repeatedly
        issuing the same maya queries.
        """
        return Stream(self.execute())

    def where(self, pred):
        """
        given a callable filter function, returns a new stream containing only  items  for which the filter function
        return a truth-tested value
        """
        return Where(self, pred)

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

    def only(self, *pred):
        """
        Returns a new stream containing only items of the supplied types.  The types can be string typenames (such as
        'transforms' or 'shapes') or they can be minq.core.NodeType classes.  So

            this_stream.only('transform')

        and

            this_stream.only(Transform)

        are equivalent.

        A handful of NodeTypes (such as ObjectsOnly or Assemblies) can't be combined with others in a single call:
        """
        return OfType(self, *pred)

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


'''
    def zip(self, **kwargs):
        """
        given a collection of named streams, return a table-like stream in which each 'row' has named values
        corresponnding to the original stream. This is used for coordinating multiple streams: for example:

             bones = Joints()
             bone_parents = bones.get(Parents)


        """
        return Zip(self, **kwargs)
'''


def join(self, **streams):
    """
    given a collection of named streams, return a table-like stream in which each 'row' has named values
    corresponnding to the original stream. This is used for coordinating multiple streams: for example:

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


def long(self):
    """
    Returns a new stream containing the long names of items in this stream. Any items which are not maya nodes in the
    steeam will be filtered out.
    """
    return Long(self)


def uuid(self):
    """
    Returns a new stream containing the uuids of items in this stream. Any items which are not maya nodes in the
    steeam will be filtered out.
    """
    return UUID(self)


def __add__(self, other):
    """
    Returns a new stream
    """
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


def __gt__(self, other):
    return self.only(other)


def __rshift__(self, otherKlass):
    return self.get(otherKlass)


def __repr__(self):
    return "stream: " + self.execute().__repr__()


class Where(Stream):
    """
    Applies the supplied predicate to everything in the stream filtering only items that pass the predicate function

    if the optional invert keyword is provided, returns only itemrs where predicate returns a False-y value
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


class Like(Stream):
    """
    applies the supplied regex to all elements in the imput stream, returning items matching the regex. If the
    optional 'exact' flag is passed, the regex must be a conplete match (re.match) otherwise, partial matches are
    allowed(re.seatch)
    """

    def __init__(self, upstream=tuple(), regex='.', exact=False):
        super(Like, self).__init__(upstream=upstream)
        self.regex = re.compile(regex, re.I)
        self.exact = exact

    def __iter__(self):
        _stream = iter(self.incoming)
        if self.exact:
            return (i for i in _stream if self.regex.match(i))
        else:
            return (i for i in _stream if self.regex.search(i))


class OfType(Stream):
    """
    Filters the incoming stream using cmds.ls() to include only items of the supplied type(s).

    Type arguments can be strings or minq.nodes.NodeType instances

    """

    def __init__(self, upstream=tuple(), *types):
        super(OfType, self).__init__(upstream=upstream)
        self.delegate = None
        as_type = lambda p: p.TAG if hasattr(p, 'TAG') else str(p)
        type_strings = [as_type(t) for t in types]
        for t in type_strings:
            if not t.isalnum():
                raise QueryError, "invalid type name: %s" % t
        self.types = map(as_type, types)

        quasi = [q for q in types if isinstance(q, type) and issubclass(q, QuasiFilter)]
        if not quasi:
            return
        if len(types) > 1:
            raise QueryError, "%s cannot be combined with other filters" % quasi[0].__class__.__name__
        self.delegate = quasi[0].filter

    def __iter__(self):
        if self.delegate:
            return self.delegate(self.incoming)
        return iter(cmds.ls(*self.incoming, type=self.types))


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
    OP = operator.iand


class Short(Stream):
    """
    returns the short names of the supplied stream. Non-maya values will be filtered out
    """

    def __iter__(self):
        return iter(cmds.ls(*self.incoming, sn=True))


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
    Base class for different types of Maya nodes.  NodeTypes can be used as filters on an existing stream or as the basis of a new stream:

        Meshes()

    returns a stream with all of the mesh shapes in the scene, while

        Shapes().like('name').only(Meshes)

    will filter the stream of shapes with 'name' in their names down to only meshes.
    """
    TAG = 'node'

    def __iter__(self):
        return iter(cmds.ls(type=self.TAG) or [])

    def __str__(self):
        return self.TAG


class QuasiFilter(object):
    """
    A Mixin Base class for items which are not covered by ls -type, to make them have the same behavior as NodeTypes.  So, for example

        Assemblies()

    is a stream of top-level transforms while

        stream_of_nodes.only(Assemblies)

    will return only the nodes in <stream_of_nodes> which are also assemblies.


    """

    @classmethod
    def filter(cls, stream):
        raise NotImplementedError, "override in derived class"


class DagNodes(NodeType):
    TAG = 'dagNode'


class Shapes(NodeType):
    TAG = 'shape'


class GeometryShapes(NodeType):
    TAG = 'geometryShape'


class Meshes(NodeType):
    TAG = 'mesh'


class Transforms(NodeType):
    TAG = 'transform'


class Cameras(NodeType):
    TAG = 'camera'


class Curves(NodeType):
    TAG = 'nurbsCurve'


class Joints(NodeType):
    TAG = 'joint'


class Constraints(NodeType):
    TAG = 'constraint'


class Lights(NodeType):
    TAG = 'light'


class Selected(NodeType, QuasiFilter):
    """
    Returns of filters the currently selected nodes
    """
    TAG = 'selected'

    def __iter__(self):
        return iter(cmds.ls(selection=True))

    @classmethod
    def filter(cls, stream):
        return get_list(stream, selection=True)


class Objects(NodeType, QuasiFilter):
    """
    Applies the 'objectsOnly' filter to the current stream which will convert strings including attributes to node names.
    """
    TAG = 'objectsOnly'

    def __iter__(self):
        return iter(get_list([None], objectsOnly=True))

    @classmethod
    def filter(cls, stream):
        return get_list(stream, objectsOnly=True)


class Assemblies(NodeType, QuasiFilter):
    TAG = 'assembly'

    def __iter__(self):
        return iter(get_list(assemblies=True))

    @classmethod
    def filter(cls, stream):
        return get_list(stream, assemblies=True)


class Intermediates(NodeType, QuasiFilter):
    TAG = 'intermediates'

    def __iter__(self):
        return iter(get_list(io=True))

    @classmethod
    def filter(cls, stream):
        return get_list(stream, io=True)


class NoIntermediates(NodeType, QuasiFilter):
    TAG = 'noIntermediates'

    def __iter__(self):
        return non_empty_stream(cmds.ls(io=True))

    @classmethod
    def filter(cls, stream):
        return get_list(stream, ni=True)


class Projection(Stream):
    """
    Base class for operations which change the contents of the current stream
    """
    def __init__(self, upstream=tuple(), *args, **kwargs):
        self.incoming = upstream
        self.args = args
        self.kwargs = kwargs


class Zip(Stream):
    """
    return a stream of tuples with this stream as the key values and supplied Projection as the field values.

    """

    def __init__(self, upstream=tuple(), **streams):
        self.incoming = upstream
        self.streams = streams.items()

    def __iter__(self):
        names = ['object'] + [item[0] for item in self.streams]
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

        names = ['object'] + [item[0] for item in self.streams]
        result_row = namedtuple('dataRow', ' '.join(names))

        out_streams = [self.incoming]
        for k, v in self.streams:
            out_streams.append(v)

        for result in itertools.izip_longest(*out_streams):
            yield result_row(*result)
