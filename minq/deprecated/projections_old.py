"""
this submodule contains operators which change incoming data: for example, returning the result of a function on each incoming item

"""
import itertools
import posixpath
from collections import namedtuple

from external.minq.minq.deprecated.core import Iterate
from .relations import ComponentFilter
import maya.cmds as cmds
from .util import XYZ


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


class PolyEvaluateCommand(Iterate):
    '''
    Base class for commands that return poly topology queries.

    '''
    CMD = cmds.polyEvaluate
    FLAGS = {}

    def _run(self, *args, **kwargs):
        return ((p, self.CMD(p, **self.flags)) for p in args)


class vertex_counts(PolyEvaluateCommand):
    """
    Return (object, vertex count(object)) for each object in the stream
    """

    FLAGS = {'v': True}


class areas(PolyEvaluateCommand):
    """
    Return (object, world area(object)) for each object in the stream.

    To get the local space area instead, use parens:

        ~meshes().areas(world=False)

    for local space or

        ~meshes().areas(world=True)

    for world space
    """
    FLAGS = {'wa': True}

    def __call__(self, *args, **kwargs):
        if kwargs.get('world'):
            self.flags = {'wa': True}
        else:
            self.flags = {'a': True}


class edge_counts(PolyEvaluateCommand):
    """
    Return (object, edge count(object)) for items in stream
    """
    FLAGS = {'edges': True}


class face_counts(PolyEvaluateCommand):
    """
    Return (object, face count(object)) for items in stream.  Note that 'faces' is polygons, not triangles.
    """
    FLAGS = {'face': True}


class triangle_counts(PolyEvaluateCommand):
    """
    Return (object, tri count(object)) for items in stream
    """

    FLAGS = {'triangle': True}


class uv_counts(PolyEvaluateCommand):
    """
    Return (object, uv count(object)) for items in stream

    To specify a uv set name, use the parens:

         ~meshes().uv_counts(uvs = 'map2')

     will return the count of uvs in the 'map2' uv set
    """

    FLAGS = {'uv': True}

    def __call__(self, *args, **kwargs):
        uvs = kwargs.get('uvs', kwargs.get('uvSetName', None))
        if uvs:
            self.flags['uvs'] = uvs


class attribs(Iterate):
    """
    Converts a list of objects into a list of attributes. Items in the list which don't have the attribute will not be
    passed.

       cameras().attributes("orthographic")
       # Result:  ("|top|topShape.orthographic", "|front\frontShape.orthographic" ... etc) #

    but meshes().attributes("orthographic")

       #Result:  (,) #

    Since non-existent objects are removed from the list, you can use this to find objects that have an attribute using
    the `.objects` filter:

        objects_with_attr = transforms().attribs("customAttribute").objects.distinct

    """
    FLAGS = {'attrib': 'nodeState'}

    def _run(self, *args, **kwargs):
        attrib = self.flags['attrib']
        attributed = lambda p: "%s.%s" % (p, attrib)
        return cmds.ls([attributed(s) for s in args], long=True) or []

    def __call__(self, attrib):
        self.flags.update({'attrib': attrib})


class get_attribs(attribs):
    """
    Returns attribute, value pairs for the supplied attribute on all incoming item.  Items without that attribute
    will not be returned
    """

    FLAGS = {'attrib': 'nodeState'}

    def _run(self, *args, **kwargs):
        attributed = super(get_attribs, self)._run(*args, **kwargs)
        attrib_values = cmds.getAttr(*attributed)
        return itertools.izip(attributed, attrib_values)


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


class keys(cast):
    """
    Given an input list of (name, value) pairs, return only the names
    """

    def __init__(self, *args, **flags):
        super(keys, self).__init__(*args, **flags)
        self.expression = lambda p: p[0]


class values(cast):
    """
    Given an input list of (name, value) pairs, return only the values
    """

    def __init__(self, *args, **flags):
        super(values, self).__init__(*args, **flags)
        self.expression = lambda p: p[-1]
