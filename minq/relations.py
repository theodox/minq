import re

from .core import Operator, DisjointOperator
import maya.cmds as cmds


class ListHistoryCommand(Operator):
    CMD = cmds.listHistory


class history(Operator):
    CMD = cmds.listHistory
    FLAGS = {'future': False}


class future(Operator):
    CMD = cmds.listHistory
    FLAGS = {'future':True}


class ListRelativesBase(Operator):
    CMD = cmds.listRelatives
    FLAGS = {'fullPath': True}


class children(ListRelativesBase):
    FLAGS = {'fullPath': True, 'children': True}

    def __call__(self, shapes=False):
        self.flags['shapes'] = shapes
        self.flags['children'] = not shapes





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


