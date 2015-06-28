from .core import Operator

__author__ = 'stevet'

import maya.cmds as cmds


class LSBase(Operator):
    CMD = cmds.ls
    FLAGS = {'long': True}

class scene(LSBase):
    SOURCE_ONLY = True


class selected(LSBase):
    """
    filter for the selection
    """
    FLAGS = {'long': True, 'selection': True}


class templated(LSBase):
    """
    filter for templated objects.  If called, a true value filters for templated and a false value for untemplated
    """
    FLAGS = {'long': True, 'templated': True}

    def __call__(self, templated = True):
        self.flags['templated'] = templated
        self.flags['untemplated'] = not templated

class intermediates(LSBase):
    """
    filter for intermediate objects.  If called, use true to find intermediates or false to suppress them
    """
    FLAGS = {'long': True, 'intermediateObjects': True}

    def __call__(self, inter = True):
        self.flags['intermediateObjects'] = inter
        self.flags['noIntermediate'] = not inter



class objects(LSBase):
    """
    filter for objects (no components or attributes)
    """
    FLAGS = {'long': True, 'objects': True}

class below(LSBase):
    """
    Return any dag objects below the incoming objects. Includes both shapes and transforms
    """
    FLAGS = {'long': True, 'dagObjects': True}

class roots(LSBase):
    FLAGS = {'long': True, 'assemblies': True}

class leaves(LSBase):
    FLAGS = {'long': True, 'dag': True, 'leaf':True}


class of_type(LSBase):
    FLAGS = {'long': True}

    def __call__(self, *types, **kw):
        if kw.get('exact'):
            self.flags['exactType'] = types
        else:
            self.flags['type'] = types



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

class deformers(LSByType):
    TYPE = 'geometryFilter'

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


class joints(LSByType):
    TYPE = 'joint'


class lights(LSByType):
    TYPE = 'light'


class surfaces(LSByType):
    TYPE = 'nurbsSurface'


class manips(LSByType):
    TYPE = ('manip2D', 'manip3D')


class meshes(LSByType):
    TYPE = ('mesh')


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


class shapes(LSByType):
    TYPE = 'shape'


class skins(LSByType):
    TYPE = 'skinCluster'


class transforms(LSByType):
    TYPE = 'transform'


class subd_creators(LSByType):
    TYPE = 'subdBase'


class subd_modifieres(LSByType):
    TYPE = 'subdModifier'


class subd_uv_modifiers(LSByType):
    TYPE = 'subdModifierUV'

class sets(LSByType):
    TYPE = 'objectSet'

class surfaces(LSByType):
    TYPE = 'surfaceShape'


class textures(LSByType):
    TYPE = ('texture2d', 'texture3d', 'textureEnv')

