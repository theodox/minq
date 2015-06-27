from minq.core import Operator

__author__ = 'stevet'

import maya.cmds as cmds


class LSBase(Operator):
    CMD = cmds.ls
    FLAGS = {'long': True}


class selection(LSBase):
    FLAGS = {'long': True, 'selection': True}


class LSByType(LSBase):
    TYPE = 'node'
    FLAGS = {'long': True}

    def __init__(self, *args, **flags):
        d = dict(**flags)
        d['type'] = self.TYPE
        super(LSByType, self).__init__(*args, **d)


class animCurves(LSByType):
    TYPE = 'animCurve'


class assemblies(LSByType):
    TYPE = 'assembly'


class bakeSets(LSByType):
    TYPE = 'bakeSet'


class birails(LSByType):
    TYPE = 'birailSrf'


class blends(LSByType):
    TYPE = 'blend'


class caches(LSByType):
    TYPE = 'cacheBase'


class cameras(LSByType):
    TYPE = 'camera'


class constraints(LSByType):
    TYPE = 'constraint'


class curves(LSByType):
    TYPE = 'curveShape'


class surface_curves(LSByType):
    TYPE = ('curveFromMesh', 'curveFromSubdiv', 'curveFromSurface')


class dagNode(LSByType):
    TYPE = 'dagNode'


class dimensions(LSByType):
    TYPE = 'dimensionShape'


class entities(LSByType):
    TYPE = 'entity'


class fields(LSByType):
    TYPE = 'field'


class filters(LSByType):
    TYPE = 'filter'


class geometry(LSByType):
    TYPE = 'geometryShape'


class lights(LSByType):
    TYPE = 'light'


class surfaces(LSByType):
    TYPE = 'nurbsSurface'


class manips(LSByType):
    TYPE = ('manip2D', 'manip3D')


class nodes(LSByType):
    TYPE = 'node'


class pfx(LSByType):
    TYPE = 'pfxGeometry'


class planes(LSByType):
    TYPE = 'plane'


class poly_creators(LSByType):
    TYPE = 'polyBase'


class poly_modifiers(LSByType):
    TYPE = 'polyModifier'


class poly_uv_modifiers(LSByType):
    TYPE = 'polyModifierUV'


class primitive(LSByType):
    TYPE = 'primitive'


class reflect(LSByType):
    TYPE = 'reflect'


class shading_nodes(LSByType):
    TYPE = 'shadingDependNode'


class shape(LSByType):
    TYPE = 'shape'


class subd_creators(LSByType):
    TYPE = 'subdBase'


class subd_modifieres(LSByType):
    TYPE = 'subdModifier'


class subd_uv_modifiers(LSByType):
    TYPE = 'subdModifierUV'


class surfaces(LSByType):
    TYPE = 'surfaceShape'


class textures(LSByType):
    TYPE = ('texture2d', 'textures3d', 'textureEnv')

