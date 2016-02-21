'''
This module contains NodeType objects, which can be used to start a Stream or as arguments to an .only() function.

If you want to filter on a node not listed here, you can use pass the name of the node type as as string to .only():

    birails = Scene().only('birailSrf')

If you want to use a type not listed as the root of a Stream you can declare it using this pattern:

    class Birails(NodeType):
        TAG = 'birailSrf'

Or, you can use the function 'node_type_factory' to create a class definition for you.  It's possible for a NodeType
to contain more than one maya type: if you have a common combination you could provide a tuple of types rather than
a single string:

    class NurbsAndMeshes(NodeType):
        TAG = ('mesh', 'nurbsSurface')


'''

from minq.core import NodeType


def node_type_factory(name, node_string):
    return type(
        name, (NodeType,), {'TAG': node_string}
    )


class Transforms(NodeType):
    TAG = 'transform'


class Constraints(NodeType):
    TAG = 'constraint'


class ControlPoints(NodeType):
    TAG = 'controlPoint'


class CurveShapes(NodeType):
    TAG = 'curveShape'


class DagNodes(NodeType):
    TAG = 'dagNode'


class DeformableShapes(NodeType):
    TAG = 'deformableShape'


class Fields(NodeType):
    TAG = 'field'


class GeometryShapes(NodeType):
    TAG = 'geometryShape'


class IkSolvers(NodeType):
    TAG = 'ikSolver'


class Lights(NodeType):
    TAG = 'light'


class Planes(NodeType):
    TAG = 'plane'


class PolyBases(NodeType):
    TAG = 'polyBase'


class PolyCreators(NodeType):
    TAG = 'polyCreator'


class PolyModifiers(NodeType):
    TAG = 'polyModifier'


class PolyPrimitives(NodeType):
    TAG = 'polyPrimitive'


class Primitives(NodeType):
    TAG = 'primitive'


class ShadingDependNodes(NodeType):
    TAG = 'shadingDependNode'


class Shapes(NodeType):
    TAG = 'shape'


class SubdBases(NodeType):
    TAG = 'subdBase'


class SubdModifiers(NodeType):
    TAG = 'subdModifier'


class SurfaceShapes(NodeType):
    TAG = 'surfaceShape'


class Texture2ds(NodeType):
    TAG = 'texture2d'


class Texture3ds(NodeType):
    TAG = 'texture3d'


class TextureEnvs(NodeType):
    TAG = 'textureEnv'


class ShaderfxShaders(NodeType):
    TAG = 'ShaderfxShader'


class StingrayPBSs(NodeType):
    TAG = 'StingrayPBS'


class AnimCurves(NodeType):
    TAG = 'animCurve'


class BlendShapes(NodeType):
    TAG = 'blendShape'


class Brushes(NodeType):
    TAG = 'brush'


class Cameras(NodeType):
    TAG = 'camera'


class Characters(NodeType):
    TAG = 'character'


class Cloths(NodeType):
    TAG = 'cloth'


class Clusters(NodeType):
    TAG = 'cluster'


class Containers(NodeType):
    TAG = 'container'


class DagContainers(NodeType):
    TAG = 'dagContainer'


class DagPoses(NodeType):
    TAG = 'dagPose'


class DisplayLayers(NodeType):
    TAG = 'displayLayer'


class Expressions(NodeType):
    TAG = 'expression'


class GeoConnectors(NodeType):
    TAG = 'geoConnector'


class GeomBinds(NodeType):
    TAG = 'geomBind'


class GeometryFilters(NodeType):
    TAG = 'geometryFilter'


class HikSolvers(NodeType):
    TAG = 'hikSolver'


class IkEffectors(NodeType):
    TAG = 'ikEffector'


class IkHandles(NodeType):
    TAG = 'ikHandle'


class ImagePlanes(NodeType):
    TAG = 'imagePlane'


class Joints(NodeType):
    TAG = 'joint'


class JointClusters(NodeType):
    TAG = 'jointCluster'


class Lamberts(NodeType):
    TAG = 'lambert'


class Locators(NodeType):
    TAG = 'locator'


class LodGroups(NodeType):
    TAG = 'lodGroup'


class Meshes(NodeType):
    TAG = 'mesh'


class Mutes(NodeType):
    TAG = 'mute'


class NCloths(NodeType):
    TAG = 'nCloth'


class NComponents(NodeType):
    TAG = 'nComponent'


class NParticles(NodeType):
    TAG = 'nParticle'


class NRigids(NodeType):
    TAG = 'nRigid'


class Networks(NodeType):
    TAG = 'network'


class NonLinears(NodeType):
    TAG = 'nonLinear'


class NurbsCurves(NodeType):
    TAG = 'nurbsCurve'


class NurbsSurfaces(NodeType):
    TAG = 'nurbsSurface'


class ObjectSets(NodeType):
    TAG = 'objectSet'


class ObjectTypeFilters(NodeType):
    TAG = 'objectTypeFilter'


class Particles(NodeType):
    TAG = 'particle'


class Partitions(NodeType):
    TAG = 'partition'


class Phongs(NodeType):
    TAG = 'phong'


class PolyProjs(NodeType):
    TAG = 'polyProj'


class Projections(NodeType):
    TAG = 'projection'


class References(NodeType):
    TAG = 'reference'


class Scripts(NodeType):
    TAG = 'script'


class Sculpts(NodeType):
    TAG = 'sculpt'


class ShadingEngines(NodeType):
    TAG = 'shadingEngine'


class SkinClusters(NodeType):
    TAG = 'skinCluster'


class Transforms(NodeType):
    TAG = 'transform'


class Trims(NodeType):
    TAG = 'trim'


class Unknowns(NodeType):
    TAG = 'unknown'


class UnknownDags(NodeType):
    TAG = 'unknownDag'


class UnknownTransforms(NodeType):
    TAG = 'unknownTransform'

