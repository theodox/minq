import itertools
import re

from minq.core import Operator, DisjointOperator
import maya.cmds as cmds


class ListHistoryCommand(Operator):
    CMD = cmds.listHistory


class ListRelativesBase(Operator):
    CMD = cmds.listRelatives
    FLAGS = {'fullPath': True}


class shape_children(ListRelativesBase):
    FLAGS = {'fullPath': True, 'shapes': True}


class parents(ListRelativesBase):
    FLAGS = {'fullPath': True, 'parent': True}


class ComponentFilter(object):
    """
    Helper class for working with components
    """
    EXPANSIONS = {
        31: 'vtx',
        32: 'e',
        34: 'f',
        35: 'map',
        70: 'vtxFace',
        28: 'cv',
        30: 'ep'
    }

    BRACKETS = re.compile("(\[)(\d*)(\])")

    @classmethod
    def componentize(cls, comp, mask):
        if '[' in comp:
            return comp
        return "%s.%s[*]" % (comp, cls.EXPANSIONS[mask])

    @classmethod
    def expand(cls, *args, **kwargs):
        mask = kwargs.get('selectionMask')
        force = kwargs.get('force', False)

        if force:
            args = [cls.componentize(i, mask) for i in args]

        if 'force' in kwargs:
            del kwargs['force']

        result = (i for i in cmds.filterExpand(*args, **kwargs) or [])
        return result

    @classmethod
    def index(cls, item):
        return int(cls.BRACKETS.search(item).groups()[1])


class FilterExpandCommand(Operator):
    CMD = ComponentFilter.expand

    def __call__(self, force=False, expand=True):
        self.flags.update(force=force, expand=expand)


class Vertices(FilterExpandCommand):
    FLAGS = {'selectionMask': 31, 'fullPath': True}


class Edges(FilterExpandCommand):
    FLAGS = {'selectionMask': 32, 'fullPath': True}


class Faces(FilterExpandCommand):
    FLAGS = {'selectionMask': 34, 'fullPath': True}


class UVs(FilterExpandCommand):
    FLAGS = {'selectionMask': 35, 'fullPath': True}


class VertexFaces(FilterExpandCommand):
    FLAGS = {'selectionMask': 70, 'fullPath': True}


class CVs(FilterExpandCommand):
    FLAGS = {'selectionMask': 28, 'fullPath': True}


class EPs(FilterExpandCommand):
    FLAGS = {'selectionMask': 30, 'fullPath': True}


class FindTypeCommand(Operator):
    CMD = cmds.findType
    FLAGS = {'deep': True}


class ConvertComponentCommand(DisjointOperator):
    CMD = cmds.polyListComponentConversion
    FLAGS = {}


class AsFaces(ConvertComponentCommand):
    FLAGS = {'tf': True}


class AsVertices(ConvertComponentCommand):
    FLAGS = {'tv': True}


class AsEdges(ConvertComponentCommand):
    FLAGS = {'te': True}


class AsVertexFace(ConvertComponentCommand):
    FLAGS = {'tvf': True}


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


class Where(Iterate):
    def _run(self, *args, **kwargs):
        return itertools.ifilter(self.expression, args)


class Where_Not(Iterate):
    def _run(self, *args, **kwargs):
        return itertools.ifilterfalse(self.expression, args)


class Cast(Iterate):
    def __init__(self, *args, **flags):
        self.command = self._run
        self.args = args
        self.flags = flags
        self.expression = lambda p: p

    def _run(self, *args, **kwargs):
        return itertools.imap(self.expression, args)


class Indices(Cast):
    """
    Return the indexed part of incoming components, ie 'pCube1.vtx[1]' becomes 1
    """

    def __init__(self, *args, **kwargs):
        super(Indices, self).__init__(*args, **kwargs)
        self.expression = ComponentFilter.index


class For_Each(Iterate):
    """
    return <expr> on all incoming items; equivalent to [expr(i) for i in incoming]
    """

    def _run(self, *args, **kwargs):
        return ((p, self.expression(p)) for p in args)

    def __call__(self, expr, world=True, abs=True):
        self.expression = expr
        self.flags = {'ws': world, 'a': abs}


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


class Translations(XformCommand):
    FLAGS = {'q': True, 'ws': True, 'a': True, 't': True}


class Rotations(XformCommand):
    FLAGS = {'q': True, 'ws': True, 'a': True, 'ro': True}


class Scales(XformCommand):
    FLAGS = {'q': True, 'ws': True, 'a': True, 's': True}


class Pivots(XformCommand):
    FLAGS = {'q': True, 'ws': True, 'a': True, 'piv': True}


class Matrices(XformCommand):
    FLAGS = {'q': True, 'ws': True, 'matrix': True}
        
