import re
import itertools

import maya.cmds as cmds


class QueryMeta(type):
    """
    Root metaclass for queries. It allows for declarative flags:

       class Example(object):
           _CMD = cmds.ls
           __metaclass__ = QueryMeta

           shapes = True
           transforms = False

    will produce a class that calls cmds.ls(shapes=True, transforms = False) when resultsd.

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
        if issubclass(target_class, Composable):
            return self.compose(target_class)
        else:
            return target_class(upstream=self)


class QueryBase(object):
    """
    Allows for lazy execution a maya command (usually ls, but this change in derived classes) and iteration over thew results:

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

        q = Query('joint1').Children.Shapes

    would find all of the children of 'joint1' which are shapes.  As with a simple query, the actual values are not
    retrieved until the query is iterated or results are calledd




    """
    _CMD = cmds.ls
    __metaclass__ = QueryMeta


    def __init__(self, upstream=None, *additional):
        if additional:
            self.upstream = (upstream) + additional
        self.upstream = upstream
        self._instance_flags = dict(self._FLAGS)

    def results(self):


        if self.upstream is None:
            return tuple(self._CMD(**self._instance_flags) or [])
        else:
            values, incoming = itertools.tee(self.upstream)
            if values.next():
                return tuple(self._CMD(*incoming, **self._instance_flags) or [])
            else:
                return tuple()


    def __iter__(self):
        return iter(self.results())

    def __getattr__(self, name):
        target_class = QueryMeta.get_type(name)
        if target_class is None:
            raise NameError, "No QueryMeta class named " + name
        return target_class(upstream=self)

    def __str__(self):
        rpr = {
            cmds.ls: "cmds.ls( {} )".format,
            cmds.listRelatives: "cmds.listRelatives( {} )".format,
            cmds.listHistory: "cmds.listHistory( {} )".format
        }

        quoted = lambda p: '"{}"'.format(p) if str(p) == p else p
        contents = lambda k, v: "{} = {}".format(k, quoted(v))
        args = quoted(self.upstream) if not hasattr(self.upstream, '__iter__') else str(self.upstream)
        kwargs = ", ".join([contents(k, v) for k, v in self._instance_flags.items()])
        return rpr[self._CMD](", ".join((args, kwargs)))


    def __add__(self, other):
        result = iter(set(self).union(set(other)))
        return QueryBase(result)

    def __sub__(self, other):
        result = iter(set(self).union(set(other)))
        return QueryBase(result)


    def __xor__(self, other):
        result = iter(set(self).symmetric_difference(set(other)))
        return QueryBase(result)

    def __and__(self, other):
        result = iter(set(self).intersection(set(other)))
        return QueryBase(result)


class Query(Composable, QueryBase):
    pass


class Selected(Query):
    selected = True


class Transforms(Query):
    transforms = True
    shapes = False
    objectsOnly = True


class Shapes(Query):
    shapes = True
    transforms = False
    objectsOnly = True


class Geometry(Query):
    geometry = True


class Lights(Shapes):
    lights = True


class Cameras(Shapes):
    cameras = True


class Dag(QueryBase):
    dag = True
    objectsOnly = True


class Nodes(QueryBase):
    dependencyNodes = True
    objectsOnly = True


class ByType(Nodes):
    type = 'dag'


class Meshes(ByType):
    type = 'mesh'


class Curves(ByType):
    type = 'nurbsCurve'


class Constraint(ByType):
    type = 'constraint'


class OfType(ByType):
    type = 'dag'

    def __call__(self, *types):
        self._instance_flags['type'] = types
        return self


class WithChildren(QueryBase):
    _CMD = cmds.listRelatives
    ignore = 1

    def results(self):
        return tuple([i for i in self.upstream if cmds.listRelatives(i, c=True) is not None])


class WithoutChildren(QueryBase):
    _CMD = cmds.listRelatives
    ignore = 1

    def results(self):
        return tuple([i for i in self.upstream if cmds.listRelatives(i, c=True) is None])


class Children(QueryBase):
    _CMD = cmds.listRelatives

    def results(self):
        return tuple(self._CMD(*self.upstream, c=True, fullPath=True) or [])


class Parents(QueryBase):
    _CMD = cmds.listRelatives

    def results(self):
        return tuple(self._CMD(*self.upstream, p=True, fullPath=True) or [])


class Above(QueryBase):
    _CMD = cmds.listRelatives

    def results(self):
        return tuple(self._CMD(*self.upstream, ap=True, fullPath=True) or [])


class Below(QueryBase):
    _CMD = cmds.listRelatives

    def results(self):
        return tuple(self._CMD(*self.upstream, ad=True, fullPath=True) or [])


class Where(QueryBase):
    _predicate = lambda p: 1

    def __call__(self, predicate):
        self._predicate = predicate
        return self

    def results(self):
        return tuple(filter(self._predicate, (i for i in self.upstream)))


class Named(Where):
    def __call__(self, expr):
        self._re = re.compile(expr)
        self._predicate = lambda p: self._re.search(p) is not None
        return self


class Attributes(Composable, QueryBase):
    objectsOnly = False

    def __init__(self, *args):
        args = ["*." + i for i in args]
        super(Attributes, self).__init__(args)

    def results(self):
        # attribute queries often
        # return duplicate entries
        results =  super(Attributes, self).results()
        return tuple(set(results))


class ObjectsWithAttributes(Attributes):
    objectsOnly = True

class Objects(Query):
    objectsOnly = True


class HasAttribute(Where):

    def __call__(self, expr, shortNames=False):
        self._attrib = expr
        if shortNames:
            self._predicate = lambda p: self._attrib in cmds.listAttr(p, sn=True)
        else:
            self._predicate = lambda p: self._attrib in cmds.listAttr(p)
        return self



a = Attributes("depth").Objects
b = Attributes("width").Objects
print (a & b).results()