"""
this submodule contains operators which change incoming data: for example, returning the result of a function on each incoming item
"""
import itertools
import re

from .core import DisjointOperator
from .relations import ComponentFilter
import maya.cmds as cmds


class Iterate(DisjointOperator):
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
    returns the transform hierarchy chain above all incoming up to the root transforms
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


class where(Iterate):
    def _run(self, *args, **kwargs):
        return itertools.ifilter(self.expression, args)


class where_not(Iterate):
    def _run(self, *args, **kwargs):
        return itertools.ifilterfalse(self.expression, args)


class like(Iterate):
    def __init__(self, *args, **kwargs):
        super(like, self).__init__(*args, **kwargs)
        self.re = re.compile(".")

    def _run(self, *args, **kwargs):
        is_match = lambda p: self.re.search(p) is not None

        return itertools.ifilter(is_match, args)

    def __call__(self, *args):
        self.re = re.compile(*args)


class cast(Iterate):
    """
    Return the result of the supplied single-item function for ever item in the list
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
    return <expr> on all incoming items; equivalent to [expr(i) for i in incoming]
    """

    def _run(self, *args, **kwargs):
        return ((p, self.expression(p)) for p in args)


class distinct(Iterate):
    def _run(self, *args, **kwargs):
        return iter(set(args))


class ordered(Iterate):
    def _run(self, *args, **kwargs):
        results = [i for i in args]
        return iter(sorted(results, reverse=self.flags.get('reverse', False), key=self.flags.get('key')))

    def __call__(self, reverse=False, key=None):
        self.flags['reverse'] = reverse
        self.flags['key'] = key


class XformCommand(Iterate):
    '''
    Base class for commands that return transform queries
    '''
    CMD = cmds.xform
    FLAGS = {'q': True, 'ws': True, 'a': True}

    def _run(self, *args, **kwargs):
        return ((p, self.CMD(p, **self.flags)) for p in args)

    def __call__(self, world=True, abs=True):
        self.flags.update({'ws': world, 'a': abs})


class translations(XformCommand):
    FLAGS = {'q': True, 'ws': True, 'a': True, 't': True}


class rotations(XformCommand):
    FLAGS = {'q': True, 'ws': True, 'a': True, 'ro': True}


class scales(XformCommand):
    FLAGS = {'q': True, 'ws': True, 'a': True, 's': True}


class pivots(XformCommand):
    FLAGS = {'q': True, 'ws': True, 'a': True, 'piv': True}


class matrices(XformCommand):
    FLAGS = {'q': True, 'ws': True, 'matrix': True}
