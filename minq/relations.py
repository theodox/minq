import re

from .core import Operator, DisjointOperator
import maya.cmds as cmds


class ListHistoryCommand(Operator):
    CMD = cmds.listHistory


class history(ListHistoryCommand):
    CMD = cmds.listHistory
    FLAGS = {'future': False}


class future(ListHistoryCommand):
    FLAGS = {'future': True}


class inputs(ListHistoryCommand):
    FLAGS = {'future': False, 'levels': 1}


class outputs(ListHistoryCommand):
    FLAGS = {'future': True, 'levels': 1}


class ConnectionHelper(object):
    @classmethod
    def upstream(cls, *args, **kwargs):
        return iter(set(cmds.listConnections(*args, source=True, destination=False, scn=True) or []))

    @classmethod
    def downstream(cls, *args, **kwargs):
        return iter(set(cmds.listConnections(*args, source=False, destination=True, scn=True) or []))


class downstream(Operator):
    CMD = ConnectionHelper.downstream


class upstream(Operator):
    CMD = ConnectionHelper.upstream


class ListRelativesBase(Operator):
    CMD = cmds.listRelatives
    FLAGS = {'fullPath': True}


class children(ListRelativesBase):
    """
    return immediate children. If shapes is true, return only shape children
    """
    FLAGS = {'fullPath': True, 'children': True}

    def __call__(self, shapes=False):
        self.flags['shapes'] = shapes
        self.flags['children'] = not shapes


class parents(ListRelativesBase):
    """
    return immediate parents
    """
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

    @classmethod
    def convert_components(cls, *args, **kwargs):

        target = kwargs.get('to')
        target_mask = {
            'face': ({'tf': 1}, 34),
            'vertex': ({'tv': 1}, 31),
            'edge': ({'te': 1}, 32),
            'vtf': ({'tvf': 1}, 70)
        }[target]

        convert_args = target_mask[0]
        if 'internal' in kwargs:
            convert_args['internal'] = kwargs.get('internal')

        conversion = (i for i in cmds.polyListComponentConversion(*args, **convert_args))
        return cls.expand(*conversion, force=True, selectionMask=target_mask[1])


class FilterExpandCommand(Operator):
    CMD = ComponentFilter.expand

    def __call__(self, force=True, expand=True):
        self.flags.update(force=force, expand=expand)


class vertices(FilterExpandCommand):
    FLAGS = {'selectionMask': 31, 'fullPath': True}


class edges(FilterExpandCommand):
    FLAGS = {'selectionMask': 32, 'fullPath': True}


class faces(FilterExpandCommand):
    FLAGS = {'selectionMask': 34, 'fullPath': True}


class uvs(FilterExpandCommand):
    FLAGS = {'selectionMask': 35, 'fullPath': True}


class vertex_faces(FilterExpandCommand):
    FLAGS = {'selectionMask': 70, 'fullPath': True}


class cvs(FilterExpandCommand):
    FLAGS = {'selectionMask': 28, 'fullPath': True}


class eps(FilterExpandCommand):
    FLAGS = {'selectionMask': 30, 'fullPath': True}


class ComponentConversionCommand(DisjointOperator):
    CMD = ComponentFilter.convert_components
    FLAGS = {}

    def __call__(self, internal=False):
        if internal:
            self.flags['internal'] = True


class to_faces(ComponentConversionCommand):
    FLAGS = {'to': 'face'}


class to_vertices(ComponentConversionCommand):
    FLAGS = {'to': 'vertex'}


class to_edges(ComponentConversionCommand):
    FLAGS = {'to': 'edge'}


class to_vertex_faces(ComponentConversionCommand):
    FLAGS = {'to': 'vtf'}
