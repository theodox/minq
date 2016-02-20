from external.minq.minq.deprecated.core import Operator
import maya.cmds as cmds


class LSBase(Operator):
    """
    Base class for ls commands
    """
    CMD = cmds.ls
    FLAGS = {'long': True}


class scene(LSBase):
    """
    Convenience wrapper for a default query: it returns everything in the scene.
    """
    SOURCE_ONLY = True


class selected(LSBase):
    """
    Pass selected items
    """
    FLAGS = {'long': True, 'selection': True}


class templated(LSBase):
    """
    Pass templated objects.  If called, a true value filters for templated and a false value for untemplated
    """
    FLAGS = {'long': True, 'templated': True}

    def __call__(self, templated=True):
        self.flags['templated'] = templated
        self.flags['untemplated'] = not templated


class intermediates(LSBase):
    """
    Pass or exclude intermediate objects.  By default

        .intermediates()

    will pass _only_ intermediate objects; while

        .intermediates(False)

    will filter out intermediates instead.

    """
    FLAGS = {'long': True, 'intermediateObjects': True}

    def __call__(self, inter=True):
        self.flags['intermediateObjects'] = inter
        self.flags['noIntermediate'] = not inter


class objects(LSBase):
    """
    Pass only objects for objects (no components or attributes)
    """
    FLAGS = {'long': True, 'objectsOnly': True}


class short_names(LSBase):
    """
    Pass all incoming items as short names
    """
    FLAGS = {'long': False}


class long_names(LSBase):
    """
    Ensure all incoming items are Passed as long names
    
    This should not usually be necessary since most operators use long names by default. However some operations and 
    custom user commands may not, so this can be used to make sure that results are consistent.
    """
    FLAGS = {'long': True}


class below(LSBase):
    """
    Pass any dag objects below the incoming objects. Includes both shapes and transforms.  
    
    below includes the _entire_ hierarchy below supplied the source object.  For immediate children only use 
    `.children()` (in minq.relations)
    """
    FLAGS = {'long': True, 'dagObjects': True}


class roots(LSBase):
    """
    Pass only items at the scene root level.
    """
    FLAGS = {'long': True, 'assemblies': True}


class leaves(LSBase):
    """
    Pass only items which have no children
    
    There are several ways to filter for items with no children, the fastest is probably 
    
        <query> - <same query>.leaves
    """
    FLAGS = {'long': True, 'dag': True, 'leaf': True}


class of_type(LSBase):
    """
    Pass only objects of the supplied type(s).  By default, derived types are included, so for example 
    
        .of_type('lambert') 
    
    will Pass all shaders. To restrict it to specific types use the 'exact = True'.  So
    
        .of_type('lambert', exact=True)
        
    will Pass only lamberts and no other shader types

    The type value is one or more strings.  minq.nodes includes a complete list of the valid node types.
    """

    FLAGS = {'long': True}

    def __call__(self, *types, **kw):
        if kw.get('exact'):
            self.flags['exactType'] = types
        else:
            self.flags['type'] = types


class LSByType(LSBase):
    """
    Base class for pre-built type queries. Don't use directly.
    """
    TYPE = 'node'
    FLAGS = {'long': True}

    def __init__(self, *args, **flags):
        d = dict(**flags)
        d['type'] = self.TYPE
        super(LSByType, self).__init__(*args, **d)


# by default, use a hand-built list of common nodes types. nodes.py contains a much longer and more complete list.
#   The longer list is complete for maya 2016 but may not be accurate for earlier or later versions.
# It's also full of rarely used nodes which may be distracting. However if you have very fast autocomplete
# you may want to use it instead: in that case copy it into this module in place of the classes below


class animCurves(LSByType):
    """
    Pass animCurves
    """
    TYPE = 'animCurve'


class bakeSets(LSByType):
    """
    Pass only bakeSets
    """

    TYPE = 'bakeSet'


class birails(LSByType):
    """
    Pass only birails
    """

    TYPE = 'birailSrf'


class blends(LSByType):
    """
    Pass only blends
    """

    TYPE = 'blend'


class caches(LSByType):
    """
    Pass only caches
    """

    TYPE = 'cacheBase'


class cameras(LSByType):
    """
    Pass only cameras
    """

    TYPE = 'camera'


class constraints(LSByType):
    """
    Pass only constraints
    """

    TYPE = 'constraint'


class curves(LSByType):
    """
    Pass only curves
    """

    TYPE = 'curveShape'


class surface_curves(LSByType):
    """
    Pass only surface_curves
    """

    TYPE = ('curveFromMesh', 'curveFromSubdiv', 'curveFromSurface')


class dagNode(LSByType):
    """
    Pass only dagNode
    """

    TYPE = 'dagNode'


class deformers(LSByType):
    """
    Pass only deformers
    """

    TYPE = 'geometryFilter'


class dimensions(LSByType):
    """
    Pass only dimensions
    """

    TYPE = 'dimensionShape'


class entities(LSByType):
    """
    Pass only entities
    """

    TYPE = 'entity'


class fields(LSByType):
    """
    Pass only fields
    """

    TYPE = 'field'


class filters(LSByType):
    """
    Pass only filters
    """

    TYPE = 'filter'


class geometry(LSByType):
    """
    Pass only geometry
    """

    TYPE = 'geometryShape'


class joints(LSByType):
    """
    Pass only joints
    """

    TYPE = 'joint'


class lights(LSByType):
    """
    Pass only lights
    """

    TYPE = 'light'


class surfaces(LSByType):
    """
    Pass only surfaces
    """

    TYPE = 'nurbsSurface'


class manips(LSByType):
    """
    Pass only manips
    """

    TYPE = ('manip2D', 'manip3D')


class meshes(LSByType):
    """
    Pass only meshes
    """

    TYPE = ('mesh')


class nodes(LSByType):
    """
    Pass only nodes
    """

    TYPE = 'node'


class pfx(LSByType):
    """
    Pass only paintFX geometry
    """

    TYPE = 'pfxGeometry'


class planes(LSByType):
    """
    Pass only planes
    """

    TYPE = 'plane'


class poly_creators(LSByType):
    """
    Pass only poly creators
    """

    TYPE = 'polyBase'


class poly_modifiers(LSByType):
    """
    Pass only poly modifiers
    """

    TYPE = 'polyModifier'


class poly_uv_modifiers(LSByType):
    """
    Pass only poly uv modifiers
    """

    TYPE = 'polyModifierUV'


class primitive(LSByType):
    """
    Pass only primitives
    """

    TYPE = 'primitive'


class shading_nodes(LSByType):
    """
    Pass only shading nodes
    """

    TYPE = 'shadingDependNode'


class shapes(LSByType):
    """
    Pass only shape nodes
    """

    TYPE = 'shape'

class shaders(LSByType):
    """
    Pass only shaders
    """
    TYPE = 'lambert'

class sgs(LSByType):
    """
    Pass only shader groups
    """
    TYPE = 'shadingEngine'


class skins(LSByType):
    """
    Pass only skin clusters
    """

    TYPE = 'skinCluster'


class transforms(LSByType):
    """
    Pass only transforms
    """

    TYPE = 'transform'


class subd_creators(LSByType):
    """
    Pass only subdivision creators
    """

    TYPE = 'subdBase'


class subd_modifieres(LSByType):
    """
    Pass only subdivisision modifiers
    """

    TYPE = 'subdModifier'


class subd_uv_modifiers(LSByType):
    """
    Pass only subdivision UV modifiers
    """

    TYPE = 'subdModifierUV'


class sets(LSByType):
    """
    Pass only sets
    """

    TYPE = 'objectSet'


class surfaces(LSByType):
    """
    Pass only nurbs surfaces
    """

    TYPE = 'surfaceShape'


class textures(LSByType):
    """
    Pass only textures
    """

    TYPE = ('texture2d', 'texture3d', 'textureEnv')
