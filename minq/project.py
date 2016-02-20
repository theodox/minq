from collections import namedtuple
import itertools
from minq.core import Projection, get_relatives, get_list, non_empty_stream, get_history, get_connections,  get_values

__author__ = 'Steve'


class Parents(Projection):
    def __iter__(self):
        return get_relatives(self.incoming, p=True, **self.kwargs)


class Children(Projection):
    def __iter__(self):
        return get_relatives(self.incoming, c=True, **self.kwargs)


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

        return non_empty_stream(cmds.ls(*parents))


class AllChildren(Projection):
    def __iter__(self):
        return get_relatives(self.incoming, ad=True, **self.kwargs)


class History(Projection):
    def __iter__(self):
        return get_history(self.incoming, **self.kwargs)


class Future(Projection):
    def __iter__(self):
        return get_history(self.incoming, future=True, **self.kwargs)


class Connections(Projection):
    def __iter__(self):
        return get_connections(self.incoming, **self.kwargs)


class Attribute(Projection):
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
    def __iter__(self):
        return get_values(self.incoming, **self.kwargs)


class Types(Projection):
    TYPE_TUPLE = namedtuple('objectType', 'object type')

    def __iter__(self):
        _tuple = lambda p: self.TYPE_TUPLE(*p)
        nodes_and_types = get_list(self.incoming, showType=True)
        object_names, type_names = itertools.tee(nodes_and_types, 2)
        out_stream = itertools.izip(itertools.islice(object_names, None, None, 2),
                                    itertools.islice(type_names, 1, None, 2))

        return itertools.imap(_tuple, out_stream)
