import re
import itertools
import logging

import maya.cmds as cmds

# almost ready to go away

logging.basicConfig()
_log = logging.getLogger('minq')


class QueryMeta(type):
    """
    Root metaclass for queries. It allows for declarative flags:

       class Example(object):
           _CMD = cmds.ls.py
           __metaclass__ = QueryMeta

           shapes = True
           transforms = False

    will produce a class that calls cmds.ls.py(shapes=True, transforms = False) when resultsd.

    All classes are registered so that querys can spawn sub-queries
    """
    _CLASSES = {}

    def __new__(cls, name, bases, dct):
        kw_dictionary = dict(long=True)
        for k, v in dct.items():
            if not callable(v) and not k.startswith("_"):
                kw_dictionary[k] = v
                del dct[k]
        dct['_FLAGS'] = kw_dictionary
        QueryMeta._CLASSES[name] = type.__new__(cls, name, bases, dct)
        return QueryMeta._CLASSES[name]

    @staticmethod
    def get_type(name):
        return QueryMeta._CLASSES.get(name, None)


class Composable(object):
    """
    Base class for queries which can be chained together, such as multiple ls.py flags
    """

    def compose(self, other_type):
        replacement = other_type(upstream=self.upstream)
        kw = dict(self._instance_flags)
        kw.update(replacement._FLAGS)
        replacement._instance_flags = kw
        return replacement

    def __getattr__(self, name):
        target_class = QueryMeta.get_type(name)
        if target_class is None:
            raise NameError, "No QueryMeta extansion named " + name
        if issubclass(target_class, Composable) \
                and target_class._CMD == self._CMD:
            return self.compose(target_class)
        else:
            return target_class(upstream=self)


class QueryBase(object):
    """
    Allows for lazy execution a maya command (usually ls.py, but this change in derived classes) and iteration over thew results:

    A simple example:

        q = QueryBase('top*')

   produces a query object -- but as of yet it has no results: it's a description of a query you _could_ call, not a list of objects

   To get the result call it directly:

        print q.results()
        [u'|top', u'|top|topShape']

   iterating over the results also calls the query:

       for item in q:
           print item

       |top
       |top|topShape

    This class and its derivatives use the QueryMeta metaclass so they can specify command flags cleanly: most derived classes differ only in flags

    Queries can be chained together. All QueryMeta classes can 'chain' to other types, creating a cascading filter that will be evaluated only
    when called: For example:

       q = Query().Transforms.Filter('fred').WithChildren

    would find all the transforms in the scene with 'fred' in their names who have children, while

        q = Query('joint1').children.shapes

    would find all of the children of 'joint1' which are shapes.  As with a simple query, the actual values are not
    retrieved until the query is iterated or results are called
    """
    _CMD = cmds.ls
    __metaclass__ = QueryMeta


    def __init__(self, *args, **kwargs):
        self.upstream = kwargs.get('upstream', args)
        self.explicit = self.upstream == args
        self._instance_flags = dict(self._FLAGS)
        self.upstream = kwargs.get('upstream', args)
        self.explicit = self.upstream == args
        self._instance_flags = dict(self._FLAGS)


    def results(self):
        if self.upstream is not None:
            _log.info('calling %s' % self.__class__)
            return tuple(self._CMD(*[i for i in self.upstream], **self._instance_flags) or [])
        else:
            _log.info('empty input')
            return tuple()


    def first(self):
        return self.__iter__().next()


    def last(self):
        return self.results()[-1]


    def slice(self, *args):
        return itertools.islice(self, *args)


    def __iter__(self):
        return iter(self.results())


    def __getattr__(self, name):
        target_class = QueryMeta.get_type(name)
        if target_class is None:
            raise NameError, "No QueryMeta class named " + name
        return target_class(upstream=self)


    def __str__(self):
        rpr = {
            cmds.ls: "cmds.ls.py( {} )".format,
            cmds.listRelatives: "cmds.listRelatives( {} )".format,
            cmds.listHistory: "cmds.listHistory( {} )".format
        }

        quoted = lambda p: '"{}"'.format(p) if str(p) == p else p
        contents = lambda k, v: "{} = {}".format(k, quoted(v))
        kwargs = ", ".join([contents(k, v) for k, v in self._instance_flags.items()])
        if self.upstream:
            args = quoted(self.upstream) if not hasattr(self.upstream, '__iter__') else str(self.upstream)
            return rpr[self._CMD](", ".join((args, kwargs)))
        else:
            return rpr[self._CMD](kwargs)


    def __add__(self, other):
        result = iter(set(self).union(set(other)))
        return QueryBase(upstream=result)


    def __sub__(self, other):
        result = iter(set(self).union(set(other)))
        return QueryBase(upstream=result)


    def __xor__(self, other):
        result = iter(set(self).symmetric_difference(set(other)))
        return QueryBase(upstream=result)


    def __and__(self, other):
        result = iter(set(self).intersection(set(other)))
        return QueryBase(upstream=result)


    def __invert__(self):
        """
        shorthand for use in the listener
        """
        return self.results()


class SceneQuery(Composable, QueryBase):
    long = True

    pass


class Scene(SceneQuery):
    """
    A default query, similar to ls.py(). You can restrict it to known items by passing in an iterable (list, tuple or generator) of names:

        Query()  # returns everything in the scene
        Query(['a', 'b','c'])   # returns a, b and c, can be filtered or expanded
    """

    pass


class Attributes(Composable, QueryBase):
    """
    a global search for all instances of the supplied attribute in the scene:

        attributed('filename')

    will find all items with an attribute called 'filename'.
    """

    objectsOnly = False


    def __init__(self, *args):
        args = ["*." + i for i in args]
        super(Attributes, self).__init__(args)

    def results(self):
        # attribute queries often
        # return duplicate entries
        results = super(Attributes, self).results()
        return tuple(set(results))


class Selection(Composable, QueryBase):
    """
    A search which begins with the selected object(s)
    """
    selection = True
    long = True


class Shapes(Scene):
    long = True
    shapes = True


class Xforms(Scene):
    transforms = True
    long = True


# ----------
# these classes sub-set the query stream


class shortened(Scene):
    long = False


class selected(Scene):
    selected = True


class dag(Scene):
    dag = True
    objectsOnly = True


class nodes(Scene):
    dependencyNodes = True
    objectsOnly = True


class no_intermediates(Scene):
    noIntermediate = True


# ---- type filters. Can't be chained with xforms

class ByTypeBase(Scene):
    pass


class geometry(ByTypeBase):
    geometry = True


class lights(ByTypeBase):
    lights = True


class cameras(ByTypeBase):
    cameras = True


class meshes(ByTypeBase):
    type = 'mesh'


class curves(ByTypeBase):
    type = 'nurbsCuve'


class joints(ByTypeBase):
    type = 'joint'


class shaders(ByTypeBase):
    type = 'lambert'


class shading_nodes(ByTypeBase):
    type = 'shadingDependNode'


class constraints(ByTypeBase):
    type = 'constraint'


class IKs(ByTypeBase):
    type = 'ikhandle'


class of_type(ByTypeBase):
    """
    User specified type:

        Scene().of_type('HIKSkeletonGeneratorNode')

    """
    type = 'dag'

    def __call__(self, *types):
        self._instance_flags['type'] = types
        return self


class objects(Scene):
    """
    Pass objects only, typically used in conjunction with an attribute query:

       Query().attributed('filename').objects

   is equivalent to

        Query().attributed_objects('filename')
    """
    objectsOnly = True


# -----
# these classes filter the query stream, but they generally will force it to evaluate before proceeding


class Reprocess(QueryBase):
    _CMD = None


class xforms(Reprocess):
    _CMD = cmds.ls
    type = 'transform'

    def __init__(self, upstream, *args):
        if isinstance(upstream, ByTypeBase):
            raise AttributeError, "can't chain a transform filter onto a type query"
        super(xforms, self).__init__(upstream, args)

    def results(self):
        return tuple(self._CMD(self.upstream.results(), **self._instance_flags))


class with_children(Reprocess):
    _CMD = cmds.listRelatives


    def results(self):
        return tuple([i for i in self.upstream if cmds.listRelatives(i, c=True, fullPath=True) is not None])


class without_children(Reprocess):
    _CMD = cmds.listRelatives

    def results(self):
        return tuple([i for i in self.upstream if cmds.listRelatives(i, c=True) is None])


class children(Reprocess):
    _CMD = cmds.listRelatives

    def results(self):
        return tuple(self._CMD(*self.upstream, c=True, fullPath=True) or [])


class shapes(Reprocess):
    _CMD = cmds.listRelatives
    children = True
    shapes = True

    def results(self):
        r = [i for i in self.upstream]
        return tuple(self._CMD(*r, c=True, fullPath=True) or [])


class parents(Reprocess):
    _CMD = cmds.listRelatives

    def results(self):
        return tuple(self._CMD(*self.upstream, p=True, fullPath=True) or [])


class above(Reprocess):
    _CMD = cmds.listRelatives

    def results(self):
        return tuple(self._CMD(*self.upstream, ap=True, fullPath=True) or [])


class below(Reprocess):
    _CMD = cmds.listRelatives

    def results(self):
        return tuple(self._CMD(*self.upstream, ad=True, fullPath=True) or [])


class where(Reprocess):
    _CMD = None
    _predicate = lambda p: 1

    def __call__(self, predicate):
        self._predicate = predicate
        return self

    def results(self):
        return tuple(filter(self._predicate, (i for i in self.upstream)))

    def __iter__(self):
        return itertools.ifilter(self._predicate, self.upstream)


class named(where):
    def __call__(self, expr):
        self._re = re.compile(expr)
        self._predicate = lambda p: self._re.search(p.split("|")[-1]) is not None
        return self


class having(where):
    """
    Pass items in the query which have the supplied attribute (by default, attributes use long names: to use
    short names instead, pass the shortNames =True) flag

    This call will check the attribute on all items in the query, which will force the query to execute first.  For a global search of all attributed objects use AttrQuery
    """

    def __call__(self, expr, shortNames=False):
        self._attrib = expr
        if shortNames:
            self._predicate = lambda p: self._attrib in cmds.listAttr(p, sn=True)
        else:
            self._predicate = lambda p: self._attrib in cmds.listAttr(p)
        return self


class relative(Reprocess):
    '''
    transform all paths using file style relative paths  For example a query that returns  |A|B|C , with a relative
    path of "../D/E" , would pass this stage as "|A|B|D|E"
    '''

    def __init__(self, upstream):
        super(relative, self).__init__(upstream)
        self.path = ""

    def __call__(self, path):
        path = path.replace("/", "|")
        self.path = path.split("|")
        return self

    def results(self):
        return tuple(cmds.ls([self.splice_path(p) for p in self.upstream], **self._instance_flags))

    def splice_path(self, pth):
        segs = pth.split("|")
        for p in self.path:
            if p == "..":
                segs.pop()
            elif p == ".":
                continue
            else:
                segs.append(p)
        return "|".join(segs)


class topmost(Reprocess):
    '''
    for a set of results, return only those which are not children of any others in the set
    '''

    _CMD = None

    def results(self):
        results = [i for i in self.upstream]
        if not results:
            return tuple()
        results.sort()
        output = []
        for item in results:
            contained = False
            for o in output:
                contained = contained or o in item
            if not contained:
                output.append(item)

        return output


class cast(Reprocess):
    '''
    return all items in the query as processed by the supplied function, ie:

        query().cast(PyNode)

    would return all of the items int the list as PyNodes, while

        query.cast(lambda p: p.upper())

    would return all of the names in upper case
    '''

    def __call__(self, cast_fn):
        self.cast = cast_fn
        return self

    def results(self):
        return tuple([self.cast(i) for i in self.upstream])

    def __iter__(self):
        return itertools.imap(self.cast, self.upstream)


class history(Reprocess):
    _CMD = cmds.findType
    type = 'node'
    deep = True
    exact = False


    def __init__(self, *args, **kwargs):
        super(history, self).__init__(*args, **kwargs)
        del self._instance_flags['long']

    def results(self):
        r = [i for i in self.upstream]
        if len(r):
            return tuple((set(self._CMD(*r, **self._instance_flags) or [])))
        return tuple()

    def __call__(self, type='node', exact=False):
        self._instance_flags['type'] = type
        self._instance_flags['exact'] = exact
        return self


class future(Reprocess):
    _CMD = cmds.listHistory
    future = True
    allFuture = True

    def __init__(self, *args, **kwargs):
        super(future, self).__init__(*args, **kwargs)
        del self._instance_flags['long']

    def results(self):
        r = [i for i in self.upstream]
        if len(r):
            return tuple((set(self._CMD(*r, **self._instance_flags) or [])))
        return tuple()


def iter_history(obj, lv=0, interestLevel=0, seen=None, limit=999):
    if lv < limit:
        if not seen:
            seen = set()
        upstream = (i for i in cmds.listHistory(obj, lv=1, il=interestLevel) if i != obj)
        for item in upstream:
            if item[0] not in seen:
                yield item, lv
                seen.add(item)
            for subitem in iter_history(item, lv + 1, seen=seen, limit=limit):
                yield subitem


~Selection().shapes.history
Scene('polyUnite1').future.last()