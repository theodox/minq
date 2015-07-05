"""
this submodule contains operators which change incoming data: for example, returning the result of a function on each incoming item

"""
import itertools
import posixpath
from collections import namedtuple

from .core import DisjointOperator
from .relations import ComponentFilter
import maya.cmds as cmds
from .util import XYZ


class Iterate(DisjointOperator):
    """
    Base class for operations which run a callable procedure on every item in the incoming query.
    """

    def __init__(self, *args, **flags):
        self.command = self._run
        self.args = args
        d = dict(**flags)
        d.update(self.FLAGS)
        self.flags = d
        self.expression = lambda p: p

    def _run(self, *args, **kwargs):
        return itertools.imap(self.expression, args)

    def _eval(self):
        return self._run(*self.args)

    def __call__(self, expr):
        self.expression = expr

    def _format_expression(self, command, args, flags):
        cmd = str(self.expression)
        arglist = []
        if len(args):
            arglist.append("\n\t*" + args.__repr__())
        if len(flags):
            arglist.append("\n\t**" + flags.__repr__())
        return "{}({})".format(cmd, ",".join(arglist))


class above(Iterate):
    """
    Produces the transform hierarchy chain above all incoming up to the root transforms.  This is the inverse of
    `below` in minq.ls
    """

    def _run(self, *args, **kwargs):
        def iter_parents(source):

            parents, _, __ = source.rpartition("|")
            if parents:
                yield parents
                for item in iter_parents(parents):
                    yield item

        parentage = lambda p: (i for i in iter_parents(p))

        results = (i for i in itertools.chain.from_iterable(itertools.imap(parentage, args)))
        return iter(set(results))


class cast(Iterate):
    """
    Return the result of the supplied single-item function for ever item in the list. For example:

        example = lambda p: p.upper()
        Scene('top', 'front').cast(example)

    will return ("TOP", "FRONT")
    """

    def __init__(self, *args, **flags):
        self.command = self._run
        self.args = args
        self.flags = flags
        self.expression = lambda p: p

    def _run(self, *args, **kwargs):
        return itertools.imap(self.expression, args)


class indices(cast):
    """
    Return the indexed part of incoming components, ie 'pCube1.vtx[1]' becomes 1
    """

    def __init__(self, *args, **kwargs):
        super(indices, self).__init__(*args, **kwargs)
        self.expression = ComponentFilter.index


class zip(Iterate):
    """
    Return (item, cast(item)) for all incoming items.

    Like .cast() runs the supplied function on every incoming item, but returns the original item alongside the
    result as a tuple.  The result can be turned into a dictionary:

        Scene('top', 'front').zip(lambda p: len(p))

    will return  [('top', 3),  ('front', 5)]
    """

    def _run(self, *args, **kwargs):
        return ((p, self.expression(p)) for p in args)


class node_types(Iterate):
    """
    Return (item, nodeType(item)) for every incoming item.

    Like `.zip()`, can be turned into a dictionary
    """
    def _run(self, *args, **kwargs):
        return itertools.imap(lambda p: (p, cmds.nodeType(p)), args)



class ordered(Iterate):
    """
    Returns all incoming items sorted using a standard python sort (ie, alphanumeric order).

    Accepts the same arguments as python 'sorted':

        Expression('zzz', 'aaa', 'bbb').sorted

    will return

        ['aaa', 'bbb', 'zzz']

    while

        Expression('zzz', 'aaa', 'bbb').sorted(reverse = True)

    will return

        ['zzz', 'bbb', 'aaa']

    You can also use the python 'key' parameter to provide a custom sort:

        Expression( 'aaaaa', 'z').sorted(key = lambda p: len(p))

    will return

        ['z', 'aaaaa']
    """

    def _run(self, *args, **kwargs):
        results = [i for i in args]
        return iter(sorted(results, reverse=self.flags.get('reverse', False), key=self.flags.get('key')))

    def __call__(self, reverse=False, key=None):
        self.flags['reverse'] = reverse
        self.flags['key'] = key


# convenience tuple wrappers
Bounds = namedtuple('bounds', 'minx miny minz max maxy maxz')
Matrix = namedtuple('matrix', 'm00 m01 m02 m03 m10 m11 m12 m13 m20 m21 m22 m23 m30 m31 m32 m33')


class XformCommand(Iterate):
    '''
    Base class for commands that return transform queries.

    Xform commands return *world space*, *absolute* values by default. Get local values py passing world = False. For example:

         world_positions = query.translations
         local_positions = query.translations(world=False)

    Results are returned as a tuple (object, value) where the object is the maya transform path and the value is the
    result of the query.  This makes it easy to do

        dict(meshes().parents.translations)
        # Result: {u'|pSphere1': XYZ(x=1.0, y=2.0, z=3.0), u'|pPlane1': XYZ(x=0.0, y=2.0, z=0.0), u'|pCube1': XYZ(x=0.0, y=0.0, z=0.0)} #

    '''
    CMD = cmds.xform
    FLAGS = {'q': True, 'ws': True}
    TRANSFORM = XYZ

    def _run(self, *args, **kwargs):
        return ((p, self.TRANSFORM(*self.CMD(p, **self.flags))) for p in args)

    def __call__(self, world=True):
        self.flags.update({'ws': world})


class translations(XformCommand):
    """
    Return the translation for each incoming transform
    """
    FLAGS = {'q': True, 'ws': True, 't': True}


class rotations(XformCommand):
    """
    Return the rotation for each incoming transform
    """
    FLAGS = {'q': True, 'ws': True, 'ro': True}


class scales(XformCommand):
    """
    Return the scale for each incoming transform
    """
    FLAGS = {'q': True, 'ws': True, 's': True}


class pivots(XformCommand):
    """
    Return the pivot for each incoming transform
    """
    FLAGS = {'q': True, 'ws': True, 'piv': True}


class matrices(XformCommand):
    """
    Return the matrix for each incoming transform
    """
    FLAGS = {'q': True, 'ws': True, 'matrix': True}
    TRANSFORM = Matrix


class bounds(XformCommand):
    """
    Return the bounding box for each incoming transform.  This is equivalent to

        [ (i, cmds.xform(i, q=True, ws=True, bb=True)) for i in query]
    """
    FLAGS = {'q': True, 'ws': True, 'bb': True}
    TRANSFORM = Bounds


class get_attr(Iterate):
    """
    Returns attribute, value pairs for the supplied attribute on all incoming item.  Items without that attribute
    will not be returned
    """

    FLAGS = {'attrib': 'nodeState'}

    def _run(self, *args, **kwargs):
        attrib = self.flags['attrib']
        attributed = lambda p: "%s.%s" % (p, attrib)
        attribute_strings = cmds.ls([attributed(s) for s in args])
        attrib_values = cmds.getAttr(*attribute_strings)
        return itertools.izip(attribute_strings, attrib_values)

    def __call__(self, attrib):
        self.flags.update({'attrib': attrib})


class relative(Iterate):
    """
    Return all of the long paths transformed using path style syntax: thus

        cameras.relative("..")

    will return the ['top', 'persp', 'front', 'side'] because the transforms are one level above the shapes returned
    by cameras.

    The generated paths are not guaranteed to actually exist: you can filter them by adding a long_names or
    short_names after this operator to winnow out nonexistent results.
    """

    FLAGS = {'path': ""}

    def _run(self, *args, **kwargs):
        pth = self.flags['path']
        convert = lambda p: posixpath.normpath(p.replace("|", "/") + pth)
        relativized = (convert(p) for p in args)
        no_pipes = lambda p: p.replace('/', '|') if len(p) > 1 else ''
        return (no_pipes(q) for q in relativized)

    def __call__(self, relpath):
        self.flags.update({'path': '/' + relpath.replace('|', '/')})
