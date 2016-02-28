import itertools
from collections import namedtuple

import maya.cmds as cmds
from minq.core import Projection, get_relatives, get_list, non_empty_stream, get_history, get_connections, get_values, QueryError


__author__ = 'Steve'


class Parents(Projection):
    def __iter__(self):
        return get_relatives(self.incoming, p=True, f=True, **self.kwargs)


class Children(Projection):
    def __iter__(self):
        return get_relatives(self.incoming, c=True, f=True, **self.kwargs)


class AllParents(Projection):
    def __iter__(self):

        parents = {''}
        for path in get_list(self.incoming, l=True):
            while path:
                if path in parents:
                    path = None
                else:
                    parents.add(path)
                    path, _, __ = path.rpartition("|")

        return non_empty_stream(cmds.ls(*parents, long=True))


class AllChildren(Projection):
    def __iter__(self):
        return get_relatives(self.incoming, ad=True, f=True, **self.kwargs)


class History(Projection):
    def __iter__(self):
        return get_list(get_history(self.incoming, **self.kwargs), long=True)


class Future(Projection):
    def __iter__(self):
        return get_list(get_history(self.incoming, future=True, **self.kwargs), long=True)


class Connections(Projection):
    def __iter__(self):
        return get_connections(self.incoming, **self.kwargs)


class Attribute(Projection):
    """
    Yields a stream of attribute names for the incoming streams. For example

        Cameras().get(Attribute, 'orthographic')

    will produce something like

        Stream([u'['topShape.orthographic', 'sideShape.orthographic', ...])

    This can be filtered to objects that have actually have the attribute by
    passing it to an ObjectsOnly:

        Shapes().get(Attributes, 'orthographic').only(ObjectsOnly)

    is equivalent to

        cmds.ls( "*.orthographic", objectsOnly = True)

    You can pass multiple attributes if needed
    """

    def __iter__(self):

        def attrib_generator():
            for item in self.incoming:
                base = item + "."
                for attrib in self.args:
                    yield base + attrib

        attrib_stream = iter(attrib_generator())

        if self.kwargs.get('valid', False):
            return get_list(attrib_stream)
        return attrib_stream


class Values(Projection):
    """
    Returns all of the values for a stream of attributes: for example

        Transforms().get(Attribute, 'tx').get(Values)

    will yield a stream of all the translateX values in the scene.
    """

    def __iter__(self):
        return get_values(self.incoming, **self.kwargs)


class AttribValues(Projection):
    """
    Combines a call to Attribute() and Values() into one operation for convenience

        Transforms().get(AttribValues, 'tx')

    """
    def __iter__(self):
        attrib_stream = Attribute(self.incoming, self.args[0])
        return iter(Values(attrib_stream, **self.kwargs))


class Counts(Projection):
    """
    Base class for queries which get the size of array attributes.  This
    uses the same bulk attribute queires as Valuess() so it is much faster
    that running  multiple pokyEvaluates() or similar calls
    """
    ATTRIBUTE = 'vrts'

    def __iter__(self):
        attrib_stream = Attribute(self.incoming, self.ATTRIBUTE)
        return iter(Values(attrib_stream, s=True))


class VertCount(Counts):
    """
    Get the vertex counts of a mesh stream
    """
    ATTRIBUTE = 'vrts'


class FaceCount(Counts):
    """
    Get the poly face counts of a mesh stream
    """
    ATTRIBUTE = 'face'


class ColorCount(Counts):
    """
    Get color vertex count of a mesh stream
    """
    ATTRIBUTE = 'color'


class TweakCount(Counts):
    """
    Get the number of tweakss (the .pnts attribuute) on a shape steam
    """

    ATTRIBUTE = 'pnts'


class CVCount(Counts):
    """
    Gets the cv counts on a nurbs stream
    """
    ATTRIBUTE = 'controlPoints'


class UVSetCount(Counts):
    """
    Gets the count of uv  sets in a mesh stream
    """
    ATTRIBUTE = 'uvSet'


class UVPointCount(Counts):
    """
    Gets the count of uv vertices in the current uv set of a mesh stream
    """
    ATTRIBUTE = 'uv'


class Types(Projection):
    """
    Returns a stream of tuples (object, nodeType) for every object in the
    incoming stream.
    """
    TYPE_TUPLE = namedtuple('objectType', 'object type')

    def __iter__(self):
        _tuple = lambda p: self.TYPE_TUPLE(*p)
        nodes_and_types = get_list(self.incoming, showType=True)
        object_names, type_names = itertools.tee(nodes_and_types, 2)
        out_stream = itertools.izip(itertools.islice(object_names, None, None, 2),
                                    itertools.islice(type_names, 1, None, 2))

        return itertools.imap(_tuple, out_stream)
