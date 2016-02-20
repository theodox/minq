'''
This module contains NodeType filters for all of the node classes in Maya 2015.  Early or later versions may have
slightly different node TAG lists. It's useful if you use an autocompleting IDE - otherwise it's only a convenience
to avoid typing 'of_type'
'''

from minq.core import NodeType


class AbstractBaseCreate(NodeType):
    TAG = 'abstractBaseCreate'


class AbstractBaseNurbsConversion(NodeType):
    TAG = 'abstractBaseNurbsConversion'


class AdskAssetInstanceNode_TdependNode(NodeType):
    TAG = 'adskAssetInstanceNode_TdependNode'


class AdskAssetInstanceNode_TdnTx2D(NodeType):
    TAG = 'adskAssetInstanceNode_TdnTx2D'


class AdskAssetInstanceNode_TlightShape(NodeType):
    TAG = 'adskAssetInstanceNode_TlightShape'


class AnimBlendNodeBase(NodeType):
    TAG = 'animBlendNodeBase'


class AnimCurve(NodeType):
    TAG = 'animCurve'


class BakeSet(NodeType):
    TAG = 'bakeSet'


class BaseGeometryVarGroup(NodeType):
    TAG = 'baseGeometryVarGroup'


class BaseShadingSwitch(NodeType):
    TAG = 'baseShadingSwitch'


class BirailSrf(NodeType):
    TAG = 'birailSrf'


class Blend(NodeType):
    TAG = 'blend'


class BoundaryBase(NodeType):
    TAG = 'boundaryBase'


class CacheBase(NodeType):
    TAG = 'cacheBase'


class ClientDevice(NodeType):
    TAG = 'clientDevice'


class Constraint(NodeType):
    TAG = 'constraint'


class ControlPoint(NodeType):
    TAG = 'controlPoint'


class CteInterpolator(NodeType):
    TAG = 'cteInterpolator'


class CurveFromMesh(NodeType):
    TAG = 'curveFromMesh'


class CurveFromSubdiv(NodeType):
    TAG = 'curveFromSubdiv'


class CurveFromSurface(NodeType):
    TAG = 'curveFromSurface'


class CurveNormalizer(NodeType):
    TAG = 'curveNormalizer'


class CurveRange(NodeType):
    TAG = 'curveRange'


class CurveShape(NodeType):
    TAG = 'curveShape'


class DagNode(NodeType):
    TAG = 'dagNode'


class DeformFunc(NodeType):
    TAG = 'deformFunc'


class DeformableShape(NodeType):
    TAG = 'deformableShape'


class DimensionShape(NodeType):
    TAG = 'dimensionShape'


class DynBase(NodeType):
    TAG = 'dynBase'


class Entity(NodeType):
    TAG = 'entity'


class Field(NodeType):
    TAG = 'field'


class Filter(NodeType):
    TAG = 'filter'


class GeometryShape(NodeType):
    TAG = 'geometryShape'


class GroundPlane(NodeType):
    TAG = 'groundPlane'


class HwShader(NodeType):
    TAG = 'hwShader'


class IkSolver(NodeType):
    TAG = 'ikSolver'


class ImageSource(NodeType):
    TAG = 'imageSource'


class Light(NodeType):
    TAG = 'light'


class MakeCircularArc(NodeType):
    TAG = 'makeCircularArc'


class Manip2D(NodeType):
    TAG = 'manip2D'


class Manip3D(NodeType):
    TAG = 'manip3D'


class NBase(NodeType):
    TAG = 'nBase'


class Node(NodeType):
    TAG = 'node'


class NonAmbientLightShapeNode(NodeType):
    TAG = 'nonAmbientLightShapeNode'


class NonExtendedLightShapeNode(NodeType):
    TAG = 'nonExtendedLightShapeNode'


class NurbsDimShape(NodeType):
    TAG = 'nurbsDimShape'


class OrthoGrid(NodeType):
    TAG = 'orthoGrid'


class ParentTessellate(NodeType):
    TAG = 'parentTessellate'


class PfxGeometry(NodeType):
    TAG = 'pfxGeometry'


class Plane(NodeType):
    TAG = 'plane'


class PolyBase(NodeType):
    TAG = 'polyBase'


class PolyCreator(NodeType):
    TAG = 'polyCreator'


class PolyModifier(NodeType):
    TAG = 'polyModifier'


class PolyModifierUV(NodeType):
    TAG = 'polyModifierUV'


class PolyModifierWorld(NodeType):
    TAG = 'polyModifierWorld'


class PolyPrimitive(NodeType):
    TAG = 'polyPrimitive'


class Primitive(NodeType):
    TAG = 'primitive'


class Reflect(NodeType):
    TAG = 'reflect'


class RenderLight(NodeType):
    TAG = 'renderLight'


class ResultCurve(NodeType):
    TAG = 'resultCurve'


class RevolvedPrimitive(NodeType):
    TAG = 'revolvedPrimitive'


class ShadingDependNode(NodeType):
    TAG = 'shadingDependNode'


class Shape(NodeType):
    TAG = 'shape'


class SubdBase(NodeType):
    TAG = 'subdBase'


class SubdModifier(NodeType):
    TAG = 'subdModifier'


class SubdModifierUV(NodeType):
    TAG = 'subdModifierUV'


class SubdModifierWorld(NodeType):
    TAG = 'subdModifierWorld'


class SurfaceShape(NodeType):
    TAG = 'surfaceShape'


class TexBaseDeformManip(NodeType):
    TAG = 'texBaseDeformManip'


class Texture2d(NodeType):
    TAG = 'texture2d'


class Texture3d(NodeType):
    TAG = 'texture3d'


class TextureEnv(NodeType):
    TAG = 'textureEnv'


class ThreadedDevice(NodeType):
    TAG = 'threadedDevice'


class WriteToFrameBuffer(NodeType):
    TAG = 'writeToFrameBuffer'


class AISEnvFacade(NodeType):
    TAG = 'AISEnvFacade'


class AlembicNode(NodeType):
    TAG = 'AlembicNode'


class ComputeGlobal(NodeType):
    TAG = 'ComputeGlobal'


class ComputeLocal(NodeType):
    TAG = 'ComputeLocal'


class CustomRigDefaultMappingNode(NodeType):
    TAG = 'CustomRigDefaultMappingNode'


class CustomRigRetargeterNode(NodeType):
    TAG = 'CustomRigRetargeterNode'


class HIKCharacterNode(NodeType):
    TAG = 'HIKCharacterNode'


class HIKCharacterStateClient(NodeType):
    TAG = 'HIKCharacterStateClient'


class HIKControlSetNode(NodeType):
    TAG = 'HIKControlSetNode'


class HIKEffector2State(NodeType):
    TAG = 'HIKEffector2State'


class HIKEffectorFromCharacter(NodeType):
    TAG = 'HIKEffectorFromCharacter'


class HIKFK2State(NodeType):
    TAG = 'HIKFK2State'


class HIKPinning2State(NodeType):
    TAG = 'HIKPinning2State'


class HIKProperty2State(NodeType):
    TAG = 'HIKProperty2State'


class HIKRetargeterNode(NodeType):
    TAG = 'HIKRetargeterNode'


class HIKSK2State(NodeType):
    TAG = 'HIKSK2State'


class HIKSkeletonGeneratorNode(NodeType):
    TAG = 'HIKSkeletonGeneratorNode'


class HIKSolverNode(NodeType):
    TAG = 'HIKSolverNode'


class HIKState2Effector(NodeType):
    TAG = 'HIKState2Effector'


class HIKState2FK(NodeType):
    TAG = 'HIKState2FK'


class HIKState2GlobalSK(NodeType):
    TAG = 'HIKState2GlobalSK'


class HIKState2SK(NodeType):
    TAG = 'HIKState2SK'


class ShaderfxShader(NodeType):
    TAG = 'ShaderfxShader'


class StingrayPBS(NodeType):
    TAG = 'StingrayPBS'


class Unfold3DOptimize(NodeType):
    TAG = 'Unfold3DOptimize'


class Unfold3DUnfold(NodeType):
    TAG = 'Unfold3DUnfold'


class AboutToSetValueTestNode(NodeType):
    TAG = 'aboutToSetValueTestNode'


class AddDoubleLinear(NodeType):
    TAG = 'addDoubleLinear'


class AddMatrix(NodeType):
    TAG = 'addMatrix'


class AdskMaterial(NodeType):
    TAG = 'adskMaterial'


class AdskPrepareRenderGlobals(NodeType):
    TAG = 'adskPrepareRenderGlobals'


class AimConstraint(NodeType):
    TAG = 'aimConstraint'


class AirField(NodeType):
    TAG = 'airField'


class AirManip(NodeType):
    TAG = 'airManip'


class AlignCurve(NodeType):
    TAG = 'alignCurve'


class AlignManip(NodeType):
    TAG = 'alignManip'


class AlignSurface(NodeType):
    TAG = 'alignSurface'


class AmbientLight(NodeType):
    TAG = 'ambientLight'


class AngleBetween(NodeType):
    TAG = 'angleBetween'


class AngleDimension(NodeType):
    TAG = 'angleDimension'


class AnimBlend(NodeType):
    TAG = 'animBlend'


class AnimBlendInOut(NodeType):
    TAG = 'animBlendInOut'


class AnimBlendNodeAdditive(NodeType):
    TAG = 'animBlendNodeAdditive'


class AnimBlendNodeAdditiveDA(NodeType):
    TAG = 'animBlendNodeAdditiveDA'


class AnimBlendNodeAdditiveDL(NodeType):
    TAG = 'animBlendNodeAdditiveDL'


class AnimBlendNodeAdditiveF(NodeType):
    TAG = 'animBlendNodeAdditiveF'


class AnimBlendNodeAdditiveFA(NodeType):
    TAG = 'animBlendNodeAdditiveFA'


class AnimBlendNodeAdditiveFL(NodeType):
    TAG = 'animBlendNodeAdditiveFL'


class AnimBlendNodeAdditiveI16(NodeType):
    TAG = 'animBlendNodeAdditiveI16'


class AnimBlendNodeAdditiveI32(NodeType):
    TAG = 'animBlendNodeAdditiveI32'


class AnimBlendNodeAdditiveRotation(NodeType):
    TAG = 'animBlendNodeAdditiveRotation'


class AnimBlendNodeAdditiveScale(NodeType):
    TAG = 'animBlendNodeAdditiveScale'


class AnimBlendNodeBoolean(NodeType):
    TAG = 'animBlendNodeBoolean'


class AnimBlendNodeEnum(NodeType):
    TAG = 'animBlendNodeEnum'


class AnimBlendNodeTime(NodeType):
    TAG = 'animBlendNodeTime'


class AnimClip(NodeType):
    TAG = 'animClip'


class AnimCurveTA(NodeType):
    TAG = 'animCurveTA'


class AnimCurveTL(NodeType):
    TAG = 'animCurveTL'


class AnimCurveTT(NodeType):
    TAG = 'animCurveTT'


class AnimCurveTU(NodeType):
    TAG = 'animCurveTU'


class AnimCurveUA(NodeType):
    TAG = 'animCurveUA'


class AnimCurveUL(NodeType):
    TAG = 'animCurveUL'


class AnimCurveUT(NodeType):
    TAG = 'animCurveUT'


class AnimCurveUU(NodeType):
    TAG = 'animCurveUU'


class AnimLayer(NodeType):
    TAG = 'animLayer'


class AnimLayerClip(NodeType):
    TAG = 'animLayerClip'


class AnimLayerClipContainer(NodeType):
    TAG = 'animLayerClipContainer'


class AnimLayerClipRoster(NodeType):
    TAG = 'animLayerClipRoster'


class AnimLayerClipRotation(NodeType):
    TAG = 'animLayerClipRotation'


class AnimLayerClipSingle(NodeType):
    TAG = 'animLayerClipSingle'


class AnimLayerClipTRS(NodeType):
    TAG = 'animLayerClipTRS'


class Anisotropic(NodeType):
    TAG = 'anisotropic'


class AnnotationShape(NodeType):
    TAG = 'annotationShape'


class ApfEntityNode(NodeType):
    TAG = 'apfEntityNode'


class ApfFileNode(NodeType):
    TAG = 'apfFileNode'


class ArcLengthDimension(NodeType):
    TAG = 'arcLengthDimension'


class AreaLight(NodeType):
    TAG = 'areaLight'


class ArrayMapper(NodeType):
    TAG = 'arrayMapper'


class ArrowManip(NodeType):
    TAG = 'arrowManip'


class AssemblyDefinition(NodeType):
    TAG = 'assemblyDefinition'


class AssemblyReference(NodeType):
    TAG = 'assemblyReference'


class AttachCurve(NodeType):
    TAG = 'attachCurve'


class AttachSurface(NodeType):
    TAG = 'attachSurface'


class AttrHierarchyTest(NodeType):
    TAG = 'attrHierarchyTest'


class Audio(NodeType):
    TAG = 'audio'


class AvgCurves(NodeType):
    TAG = 'avgCurves'


class AvgCurvesManip(NodeType):
    TAG = 'avgCurvesManip'


class AvgNurbsSurfacePoints(NodeType):
    TAG = 'avgNurbsSurfacePoints'


class AvgSurfacePoints(NodeType):
    TAG = 'avgSurfacePoints'


class AxesActionManip(NodeType):
    TAG = 'axesActionManip'


class BallProjManip(NodeType):
    TAG = 'ballProjManip'


class BarnDoorManip(NodeType):
    TAG = 'barnDoorManip'


class BaseLattice(NodeType):
    TAG = 'baseLattice'


class Bevel(NodeType):
    TAG = 'bevel'


class BevelManip(NodeType):
    TAG = 'bevelManip'


class BevelPlus(NodeType):
    TAG = 'bevelPlus'


class BezierCurve(NodeType):
    TAG = 'bezierCurve'


class BezierCurveToNurbs(NodeType):
    TAG = 'bezierCurveToNurbs'


class BifrostAeroMaterial(NodeType):
    TAG = 'bifrostAeroMaterial'


class BifrostAttrNotifier(NodeType):
    TAG = 'bifrostAttrNotifier'


class BifrostContainer(NodeType):
    TAG = 'bifrostContainer'


class BifrostFoamMaterial(NodeType):
    TAG = 'bifrostFoamMaterial'


class BifrostLiquidMaterial(NodeType):
    TAG = 'bifrostLiquidMaterial'


class BifrostShape(NodeType):
    TAG = 'bifrostShape'


class BlendColorSets(NodeType):
    TAG = 'blendColorSets'


class BlendColors(NodeType):
    TAG = 'blendColors'


class BlendDevice(NodeType):
    TAG = 'blendDevice'


class BlendManip(NodeType):
    TAG = 'blendManip'


class BlendShape(NodeType):
    TAG = 'blendShape'


class BlendTwoAttr(NodeType):
    TAG = 'blendTwoAttr'


class BlendWeighted(NodeType):
    TAG = 'blendWeighted'


class BlindDataTemplate(NodeType):
    TAG = 'blindDataTemplate'


class Blinn(NodeType):
    TAG = 'blinn'


class BoneLattice(NodeType):
    TAG = 'boneLattice'


class Boolean(NodeType):
    TAG = 'boolean'


class Boundary(NodeType):
    TAG = 'boundary'


class Brownian(NodeType):
    TAG = 'brownian'


class Brush(NodeType):
    TAG = 'brush'


class Bulge(NodeType):
    TAG = 'bulge'


class Bump2d(NodeType):
    TAG = 'bump2d'


class Bump3d(NodeType):
    TAG = 'bump3d'


class ButtonManip(NodeType):
    TAG = 'buttonManip'


class CMuscleCreator(NodeType):
    TAG = 'cMuscleCreator'


class CMuscleDebug(NodeType):
    TAG = 'cMuscleDebug'


class CMuscleDirection(NodeType):
    TAG = 'cMuscleDirection'


class CMuscleDisplace(NodeType):
    TAG = 'cMuscleDisplace'


class CMuscleDisplay(NodeType):
    TAG = 'cMuscleDisplay'


class CMuscleFalloff(NodeType):
    TAG = 'cMuscleFalloff'


class CMuscleKeepOut(NodeType):
    TAG = 'cMuscleKeepOut'


class CMuscleMultiCollide(NodeType):
    TAG = 'cMuscleMultiCollide'


class CMuscleObject(NodeType):
    TAG = 'cMuscleObject'


class CMuscleRelative(NodeType):
    TAG = 'cMuscleRelative'


class CMuscleShader(NodeType):
    TAG = 'cMuscleShader'


class CMuscleSmartCollide(NodeType):
    TAG = 'cMuscleSmartCollide'


class CMuscleSmartConstraint(NodeType):
    TAG = 'cMuscleSmartConstraint'


class CMuscleSpline(NodeType):
    TAG = 'cMuscleSpline'


class CMuscleSplineDeformer(NodeType):
    TAG = 'cMuscleSplineDeformer'


class CMuscleStretch(NodeType):
    TAG = 'cMuscleStretch'


class CMuscleSurfAttach(NodeType):
    TAG = 'cMuscleSurfAttach'


class CMuscleSystem(NodeType):
    TAG = 'cMuscleSystem'


class CacheBlend(NodeType):
    TAG = 'cacheBlend'


class CacheFile(NodeType):
    TAG = 'cacheFile'


class CaddyManip(NodeType):
    TAG = 'caddyManip'


class CaddyManipBase(NodeType):
    TAG = 'caddyManipBase'


class Camera(NodeType):
    TAG = 'camera'


class CameraManip(NodeType):
    TAG = 'cameraManip'


class CameraPlaneManip(NodeType):
    TAG = 'cameraPlaneManip'


class CameraSet(NodeType):
    TAG = 'cameraSet'


class CameraView(NodeType):
    TAG = 'cameraView'


class CenterManip(NodeType):
    TAG = 'centerManip'


class Character(NodeType):
    TAG = 'character'


class CharacterMap(NodeType):
    TAG = 'characterMap'


class CharacterOffset(NodeType):
    TAG = 'characterOffset'


class Checker(NodeType):
    TAG = 'checker'


class Choice(NodeType):
    TAG = 'choice'


class Chooser(NodeType):
    TAG = 'chooser'


class CircleManip(NodeType):
    TAG = 'circleManip'


class CircleSweepManip(NodeType):
    TAG = 'circleSweepManip'


class Clamp(NodeType):
    TAG = 'clamp'


class ClipGhostShape(NodeType):
    TAG = 'clipGhostShape'


class ClipLibrary(NodeType):
    TAG = 'clipLibrary'


class ClipScheduler(NodeType):
    TAG = 'clipScheduler'


class ClipToGhostData(NodeType):
    TAG = 'clipToGhostData'


class CloseCurve(NodeType):
    TAG = 'closeCurve'


class CloseSurface(NodeType):
    TAG = 'closeSurface'


class ClosestPointOnMesh(NodeType):
    TAG = 'closestPointOnMesh'


class ClosestPointOnSurface(NodeType):
    TAG = 'closestPointOnSurface'


class Cloth(NodeType):
    TAG = 'cloth'


class Cloud(NodeType):
    TAG = 'cloud'


class Cluster(NodeType):
    TAG = 'cluster'


class ClusterFlexorShape(NodeType):
    TAG = 'clusterFlexorShape'


class ClusterHandle(NodeType):
    TAG = 'clusterHandle'


class CoiManip(NodeType):
    TAG = 'coiManip'


class CollisionModel(NodeType):
    TAG = 'collisionModel'


class ColorManagementGlobals(NodeType):
    TAG = 'colorManagementGlobals'


class ColorProfile(NodeType):
    TAG = 'colorProfile'


class CompactPlugArrayTest(NodeType):
    TAG = 'compactPlugArrayTest'


class ComponentManip(NodeType):
    TAG = 'componentManip'


class ComposeMatrix(NodeType):
    TAG = 'composeMatrix'


class ConcentricProjManip(NodeType):
    TAG = 'concentricProjManip'


class Condition(NodeType):
    TAG = 'condition'


class Container(NodeType):
    TAG = 'container'


class ContainerBase(NodeType):
    TAG = 'containerBase'


class ContourProjManip(NodeType):
    TAG = 'contourProjManip'


class Contrast(NodeType):
    TAG = 'contrast'


class Controller(NodeType):
    TAG = 'controller'


class CopyColorSet(NodeType):
    TAG = 'copyColorSet'


class CopyUVSet(NodeType):
    TAG = 'copyUVSet'


class CpManip(NodeType):
    TAG = 'cpManip'


class Crater(NodeType):
    TAG = 'crater'


class CreaseSet(NodeType):
    TAG = 'creaseSet'


class CreateBPManip(NodeType):
    TAG = 'createBPManip'


class CreateCVManip(NodeType):
    TAG = 'createCVManip'


class CreateColorSet(NodeType):
    TAG = 'createColorSet'


class CreateEPManip(NodeType):
    TAG = 'createEPManip'


class CreatePtexUV(NodeType):
    TAG = 'createPtexUV'


class CreateUVSet(NodeType):
    TAG = 'createUVSet'


class Cte(NodeType):
    TAG = 'cte'


class CteAnimSource(NodeType):
    TAG = 'cteAnimSource'


class CteCurveVisualizer(NodeType):
    TAG = 'cteCurveVisualizer'


class CteInterpolatorRotation(NodeType):
    TAG = 'cteInterpolatorRotation'


class CteInterpolatorSingle(NodeType):
    TAG = 'cteInterpolatorSingle'


class CteInterpolatorTRS(NodeType):
    TAG = 'cteInterpolatorTRS'


class CteRoster(NodeType):
    TAG = 'cteRoster'


class CteTracks(NodeType):
    TAG = 'cteTracks'


class CubeManip(NodeType):
    TAG = 'cubeManip'


class CubicProjManip(NodeType):
    TAG = 'cubicProjManip'


class CurveEdManip(NodeType):
    TAG = 'curveEdManip'


class CurveFromMeshCoM(NodeType):
    TAG = 'curveFromMeshCoM'


class CurveFromMeshEdge(NodeType):
    TAG = 'curveFromMeshEdge'


class CurveFromSubdivEdge(NodeType):
    TAG = 'curveFromSubdivEdge'


class CurveFromSubdivFace(NodeType):
    TAG = 'curveFromSubdivFace'


class CurveFromSurfaceBnd(NodeType):
    TAG = 'curveFromSurfaceBnd'


class CurveFromSurfaceCoS(NodeType):
    TAG = 'curveFromSurfaceCoS'


class CurveFromSurfaceIso(NodeType):
    TAG = 'curveFromSurfaceIso'


class CurveInfo(NodeType):
    TAG = 'curveInfo'


class CurveIntersect(NodeType):
    TAG = 'curveIntersect'


class CurveNormalizerAngle(NodeType):
    TAG = 'curveNormalizerAngle'


class CurveNormalizerLinear(NodeType):
    TAG = 'curveNormalizerLinear'


class CurveSegmentManip(NodeType):
    TAG = 'curveSegmentManip'


class CurveVarGroup(NodeType):
    TAG = 'curveVarGroup'


class CylindricalProjManip(NodeType):
    TAG = 'cylindricalProjManip'


class DagContainer(NodeType):
    TAG = 'dagContainer'


class DagPose(NodeType):
    TAG = 'dagPose'


class DataBlockTest(NodeType):
    TAG = 'dataBlockTest'


class DecomposeMatrix(NodeType):
    TAG = 'decomposeMatrix'


class DefaultLightList(NodeType):
    TAG = 'defaultLightList'


class DefaultRenderUtilityList(NodeType):
    TAG = 'defaultRenderUtilityList'


class DefaultRenderingList(NodeType):
    TAG = 'defaultRenderingList'


class DefaultShaderList(NodeType):
    TAG = 'defaultShaderList'


class DefaultTextureList(NodeType):
    TAG = 'defaultTextureList'


class DeformBend(NodeType):
    TAG = 'deformBend'


class DeformBendManip(NodeType):
    TAG = 'deformBendManip'


class DeformFlare(NodeType):
    TAG = 'deformFlare'


class DeformFlareManip(NodeType):
    TAG = 'deformFlareManip'


class DeformSine(NodeType):
    TAG = 'deformSine'


class DeformSineManip(NodeType):
    TAG = 'deformSineManip'


class DeformSquash(NodeType):
    TAG = 'deformSquash'


class DeformSquashManip(NodeType):
    TAG = 'deformSquashManip'


class DeformTwist(NodeType):
    TAG = 'deformTwist'


class DeformTwistManip(NodeType):
    TAG = 'deformTwistManip'


class DeformWave(NodeType):
    TAG = 'deformWave'


class DeformWaveManip(NodeType):
    TAG = 'deformWaveManip'


class DeleteColorSet(NodeType):
    TAG = 'deleteColorSet'


class DeleteComponent(NodeType):
    TAG = 'deleteComponent'


class DeleteUVSet(NodeType):
    TAG = 'deleteUVSet'


class DeltaMush(NodeType):
    TAG = 'deltaMush'


class DetachCurve(NodeType):
    TAG = 'detachCurve'


class DetachSurface(NodeType):
    TAG = 'detachSurface'


class DirectedDisc(NodeType):
    TAG = 'directedDisc'


class DirectionManip(NodeType):
    TAG = 'directionManip'


class DirectionalLight(NodeType):
    TAG = 'directionalLight'


class DiscManip(NodeType):
    TAG = 'discManip'


class DiskCache(NodeType):
    TAG = 'diskCache'


class DisplacementShader(NodeType):
    TAG = 'displacementShader'


class DisplayLayer(NodeType):
    TAG = 'displayLayer'


class DisplayLayerManager(NodeType):
    TAG = 'displayLayerManager'


class DistanceBetween(NodeType):
    TAG = 'distanceBetween'


class DistanceDimShape(NodeType):
    TAG = 'distanceDimShape'


class DistanceManip(NodeType):
    TAG = 'distanceManip'


class Dof(NodeType):
    TAG = 'dof'


class DofManip(NodeType):
    TAG = 'dofManip'


class DoubleShadingSwitch(NodeType):
    TAG = 'doubleShadingSwitch'


class DpBirailSrf(NodeType):
    TAG = 'dpBirailSrf'


class DragField(NodeType):
    TAG = 'dragField'


class DropoffLocator(NodeType):
    TAG = 'dropoffLocator'


class DropoffManip(NodeType):
    TAG = 'dropoffManip'


class DynAttenuationManip(NodeType):
    TAG = 'dynAttenuationManip'


class DynController(NodeType):
    TAG = 'dynController'


class DynGlobals(NodeType):
    TAG = 'dynGlobals'


class DynHolder(NodeType):
    TAG = 'dynHolder'


class DynSpreadManip(NodeType):
    TAG = 'dynSpreadManip'


class DynamicConstraint(NodeType):
    TAG = 'dynamicConstraint'


class EditMetadata(NodeType):
    TAG = 'editMetadata'


class EditsManager(NodeType):
    TAG = 'editsManager'


class EmitterManip(NodeType):
    TAG = 'emitterManip'


class EnableManip(NodeType):
    TAG = 'enableManip'


class EnvBall(NodeType):
    TAG = 'envBall'


class EnvChrome(NodeType):
    TAG = 'envChrome'


class EnvCube(NodeType):
    TAG = 'envCube'


class EnvFacade(NodeType):
    TAG = 'envFacade'


class EnvFog(NodeType):
    TAG = 'envFog'


class EnvSky(NodeType):
    TAG = 'envSky'


class EnvSphere(NodeType):
    TAG = 'envSphere'


class EnvironmentFog(NodeType):
    TAG = 'environmentFog'


class EulerToQuat(NodeType):
    TAG = 'eulerToQuat'


class ExplodeNurbsShell(NodeType):
    TAG = 'explodeNurbsShell'


class Expression(NodeType):
    TAG = 'expression'


class ExtendCurve(NodeType):
    TAG = 'extendCurve'


class ExtendCurveDistanceManip(NodeType):
    TAG = 'extendCurveDistanceManip'


class ExtendSurface(NodeType):
    TAG = 'extendSurface'


class ExtendSurfaceDistanceManip(NodeType):
    TAG = 'extendSurfaceDistanceManip'


class Extrude(NodeType):
    TAG = 'extrude'


class ExtrudeManip(NodeType):
    TAG = 'extrudeManip'


class Facade(NodeType):
    TAG = 'facade'


class FfBlendSrf(NodeType):
    TAG = 'ffBlendSrf'


class FfBlendSrfObsolete(NodeType):
    TAG = 'ffBlendSrfObsolete'


class FfFilletSrf(NodeType):
    TAG = 'ffFilletSrf'


class Ffd(NodeType):
    TAG = 'ffd'


class FieldManip(NodeType):
    TAG = 'fieldManip'


class FieldsManip(NodeType):
    TAG = 'fieldsManip'


class File(NodeType):
    TAG = 'file'


class FilletCurve(NodeType):
    TAG = 'filletCurve'


class FilterClosestSample(NodeType):
    TAG = 'filterClosestSample'


class FilterEuler(NodeType):
    TAG = 'filterEuler'


class FilterResample(NodeType):
    TAG = 'filterResample'


class FilterSimplify(NodeType):
    TAG = 'filterSimplify'


class FitBspline(NodeType):
    TAG = 'fitBspline'


class FlexorShape(NodeType):
    TAG = 'flexorShape'


class Flow(NodeType):
    TAG = 'flow'


class FluidEmitter(NodeType):
    TAG = 'fluidEmitter'


class FluidShape(NodeType):
    TAG = 'fluidShape'


class FluidSliceManip(NodeType):
    TAG = 'fluidSliceManip'


class FluidTexture2D(NodeType):
    TAG = 'fluidTexture2D'


class FluidTexture3D(NodeType):
    TAG = 'fluidTexture3D'


class Follicle(NodeType):
    TAG = 'follicle'


class ForceUpdateManip(NodeType):
    TAG = 'forceUpdateManip'


class FosterParent(NodeType):
    TAG = 'fosterParent'


class FourByFourMatrix(NodeType):
    TAG = 'fourByFourMatrix'


class Fractal(NodeType):
    TAG = 'fractal'


class FrameCache(NodeType):
    TAG = 'frameCache'


class FreePointManip(NodeType):
    TAG = 'freePointManip'


class FreePointTriadManip(NodeType):
    TAG = 'freePointTriadManip'


class GameFbxExporter(NodeType):
    TAG = 'gameFbxExporter'


class GammaCorrect(NodeType):
    TAG = 'gammaCorrect'


class GeoConnectable(NodeType):
    TAG = 'geoConnectable'


class GeoConnector(NodeType):
    TAG = 'geoConnector'


class GeomBind(NodeType):
    TAG = 'geomBind'


class GeometryConstraint(NodeType):
    TAG = 'geometryConstraint'


class GeometryFilter(NodeType):
    TAG = 'geometryFilter'


class GeometryOnLineManip(NodeType):
    TAG = 'geometryOnLineManip'


class GeometryVarGroup(NodeType):
    TAG = 'geometryVarGroup'


class GlobalCacheControl(NodeType):
    TAG = 'globalCacheControl'


class GlobalStitch(NodeType):
    TAG = 'globalStitch'


class GpuCache(NodeType):
    TAG = 'gpuCache'


class Granite(NodeType):
    TAG = 'granite'


class GravityField(NodeType):
    TAG = 'gravityField'


class GreasePencilSequence(NodeType):
    TAG = 'greasePencilSequence'


class GreasePlane(NodeType):
    TAG = 'greasePlane'


class GreasePlaneRenderShape(NodeType):
    TAG = 'greasePlaneRenderShape'


class Grid(NodeType):
    TAG = 'grid'


class GroupId(NodeType):
    TAG = 'groupId'


class GroupParts(NodeType):
    TAG = 'groupParts'


class Guide(NodeType):
    TAG = 'guide'


class HairConstraint(NodeType):
    TAG = 'hairConstraint'


class HairSystem(NodeType):
    TAG = 'hairSystem'


class HairTubeShader(NodeType):
    TAG = 'hairTubeShader'


class HardenPoint(NodeType):
    TAG = 'hardenPoint'


class HardwareRenderGlobals(NodeType):
    TAG = 'hardwareRenderGlobals'


class HardwareRenderingGlobals(NodeType):
    TAG = 'hardwareRenderingGlobals'


class HeightField(NodeType):
    TAG = 'heightField'


class HierarchyTestNode1(NodeType):
    TAG = 'hierarchyTestNode1'


class HierarchyTestNode2(NodeType):
    TAG = 'hierarchyTestNode2'


class HierarchyTestNode3(NodeType):
    TAG = 'hierarchyTestNode3'


class HikEffector(NodeType):
    TAG = 'hikEffector'


class HikFKJoint(NodeType):
    TAG = 'hikFKJoint'


class HikFloorContactMarker(NodeType):
    TAG = 'hikFloorContactMarker'


class HikGroundPlane(NodeType):
    TAG = 'hikGroundPlane'


class HikHandle(NodeType):
    TAG = 'hikHandle'


class HikIKEffector(NodeType):
    TAG = 'hikIKEffector'


class HikSolver(NodeType):
    TAG = 'hikSolver'


class HistorySwitch(NodeType):
    TAG = 'historySwitch'


class HoldMatrix(NodeType):
    TAG = 'holdMatrix'


class HsvToRgb(NodeType):
    TAG = 'hsvToRgb'


class HwReflectionMap(NodeType):
    TAG = 'hwReflectionMap'


class HwRenderGlobals(NodeType):
    TAG = 'hwRenderGlobals'


class HyperGraphInfo(NodeType):
    TAG = 'hyperGraphInfo'


class HyperLayout(NodeType):
    TAG = 'hyperLayout'


class HyperView(NodeType):
    TAG = 'hyperView'


class IgBrushManip(NodeType):
    TAG = 'igBrushManip'


class IgmDescription(NodeType):
    TAG = 'igmDescription'


class Ik2Bsolver(NodeType):
    TAG = 'ik2Bsolver'


class IkEffector(NodeType):
    TAG = 'ikEffector'


class IkHandle(NodeType):
    TAG = 'ikHandle'


class IkMCsolver(NodeType):
    TAG = 'ikMCsolver'


class IkPASolver(NodeType):
    TAG = 'ikPASolver'


class IkRPManip(NodeType):
    TAG = 'ikRPManip'


class IkRPsolver(NodeType):
    TAG = 'ikRPsolver'


class IkSCsolver(NodeType):
    TAG = 'ikSCsolver'


class IkSplineManip(NodeType):
    TAG = 'ikSplineManip'


class IkSplineSolver(NodeType):
    TAG = 'ikSplineSolver'


class IkSpringSolver(NodeType):
    TAG = 'ikSpringSolver'


class IkSystem(NodeType):
    TAG = 'ikSystem'


class ImagePlane(NodeType):
    TAG = 'imagePlane'


class ImplicitBox(NodeType):
    TAG = 'implicitBox'


class ImplicitCone(NodeType):
    TAG = 'implicitCone'


class ImplicitSphere(NodeType):
    TAG = 'implicitSphere'


class IndexManip(NodeType):
    TAG = 'indexManip'


class InsertKnotCurve(NodeType):
    TAG = 'insertKnotCurve'


class InsertKnotSurface(NodeType):
    TAG = 'insertKnotSurface'


class Instancer(NodeType):
    TAG = 'instancer'


class IntersectSurface(NodeType):
    TAG = 'intersectSurface'


class InverseMatrix(NodeType):
    TAG = 'inverseMatrix'


class IsoparmManip(NodeType):
    TAG = 'isoparmManip'


class Jiggle(NodeType):
    TAG = 'jiggle'


class Joint(NodeType):
    TAG = 'joint'


class JointCluster(NodeType):
    TAG = 'jointCluster'


class JointClusterManip(NodeType):
    TAG = 'jointClusterManip'


class JointFfd(NodeType):
    TAG = 'jointFfd'


class JointLattice(NodeType):
    TAG = 'jointLattice'


class JointTranslateManip(NodeType):
    TAG = 'jointTranslateManip'


class KeyframeRegionManip(NodeType):
    TAG = 'keyframeRegionManip'


class KeyingGroup(NodeType):
    TAG = 'keyingGroup'


class Lambert(NodeType):
    TAG = 'lambert'


class Lattice(NodeType):
    TAG = 'lattice'


class LayeredShader(NodeType):
    TAG = 'layeredShader'


class LayeredTexture(NodeType):
    TAG = 'layeredTexture'


class LeastSquaresModifier(NodeType):
    TAG = 'leastSquaresModifier'


class Leather(NodeType):
    TAG = 'leather'


class LightFog(NodeType):
    TAG = 'lightFog'


class LightInfo(NodeType):
    TAG = 'lightInfo'


class LightLinker(NodeType):
    TAG = 'lightLinker'


class LightList(NodeType):
    TAG = 'lightList'


class LightManip(NodeType):
    TAG = 'lightManip'


class LimitManip(NodeType):
    TAG = 'limitManip'


class LineManip(NodeType):
    TAG = 'lineManip'


class LineModifier(NodeType):
    TAG = 'lineModifier'


class Locator(NodeType):
    TAG = 'locator'


class LodGroup(NodeType):
    TAG = 'lodGroup'


class LodThresholds(NodeType):
    TAG = 'lodThresholds'


class Loft(NodeType):
    TAG = 'loft'


class LookAt(NodeType):
    TAG = 'lookAt'


class Luminance(NodeType):
    TAG = 'luminance'


class MakeGroup(NodeType):
    TAG = 'makeGroup'


class MakeIllustratorCurves(NodeType):
    TAG = 'makeIllustratorCurves'


class MakeNurbCircle(NodeType):
    TAG = 'makeNurbCircle'


class MakeNurbCone(NodeType):
    TAG = 'makeNurbCone'


class MakeNurbCube(NodeType):
    TAG = 'makeNurbCube'


class MakeNurbCylinder(NodeType):
    TAG = 'makeNurbCylinder'


class MakeNurbPlane(NodeType):
    TAG = 'makeNurbPlane'


class MakeNurbSphere(NodeType):
    TAG = 'makeNurbSphere'


class MakeNurbTorus(NodeType):
    TAG = 'makeNurbTorus'


class MakeNurbsSquare(NodeType):
    TAG = 'makeNurbsSquare'


class MakeTextCurves(NodeType):
    TAG = 'makeTextCurves'


class MakeThreePointCircularArc(NodeType):
    TAG = 'makeThreePointCircularArc'


class MakeThreePointCircularArcManip(NodeType):
    TAG = 'makeThreePointCircularArcManip'


class MakeTwoPointCircularArc(NodeType):
    TAG = 'makeTwoPointCircularArc'


class MakeTwoPointCircularArcManip(NodeType):
    TAG = 'makeTwoPointCircularArcManip'


class Mandelbrot(NodeType):
    TAG = 'mandelbrot'


class Mandelbrot3D(NodeType):
    TAG = 'mandelbrot3D'


class Manip2DContainer(NodeType):
    TAG = 'manip2DContainer'


class ManipContainer(NodeType):
    TAG = 'manipContainer'


class Marble(NodeType):
    TAG = 'marble'


class MarkerManip(NodeType):
    TAG = 'markerManip'


class MaterialFacade(NodeType):
    TAG = 'materialFacade'


class MaterialInfo(NodeType):
    TAG = 'materialInfo'


class Membrane(NodeType):
    TAG = 'membrane'


class MentalrayTexture(NodeType):
    TAG = 'mentalrayTexture'


class Mesh(NodeType):
    TAG = 'mesh'


class MeshVarGroup(NodeType):
    TAG = 'meshVarGroup'


class MotionPath(NodeType):
    TAG = 'motionPath'


class MotionPathManip(NodeType):
    TAG = 'motionPathManip'


class MotionTrail(NodeType):
    TAG = 'motionTrail'


class MotionTrailShape(NodeType):
    TAG = 'motionTrailShape'


class Mountain(NodeType):
    TAG = 'mountain'


class MoveBezierHandleManip(NodeType):
    TAG = 'moveBezierHandleManip'


class MoveVertexManip(NodeType):
    TAG = 'moveVertexManip'


class Movie(NodeType):
    TAG = 'movie'


class MpBirailSrf(NodeType):
    TAG = 'mpBirailSrf'


class MultDoubleLinear(NodeType):
    TAG = 'multDoubleLinear'


class MultMatrix(NodeType):
    TAG = 'multMatrix'


class MultilisterLight(NodeType):
    TAG = 'multilisterLight'


class MultiplyDivide(NodeType):
    TAG = 'multiplyDivide'


class Mute(NodeType):
    TAG = 'mute'


class NCloth(NodeType):
    TAG = 'nCloth'


class NComponent(NodeType):
    TAG = 'nComponent'


class NParticle(NodeType):
    TAG = 'nParticle'


class NRigid(NodeType):
    TAG = 'nRigid'


class NearestPointOnCurve(NodeType):
    TAG = 'nearestPointOnCurve'


class Network(NodeType):
    TAG = 'network'


class NewtonField(NodeType):
    TAG = 'newtonField'


class NewtonManip(NodeType):
    TAG = 'newtonManip'


class NexManip(NodeType):
    TAG = 'nexManip'


class NodeGraphEditorBookmarkInfo(NodeType):
    TAG = 'nodeGraphEditorBookmarkInfo'


class NodeGraphEditorBookmarks(NodeType):
    TAG = 'nodeGraphEditorBookmarks'


class NodeGraphEditorInfo(NodeType):
    TAG = 'nodeGraphEditorInfo'


class Noise(NodeType):
    TAG = 'noise'


class NonLinear(NodeType):
    TAG = 'nonLinear'


class NormalConstraint(NodeType):
    TAG = 'normalConstraint'


class Nucleus(NodeType):
    TAG = 'nucleus'


class NurbsCurve(NodeType):
    TAG = 'nurbsCurve'


class NurbsCurveToBezier(NodeType):
    TAG = 'nurbsCurveToBezier'


class NurbsSurface(NodeType):
    TAG = 'nurbsSurface'


class NurbsTessellate(NodeType):
    TAG = 'nurbsTessellate'


class NurbsToSubdiv(NodeType):
    TAG = 'nurbsToSubdiv'


class NurbsToSubdivProc(NodeType):
    TAG = 'nurbsToSubdivProc'


class ObjectAttrFilter(NodeType):
    TAG = 'objectAttrFilter'


class ObjectBinFilter(NodeType):
    TAG = 'objectBinFilter'


class ObjectFilter(NodeType):
    TAG = 'objectFilter'


class ObjectMultiFilter(NodeType):
    TAG = 'objectMultiFilter'


class ObjectNameFilter(NodeType):
    TAG = 'objectNameFilter'


class ObjectRenderFilter(NodeType):
    TAG = 'objectRenderFilter'


class ObjectScriptFilter(NodeType):
    TAG = 'objectScriptFilter'


class ObjectSet(NodeType):
    TAG = 'objectSet'


class ObjectTypeFilter(NodeType):
    TAG = 'objectTypeFilter'


class Ocean(NodeType):
    TAG = 'ocean'


class OceanShader(NodeType):
    TAG = 'oceanShader'


class OffsetCos(NodeType):
    TAG = 'offsetCos'


class OffsetCosManip(NodeType):
    TAG = 'offsetCosManip'


class OffsetCurve(NodeType):
    TAG = 'offsetCurve'


class OffsetCurveManip(NodeType):
    TAG = 'offsetCurveManip'


class OffsetSurface(NodeType):
    TAG = 'offsetSurface'


class OffsetSurfaceManip(NodeType):
    TAG = 'offsetSurfaceManip'


class OldBlindDataBase(NodeType):
    TAG = 'oldBlindDataBase'


class OldGeometryConstraint(NodeType):
    TAG = 'oldGeometryConstraint'


class OldNormalConstraint(NodeType):
    TAG = 'oldNormalConstraint'


class OldTangentConstraint(NodeType):
    TAG = 'oldTangentConstraint'


class OpticalFX(NodeType):
    TAG = 'opticalFX'


class OrientConstraint(NodeType):
    TAG = 'orientConstraint'


class OrientationMarker(NodeType):
    TAG = 'orientationMarker'


class PairBlend(NodeType):
    TAG = 'pairBlend'


class ParamDimension(NodeType):
    TAG = 'paramDimension'


class ParentConstraint(NodeType):
    TAG = 'parentConstraint'


class Particle(NodeType):
    TAG = 'particle'


class ParticleAgeMapper(NodeType):
    TAG = 'particleAgeMapper'


class ParticleCloud(NodeType):
    TAG = 'particleCloud'


class ParticleColorMapper(NodeType):
    TAG = 'particleColorMapper'


class ParticleIncandMapper(NodeType):
    TAG = 'particleIncandMapper'


class ParticleSamplerInfo(NodeType):
    TAG = 'particleSamplerInfo'


class ParticleTranspMapper(NodeType):
    TAG = 'particleTranspMapper'


class Partition(NodeType):
    TAG = 'partition'


class PassContributionMap(NodeType):
    TAG = 'passContributionMap'


class PassMatrix(NodeType):
    TAG = 'passMatrix'


class PfxHair(NodeType):
    TAG = 'pfxHair'


class PfxToon(NodeType):
    TAG = 'pfxToon'


class Phong(NodeType):
    TAG = 'phong'


class PhongE(NodeType):
    TAG = 'phongE'


class Pivot2dManip(NodeType):
    TAG = 'pivot2dManip'


class PivotAndOrientManip(NodeType):
    TAG = 'pivotAndOrientManip'


class Place2dTexture(NodeType):
    TAG = 'place2dTexture'


class Place3dTexture(NodeType):
    TAG = 'place3dTexture'


class PlanarProjManip(NodeType):
    TAG = 'planarProjManip'


class PlanarTrimSurface(NodeType):
    TAG = 'planarTrimSurface'


class PlusMinusAverage(NodeType):
    TAG = 'plusMinusAverage'


class PointConstraint(NodeType):
    TAG = 'pointConstraint'


class PointEmitter(NodeType):
    TAG = 'pointEmitter'


class PointLight(NodeType):
    TAG = 'pointLight'


class PointMatrixMult(NodeType):
    TAG = 'pointMatrixMult'


class PointOnCurveInfo(NodeType):
    TAG = 'pointOnCurveInfo'


class PointOnCurveManip(NodeType):
    TAG = 'pointOnCurveManip'


class PointOnLineManip(NodeType):
    TAG = 'pointOnLineManip'


class PointOnPolyConstraint(NodeType):
    TAG = 'pointOnPolyConstraint'


class PointOnSurfManip(NodeType):
    TAG = 'pointOnSurfManip'


class PointOnSurfaceInfo(NodeType):
    TAG = 'pointOnSurfaceInfo'


class PointOnSurfaceManip(NodeType):
    TAG = 'pointOnSurfaceManip'


class PoleVectorConstraint(NodeType):
    TAG = 'poleVectorConstraint'


class PolyAppend(NodeType):
    TAG = 'polyAppend'


class PolyAppendVertex(NodeType):
    TAG = 'polyAppendVertex'


class PolyAutoProj(NodeType):
    TAG = 'polyAutoProj'


class PolyAutoProjManip(NodeType):
    TAG = 'polyAutoProjManip'


class PolyAverageVertex(NodeType):
    TAG = 'polyAverageVertex'


class PolyBevel(NodeType):
    TAG = 'polyBevel'


class PolyBevel2(NodeType):
    TAG = 'polyBevel2'


class PolyBevel3(NodeType):
    TAG = 'polyBevel3'


class PolyBlindData(NodeType):
    TAG = 'polyBlindData'


class PolyBoolOp(NodeType):
    TAG = 'polyBoolOp'


class PolyBridgeEdge(NodeType):
    TAG = 'polyBridgeEdge'


class PolyCBoolOp(NodeType):
    TAG = 'polyCBoolOp'


class PolyCaddyManip(NodeType):
    TAG = 'polyCaddyManip'


class PolyChipOff(NodeType):
    TAG = 'polyChipOff'


class PolyCloseBorder(NodeType):
    TAG = 'polyCloseBorder'


class PolyCollapseEdge(NodeType):
    TAG = 'polyCollapseEdge'


class PolyCollapseF(NodeType):
    TAG = 'polyCollapseF'


class PolyColorDel(NodeType):
    TAG = 'polyColorDel'


class PolyColorMod(NodeType):
    TAG = 'polyColorMod'


class PolyColorPerVertex(NodeType):
    TAG = 'polyColorPerVertex'


class PolyCone(NodeType):
    TAG = 'polyCone'


class PolyConnectComponents(NodeType):
    TAG = 'polyConnectComponents'


class PolyContourProj(NodeType):
    TAG = 'polyContourProj'


class PolyCopyUV(NodeType):
    TAG = 'polyCopyUV'


class PolyCrease(NodeType):
    TAG = 'polyCrease'


class PolyCreaseEdge(NodeType):
    TAG = 'polyCreaseEdge'


class PolyCreateFace(NodeType):
    TAG = 'polyCreateFace'


class PolyCreateToolManip(NodeType):
    TAG = 'polyCreateToolManip'


class PolyCube(NodeType):
    TAG = 'polyCube'


class PolyCut(NodeType):
    TAG = 'polyCut'


class PolyCutManip(NodeType):
    TAG = 'polyCutManip'


class PolyCutManipContainer(NodeType):
    TAG = 'polyCutManipContainer'


class PolyCylProj(NodeType):
    TAG = 'polyCylProj'


class PolyCylinder(NodeType):
    TAG = 'polyCylinder'


class PolyDelEdge(NodeType):
    TAG = 'polyDelEdge'


class PolyDelFacet(NodeType):
    TAG = 'polyDelFacet'


class PolyDelVertex(NodeType):
    TAG = 'polyDelVertex'


class PolyDuplicateEdge(NodeType):
    TAG = 'polyDuplicateEdge'


class PolyEdgeToCurve(NodeType):
    TAG = 'polyEdgeToCurve'


class PolyEditEdgeFlow(NodeType):
    TAG = 'polyEditEdgeFlow'


class PolyExtrudeEdge(NodeType):
    TAG = 'polyExtrudeEdge'


class PolyExtrudeFace(NodeType):
    TAG = 'polyExtrudeFace'


class PolyExtrudeVertex(NodeType):
    TAG = 'polyExtrudeVertex'


class PolyFlipEdge(NodeType):
    TAG = 'polyFlipEdge'


class PolyFlipUV(NodeType):
    TAG = 'polyFlipUV'


class PolyHelix(NodeType):
    TAG = 'polyHelix'


class PolyHoleFace(NodeType):
    TAG = 'polyHoleFace'


class PolyLayoutUV(NodeType):
    TAG = 'polyLayoutUV'


class PolyMapCut(NodeType):
    TAG = 'polyMapCut'


class PolyMapDel(NodeType):
    TAG = 'polyMapDel'


class PolyMapSew(NodeType):
    TAG = 'polyMapSew'


class PolyMapSewMove(NodeType):
    TAG = 'polyMapSewMove'


class PolyMappingManip(NodeType):
    TAG = 'polyMappingManip'


class PolyMergeEdge(NodeType):
    TAG = 'polyMergeEdge'


class PolyMergeFace(NodeType):
    TAG = 'polyMergeFace'


class PolyMergeUV(NodeType):
    TAG = 'polyMergeUV'


class PolyMergeVert(NodeType):
    TAG = 'polyMergeVert'


class PolyMergeVertsManip(NodeType):
    TAG = 'polyMergeVertsManip'


class PolyMirror(NodeType):
    TAG = 'polyMirror'


class PolyModifierManip(NodeType):
    TAG = 'polyModifierManip'


class PolyModifierManipContainer(NodeType):
    TAG = 'polyModifierManipContainer'


class PolyMoveEdge(NodeType):
    TAG = 'polyMoveEdge'


class PolyMoveFace(NodeType):
    TAG = 'polyMoveFace'


class PolyMoveFacetUV(NodeType):
    TAG = 'polyMoveFacetUV'


class PolyMoveUV(NodeType):
    TAG = 'polyMoveUV'


class PolyMoveUVManip(NodeType):
    TAG = 'polyMoveUVManip'


class PolyMoveVertex(NodeType):
    TAG = 'polyMoveVertex'


class PolyMoveVertexManip(NodeType):
    TAG = 'polyMoveVertexManip'


class PolyNormal(NodeType):
    TAG = 'polyNormal'


class PolyNormalPerVertex(NodeType):
    TAG = 'polyNormalPerVertex'


class PolyNormalizeUV(NodeType):
    TAG = 'polyNormalizeUV'


class PolyOptUvs(NodeType):
    TAG = 'polyOptUvs'


class PolyPassThru(NodeType):
    TAG = 'polyPassThru'


class PolyPinUV(NodeType):
    TAG = 'polyPinUV'


class PolyPipe(NodeType):
    TAG = 'polyPipe'


class PolyPlanarProj(NodeType):
    TAG = 'polyPlanarProj'


class PolyPlane(NodeType):
    TAG = 'polyPlane'


class PolyPlatonicSolid(NodeType):
    TAG = 'polyPlatonicSolid'


class PolyPoke(NodeType):
    TAG = 'polyPoke'


class PolyPokeManip(NodeType):
    TAG = 'polyPokeManip'


class PolyPrimitiveMisc(NodeType):
    TAG = 'polyPrimitiveMisc'


class PolyPrism(NodeType):
    TAG = 'polyPrism'


class PolyProj(NodeType):
    TAG = 'polyProj'


class PolyProjManip(NodeType):
    TAG = 'polyProjManip'


class PolyProjectCurve(NodeType):
    TAG = 'polyProjectCurve'


class PolyPyramid(NodeType):
    TAG = 'polyPyramid'


class PolyQuad(NodeType):
    TAG = 'polyQuad'


class PolyReduce(NodeType):
    TAG = 'polyReduce'


class PolyRemesh(NodeType):
    TAG = 'polyRemesh'


class PolySelectEditFeedbackManip(NodeType):
    TAG = 'polySelectEditFeedbackManip'


class PolySeparate(NodeType):
    TAG = 'polySeparate'


class PolySewEdge(NodeType):
    TAG = 'polySewEdge'


class PolySmooth(NodeType):
    TAG = 'polySmooth'


class PolySmoothFace(NodeType):
    TAG = 'polySmoothFace'


class PolySmoothProxy(NodeType):
    TAG = 'polySmoothProxy'


class PolySoftEdge(NodeType):
    TAG = 'polySoftEdge'


class PolySphProj(NodeType):
    TAG = 'polySphProj'


class PolySphere(NodeType):
    TAG = 'polySphere'


class PolySpinEdge(NodeType):
    TAG = 'polySpinEdge'


class PolySplit(NodeType):
    TAG = 'polySplit'


class PolySplitEdge(NodeType):
    TAG = 'polySplitEdge'


class PolySplitRing(NodeType):
    TAG = 'polySplitRing'


class PolySplitToolManip1(NodeType):
    TAG = 'polySplitToolManip1'


class PolySplitVert(NodeType):
    TAG = 'polySplitVert'


class PolyStraightenUVBorder(NodeType):
    TAG = 'polyStraightenUVBorder'


class PolySubdEdge(NodeType):
    TAG = 'polySubdEdge'


class PolySubdFace(NodeType):
    TAG = 'polySubdFace'


class PolyToSubdiv(NodeType):
    TAG = 'polyToSubdiv'


class PolyToolFeedbackManip(NodeType):
    TAG = 'polyToolFeedbackManip'


class PolyTorus(NodeType):
    TAG = 'polyTorus'


class PolyTransfer(NodeType):
    TAG = 'polyTransfer'


class PolyTriangulate(NodeType):
    TAG = 'polyTriangulate'


class PolyTweak(NodeType):
    TAG = 'polyTweak'


class PolyTweakUV(NodeType):
    TAG = 'polyTweakUV'


class PolyUVRectangle(NodeType):
    TAG = 'polyUVRectangle'


class PolyUnite(NodeType):
    TAG = 'polyUnite'


class PolyVertexNormalManip(NodeType):
    TAG = 'polyVertexNormalManip'


class PolyWedgeFace(NodeType):
    TAG = 'polyWedgeFace'


class PositionMarker(NodeType):
    TAG = 'positionMarker'


class PostProcessList(NodeType):
    TAG = 'postProcessList'


class PrecompExport(NodeType):
    TAG = 'precompExport'


class ProjectCurve(NodeType):
    TAG = 'projectCurve'


class ProjectTangent(NodeType):
    TAG = 'projectTangent'


class ProjectTangentManip(NodeType):
    TAG = 'projectTangentManip'


class Projection(NodeType):
    TAG = 'projection'


class ProjectionManip(NodeType):
    TAG = 'projectionManip'


class ProjectionMultiManip(NodeType):
    TAG = 'projectionMultiManip'


class ProjectionUVManip(NodeType):
    TAG = 'projectionUVManip'


class PropModManip(NodeType):
    TAG = 'propModManip'


class PropMoveTriadManip(NodeType):
    TAG = 'propMoveTriadManip'


class ProxyManager(NodeType):
    TAG = 'proxyManager'


class PsdFileTex(NodeType):
    TAG = 'psdFileTex'


class QuadPtOnLineManip(NodeType):
    TAG = 'quadPtOnLineManip'


class QuadShadingSwitch(NodeType):
    TAG = 'quadShadingSwitch'


class QuatAdd(NodeType):
    TAG = 'quatAdd'


class QuatConjugate(NodeType):
    TAG = 'quatConjugate'


class QuatInvert(NodeType):
    TAG = 'quatInvert'


class QuatNegate(NodeType):
    TAG = 'quatNegate'


class QuatNormalize(NodeType):
    TAG = 'quatNormalize'


class QuatProd(NodeType):
    TAG = 'quatProd'


class QuatSub(NodeType):
    TAG = 'quatSub'


class QuatToEuler(NodeType):
    TAG = 'quatToEuler'


class RadialField(NodeType):
    TAG = 'radialField'


class Ramp(NodeType):
    TAG = 'ramp'


class RampShader(NodeType):
    TAG = 'rampShader'


class RbfSrf(NodeType):
    TAG = 'rbfSrf'


class RbfSrfManip(NodeType):
    TAG = 'rbfSrfManip'


class RebuildCurve(NodeType):
    TAG = 'rebuildCurve'


class RebuildSurface(NodeType):
    TAG = 'rebuildSurface'


class Record(NodeType):
    TAG = 'record'


class Reference(NodeType):
    TAG = 'reference'


class RemapColor(NodeType):
    TAG = 'remapColor'


class RemapHsv(NodeType):
    TAG = 'remapHsv'


class RemapValue(NodeType):
    TAG = 'remapValue'


class RenderBox(NodeType):
    TAG = 'renderBox'


class RenderCone(NodeType):
    TAG = 'renderCone'


class RenderGlobals(NodeType):
    TAG = 'renderGlobals'


class RenderGlobalsList(NodeType):
    TAG = 'renderGlobalsList'


class RenderLayer(NodeType):
    TAG = 'renderLayer'


class RenderLayerManager(NodeType):
    TAG = 'renderLayerManager'


class RenderPass(NodeType):
    TAG = 'renderPass'


class RenderPassSet(NodeType):
    TAG = 'renderPassSet'


class RenderQuality(NodeType):
    TAG = 'renderQuality'


class RenderRect(NodeType):
    TAG = 'renderRect'


class RenderSphere(NodeType):
    TAG = 'renderSphere'


class RenderTarget(NodeType):
    TAG = 'renderTarget'


class RenderedImageSource(NodeType):
    TAG = 'renderedImageSource'


class Resolution(NodeType):
    TAG = 'resolution'


class ResultCurveTimeToAngular(NodeType):
    TAG = 'resultCurveTimeToAngular'


class ResultCurveTimeToLinear(NodeType):
    TAG = 'resultCurveTimeToLinear'


class ResultCurveTimeToTime(NodeType):
    TAG = 'resultCurveTimeToTime'


class ResultCurveTimeToUnitless(NodeType):
    TAG = 'resultCurveTimeToUnitless'


class Reverse(NodeType):
    TAG = 'reverse'


class ReverseCurve(NodeType):
    TAG = 'reverseCurve'


class ReverseCurveManip(NodeType):
    TAG = 'reverseCurveManip'


class ReverseSurface(NodeType):
    TAG = 'reverseSurface'


class ReverseSurfaceManip(NodeType):
    TAG = 'reverseSurfaceManip'


class Revolve(NodeType):
    TAG = 'revolve'


class RevolveManip(NodeType):
    TAG = 'revolveManip'


class RevolvedPrimitiveManip(NodeType):
    TAG = 'revolvedPrimitiveManip'


class RgbToHsv(NodeType):
    TAG = 'rgbToHsv'


class RigidBody(NodeType):
    TAG = 'rigidBody'


class RigidConstraint(NodeType):
    TAG = 'rigidConstraint'


class RigidSolver(NodeType):
    TAG = 'rigidSolver'


class Rock(NodeType):
    TAG = 'rock'


class RotateHelper(NodeType):
    TAG = 'rotateHelper'


class RotateLimitsManip(NodeType):
    TAG = 'rotateLimitsManip'


class RotateManip(NodeType):
    TAG = 'rotateManip'


class RotateUV2dManip(NodeType):
    TAG = 'rotateUV2dManip'


class RoundConstantRadius(NodeType):
    TAG = 'roundConstantRadius'


class RoundConstantRadiusManip(NodeType):
    TAG = 'roundConstantRadiusManip'


class RoundRadiusCrvManip(NodeType):
    TAG = 'roundRadiusCrvManip'


class RoundRadiusManip(NodeType):
    TAG = 'roundRadiusManip'


class Sampler(NodeType):
    TAG = 'sampler'


class SamplerInfo(NodeType):
    TAG = 'samplerInfo'


class ScaleConstraint(NodeType):
    TAG = 'scaleConstraint'


class ScaleLimitsManip(NodeType):
    TAG = 'scaleLimitsManip'


class ScaleManip(NodeType):
    TAG = 'scaleManip'


class ScaleUV2dManip(NodeType):
    TAG = 'scaleUV2dManip'


class ScreenAlignedCircleManip(NodeType):
    TAG = 'screenAlignedCircleManip'


class Script(NodeType):
    TAG = 'script'


class ScriptManip(NodeType):
    TAG = 'scriptManip'


class Sculpt(NodeType):
    TAG = 'sculpt'


class SelectionListOperator(NodeType):
    TAG = 'selectionListOperator'


class SequenceManager(NodeType):
    TAG = 'sequenceManager'


class Sequencer(NodeType):
    TAG = 'sequencer'


class SetRange(NodeType):
    TAG = 'setRange'


class ShaderGlow(NodeType):
    TAG = 'shaderGlow'


class ShadingEngine(NodeType):
    TAG = 'shadingEngine'


class ShadingMap(NodeType):
    TAG = 'shadingMap'


class ShellTessellate(NodeType):
    TAG = 'shellTessellate'


class Shot(NodeType):
    TAG = 'shot'


class ShrinkWrap(NodeType):
    TAG = 'shrinkWrap'


class SimpleTestNode(NodeType):
    TAG = 'simpleTestNode'


class SimpleVolumeShader(NodeType):
    TAG = 'simpleVolumeShader'


class SingleShadingSwitch(NodeType):
    TAG = 'singleShadingSwitch'


class SketchPlane(NodeType):
    TAG = 'sketchPlane'


class SkinBinding(NodeType):
    TAG = 'skinBinding'


class SkinCluster(NodeType):
    TAG = 'skinCluster'


class Smear(NodeType):
    TAG = 'smear'


class SmoothCurve(NodeType):
    TAG = 'smoothCurve'


class SmoothTangentSrf(NodeType):
    TAG = 'smoothTangentSrf'


class SnapUV2dManip(NodeType):
    TAG = 'snapUV2dManip'


class Snapshot(NodeType):
    TAG = 'snapshot'


class SnapshotShape(NodeType):
    TAG = 'snapshotShape'


class Snow(NodeType):
    TAG = 'snow'


class SoftMod(NodeType):
    TAG = 'softMod'


class SoftModHandle(NodeType):
    TAG = 'softModHandle'


class SoftModManip(NodeType):
    TAG = 'softModManip'


class SolidFractal(NodeType):
    TAG = 'solidFractal'


class SpBirailSrf(NodeType):
    TAG = 'spBirailSrf'


class SphericalProjManip(NodeType):
    TAG = 'sphericalProjManip'


class SpotCylinderManip(NodeType):
    TAG = 'spotCylinderManip'


class SpotLight(NodeType):
    TAG = 'spotLight'


class SpotManip(NodeType):
    TAG = 'spotManip'


class Spring(NodeType):
    TAG = 'spring'


class SquareSrf(NodeType):
    TAG = 'squareSrf'


class SquareSrfManip(NodeType):
    TAG = 'squareSrfManip'


class Stencil(NodeType):
    TAG = 'stencil'


class StereoRigCamera(NodeType):
    TAG = 'stereoRigCamera'


class StitchAsNurbsShell(NodeType):
    TAG = 'stitchAsNurbsShell'


class StitchSrf(NodeType):
    TAG = 'stitchSrf'


class StitchSrfManip(NodeType):
    TAG = 'stitchSrfManip'


class Stroke(NodeType):
    TAG = 'stroke'


class StrokeGlobals(NodeType):
    TAG = 'strokeGlobals'


class Stucco(NodeType):
    TAG = 'stucco'


class StudioClearCoat(NodeType):
    TAG = 'studioClearCoat'


class StyleCurve(NodeType):
    TAG = 'styleCurve'


class SubCurve(NodeType):
    TAG = 'subCurve'


class SubSurface(NodeType):
    TAG = 'subSurface'


class SubdAddTopology(NodeType):
    TAG = 'subdAddTopology'


class SubdAutoProj(NodeType):
    TAG = 'subdAutoProj'


class SubdBlindData(NodeType):
    TAG = 'subdBlindData'


class SubdCleanTopology(NodeType):
    TAG = 'subdCleanTopology'


class SubdHierBlind(NodeType):
    TAG = 'subdHierBlind'


class SubdLayoutUV(NodeType):
    TAG = 'subdLayoutUV'


class SubdMapCut(NodeType):
    TAG = 'subdMapCut'


class SubdMapSewMove(NodeType):
    TAG = 'subdMapSewMove'


class SubdMappingManip(NodeType):
    TAG = 'subdMappingManip'


class SubdPlanarProj(NodeType):
    TAG = 'subdPlanarProj'


class SubdProjManip(NodeType):
    TAG = 'subdProjManip'


class SubdTweak(NodeType):
    TAG = 'subdTweak'


class SubdTweakUV(NodeType):
    TAG = 'subdTweakUV'


class Subdiv(NodeType):
    TAG = 'subdiv'


class SubdivCollapse(NodeType):
    TAG = 'subdivCollapse'


class SubdivComponentId(NodeType):
    TAG = 'subdivComponentId'


class SubdivReverseFaces(NodeType):
    TAG = 'subdivReverseFaces'


class SubdivSurfaceVarGroup(NodeType):
    TAG = 'subdivSurfaceVarGroup'


class SubdivToNurbs(NodeType):
    TAG = 'subdivToNurbs'


class SubdivToPoly(NodeType):
    TAG = 'subdivToPoly'


class Substance(NodeType):
    TAG = 'substance'


class SubstanceOutput(NodeType):
    TAG = 'substanceOutput'


class SurfaceEdManip(NodeType):
    TAG = 'surfaceEdManip'


class SurfaceInfo(NodeType):
    TAG = 'surfaceInfo'


class SurfaceLuminance(NodeType):
    TAG = 'surfaceLuminance'


class SurfaceShader(NodeType):
    TAG = 'surfaceShader'


class SurfaceVarGroup(NodeType):
    TAG = 'surfaceVarGroup'


class SymmetryConstraint(NodeType):
    TAG = 'symmetryConstraint'


class TangentConstraint(NodeType):
    TAG = 'tangentConstraint'


class TexLattice(NodeType):
    TAG = 'texLattice'


class TexLatticeDeformManip(NodeType):
    TAG = 'texLatticeDeformManip'


class TexMoveShellManip(NodeType):
    TAG = 'texMoveShellManip'


class TexSmoothManip(NodeType):
    TAG = 'texSmoothManip'


class TexSmudgeUVManip(NodeType):
    TAG = 'texSmudgeUVManip'


class TextButtonManip(NodeType):
    TAG = 'textButtonManip'


class TextManip2D(NodeType):
    TAG = 'textManip2D'


class Texture3dManip(NodeType):
    TAG = 'texture3dManip'


class TextureBakeSet(NodeType):
    TAG = 'textureBakeSet'


class TextureDeformer(NodeType):
    TAG = 'textureDeformer'


class TextureDeformerHandle(NodeType):
    TAG = 'textureDeformerHandle'


class TextureToGeom(NodeType):
    TAG = 'textureToGeom'


class Time(NodeType):
    TAG = 'time'


class TimeFunction(NodeType):
    TAG = 'timeFunction'


class TimeToUnitConversion(NodeType):
    TAG = 'timeToUnitConversion'


class TimeWarp(NodeType):
    TAG = 'timeWarp'


class ToggleManip(NodeType):
    TAG = 'toggleManip'


class ToggleOnLineManip(NodeType):
    TAG = 'toggleOnLineManip'


class ToolDrawManip(NodeType):
    TAG = 'toolDrawManip'


class ToolDrawManip2D(NodeType):
    TAG = 'toolDrawManip2D'


class ToonLineAttributes(NodeType):
    TAG = 'toonLineAttributes'


class TowPointOnCurveManip(NodeType):
    TAG = 'towPointOnCurveManip'


class TowPointOnSurfaceManip(NodeType):
    TAG = 'towPointOnSurfaceManip'


class TrackInfoManager(NodeType):
    TAG = 'trackInfoManager'


class Trans2dManip(NodeType):
    TAG = 'trans2dManip'


class TransUV2dManip(NodeType):
    TAG = 'transUV2dManip'


class TransferAttributes(NodeType):
    TAG = 'transferAttributes'


class Transform(NodeType):
    TAG = 'transform'


class TransformGeometry(NodeType):
    TAG = 'transformGeometry'


class TranslateLimitsManip(NodeType):
    TAG = 'translateLimitsManip'


class TranslateManip(NodeType):
    TAG = 'translateManip'


class TranslateUVManip(NodeType):
    TAG = 'translateUVManip'


class TransposeMatrix(NodeType):
    TAG = 'transposeMatrix'


class Trim(NodeType):
    TAG = 'trim'


class TrimManip(NodeType):
    TAG = 'trimManip'


class TrimWithBoundaries(NodeType):
    TAG = 'trimWithBoundaries'


class TriplanarProjManip(NodeType):
    TAG = 'triplanarProjManip'


class TripleShadingSwitch(NodeType):
    TAG = 'tripleShadingSwitch'


class TrsInsertManip(NodeType):
    TAG = 'trsInsertManip'


class TrsManip(NodeType):
    TAG = 'trsManip'


class TurbulenceField(NodeType):
    TAG = 'turbulenceField'


class TurbulenceManip(NodeType):
    TAG = 'turbulenceManip'


class Tweak(NodeType):
    TAG = 'tweak'


class UniformField(NodeType):
    TAG = 'uniformField'


class UnitConversion(NodeType):
    TAG = 'unitConversion'


class UnitToTimeConversion(NodeType):
    TAG = 'unitToTimeConversion'


class Unknown(NodeType):
    TAG = 'unknown'


class UnknownDag(NodeType):
    TAG = 'unknownDag'


class UnknownTransform(NodeType):
    TAG = 'unknownTransform'


class Untrim(NodeType):
    TAG = 'untrim'


class UseBackground(NodeType):
    TAG = 'useBackground'


class Uv2dManip(NodeType):
    TAG = 'uv2dManip'


class UvChooser(NodeType):
    TAG = 'uvChooser'


class VectorProduct(NodeType):
    TAG = 'vectorProduct'


class VectorRenderGlobals(NodeType):
    TAG = 'vectorRenderGlobals'


class VertexBakeSet(NodeType):
    TAG = 'vertexBakeSet'


class ViewColorManager(NodeType):
    TAG = 'viewColorManager'


class VolumeAxisField(NodeType):
    TAG = 'volumeAxisField'


class VolumeBindManip(NodeType):
    TAG = 'volumeBindManip'


class VolumeFog(NodeType):
    TAG = 'volumeFog'


class VolumeLight(NodeType):
    TAG = 'volumeLight'


class VolumeNoise(NodeType):
    TAG = 'volumeNoise'


class VolumeShader(NodeType):
    TAG = 'volumeShader'


class VortexField(NodeType):
    TAG = 'vortexField'


class Water(NodeType):
    TAG = 'water'


class WeightGeometryFilter(NodeType):
    TAG = 'weightGeometryFilter'


class Wire(NodeType):
    TAG = 'wire'


class Wood(NodeType):
    TAG = 'wood'


class Wrap(NodeType):
    TAG = 'wrap'


class WriteToColorBuffer(NodeType):
    TAG = 'writeToColorBuffer'


class WriteToDepthBuffer(NodeType):
    TAG = 'writeToDepthBuffer'


class WriteToLabelBuffer(NodeType):
    TAG = 'writeToLabelBuffer'


class WriteToVectorBuffer(NodeType):
    TAG = 'writeToVectorBuffer'


class WtAddMatrix(NodeType):
    TAG = 'wtAddMatrix'


class XformManip(NodeType):
    TAG = 'xformManip'


class XgmArchiveGuide(NodeType):
    TAG = 'xgmArchiveGuide'


class XgmCardGuide(NodeType):
    TAG = 'xgmCardGuide'


class XgmConnectivity(NodeType):
    TAG = 'xgmConnectivity'


class XgmDescription(NodeType):
    TAG = 'xgmDescription'


class XgmGuide(NodeType):
    TAG = 'xgmGuide'


class XgmGuideManip(NodeType):
    TAG = 'xgmGuideManip'


class XgmGuideSculptManip(NodeType):
    TAG = 'xgmGuideSculptManip'


class XgmMakeGuide(NodeType):
    TAG = 'xgmMakeGuide'


class XgmNurbsPatch(NodeType):
    TAG = 'xgmNurbsPatch'


class XgmPalette(NodeType):
    TAG = 'xgmPalette'


class XgmPatch(NodeType):
    TAG = 'xgmPatch'


class XgmPointsManip(NodeType):
    TAG = 'xgmPointsManip'


class XgmPointsViewer(NodeType):
    TAG = 'xgmPointsViewer'


class XgmSphereGuide(NodeType):
    TAG = 'xgmSphereGuide'


class XgmSplineGuide(NodeType):
    TAG = 'xgmSplineGuide'


class XgmSubdPatch(NodeType):
    TAG = 'xgmSubdPatch'
