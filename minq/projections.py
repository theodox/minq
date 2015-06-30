"""
this submodule contains operators which change incoming data: for example, returning the result of a function on each incoming item
"""
import itertools
import re

from .core import DisjointOperator
from .relations import ComponentFilter
import maya.cmds as cmds


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


class where(Iterate):
    """
    Pass only items which pass the supplied predicate function.  For example:

        has_an_x = lambda p: x in p
        Scene('a', 'b', 'x').where(has_an_x)

    will return just 'x'
    """
    def _run(self, *args, **kwargs):
        return itertools.ifilter(self.expression, args)


class where_not(Iterate):
    """
    Pass only items which _fail_ the supplied predicate: the inverse of 'where'
    """

    def _run(self, *args, **kwargs):
        return itertools.ifilterfalse(self.expression, args)


class like(Iterate):
    """
    Pass only items matching the supplied regex.  So:

        Scene('top', 'bottom').like('to')

    will pass ('top', 'bottom'), while:

        Scene('top', 'bottom').like('^to')

    will only pass 'top' since the regex matches only the start of the string due to the '^'.

    You can also use the regex compile arguments:

        .like("xyz", re.I)

    will match ("XYZ", 'xyz' and 'XyZ')
    """
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


class distinct(Iterate):
    """
    Returns only one copy of all incoming items. Useful for queries which return duplicate items.
    """
    def _run(self, *args, **kwargs):
        return iter(set(args))


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


class XformCommand(Iterate):
    '''
    Base class for commands that return transform queries.

    Xform commands return *world space*, *absolute* values by default. Get local values py passing world = False. For example:

         world_positions = query.translations
         local_positions = query.translations(world=False)

    '''
    CMD = cmds.xform
    FLAGS = {'q': True, 'ws': True}

    def _run(self, *args, **kwargs):
        return ((p, self.CMD(p, **self.flags)) for p in args)

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
    FLAGS = {'q': True, 'ws': True,  'piv': True}


class matrices(XformCommand):
    """
    Return the matrix for each incoming transform
    """
    FLAGS = {'q': True, 'ws': True, 'matrix': True}

class bounds (XformCommand):
    """
    Return the bounding box for each incoming transform.  This is equivalent to

        [ (i, cmds.xform(i, q=True, ws=True, bb=True)) for i in query]
    """
    FLAGS = {'q': True, 'ws': True, 'bb': True}
