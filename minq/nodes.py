'''
This module contains LSByType filters for all of the node classes in Maya 2015.  Early or later versions may have
slightly different node type lists. It's useful if you use an autocompleting IDE - otherwise it's only a convenience
to avoid typing 'of_type'
'''

from .ls import LSByType


class abstractBaseCreate(LSByType):
    TYPE = 'abstractBaseCreate'

class abstractBaseNurbsConversion(LSByType):
    TYPE = 'abstractBaseNurbsConversion'

class adskAssetInstanceNode_TdependNode(LSByType):
    TYPE = 'adskAssetInstanceNode_TdependNode'

class adskAssetInstanceNode_TdnTx2D(LSByType):
    TYPE = 'adskAssetInstanceNode_TdnTx2D'

class adskAssetInstanceNode_TlightShape(LSByType):
    TYPE = 'adskAssetInstanceNode_TlightShape'

class animBlendNodeBase(LSByType):
    TYPE = 'animBlendNodeBase'

class animCurve(LSByType):
    TYPE = 'animCurve'

class assembly(LSByType):
    TYPE = 'assembly'

class bakeSet(LSByType):
    TYPE = 'bakeSet'

class baseGeometryVarGroup(LSByType):
    TYPE = 'baseGeometryVarGroup'

class baseShadingSwitch(LSByType):
    TYPE = 'baseShadingSwitch'

class birailSrf(LSByType):
    TYPE = 'birailSrf'

class blend(LSByType):
    TYPE = 'blend'

class boundaryBase(LSByType):
    TYPE = 'boundaryBase'

class cacheBase(LSByType):
    TYPE = 'cacheBase'

class clientDevice(LSByType):
    TYPE = 'clientDevice'

class constraint(LSByType):
    TYPE = 'constraint'

class controlPoint(LSByType):
    TYPE = 'controlPoint'

class cteInterpolator(LSByType):
    TYPE = 'cteInterpolator'

class curveFromMesh(LSByType):
    TYPE = 'curveFromMesh'

class curveFromSubdiv(LSByType):
    TYPE = 'curveFromSubdiv'

class curveFromSurface(LSByType):
    TYPE = 'curveFromSurface'

class curveNormalizer(LSByType):
    TYPE = 'curveNormalizer'

class curveRange(LSByType):
    TYPE = 'curveRange'

class curveShape(LSByType):
    TYPE = 'curveShape'

class dagNode(LSByType):
    TYPE = 'dagNode'

class deformFunc(LSByType):
    TYPE = 'deformFunc'

class deformableShape(LSByType):
    TYPE = 'deformableShape'

class dimensionShape(LSByType):
    TYPE = 'dimensionShape'

class dynBase(LSByType):
    TYPE = 'dynBase'

class entity(LSByType):
    TYPE = 'entity'

class field(LSByType):
    TYPE = 'field'

class filter(LSByType):
    TYPE = 'filter'

class geometryShape(LSByType):
    TYPE = 'geometryShape'

class groundPlane(LSByType):
    TYPE = 'groundPlane'

class hwShader(LSByType):
    TYPE = 'hwShader'

class ikSolver(LSByType):
    TYPE = 'ikSolver'

class imageSource(LSByType):
    TYPE = 'imageSource'

class light(LSByType):
    TYPE = 'light'

class makeCircularArc(LSByType):
    TYPE = 'makeCircularArc'

class manip2D(LSByType):
    TYPE = 'manip2D'

class manip3D(LSByType):
    TYPE = 'manip3D'

class nBase(LSByType):
    TYPE = 'nBase'

class node(LSByType):
    TYPE = 'node'

class nonAmbientLightShapeNode(LSByType):
    TYPE = 'nonAmbientLightShapeNode'

class nonExtendedLightShapeNode(LSByType):
    TYPE = 'nonExtendedLightShapeNode'

class nurbsDimShape(LSByType):
    TYPE = 'nurbsDimShape'

class orthoGrid(LSByType):
    TYPE = 'orthoGrid'

class parentTessellate(LSByType):
    TYPE = 'parentTessellate'

class pfxGeometry(LSByType):
    TYPE = 'pfxGeometry'

class plane(LSByType):
    TYPE = 'plane'

class polyBase(LSByType):
    TYPE = 'polyBase'

class polyCreator(LSByType):
    TYPE = 'polyCreator'

class polyModifier(LSByType):
    TYPE = 'polyModifier'

class polyModifierUV(LSByType):
    TYPE = 'polyModifierUV'

class polyModifierWorld(LSByType):
    TYPE = 'polyModifierWorld'

class polyPrimitive(LSByType):
    TYPE = 'polyPrimitive'

class primitive(LSByType):
    TYPE = 'primitive'

class reflect(LSByType):
    TYPE = 'reflect'

class renderLight(LSByType):
    TYPE = 'renderLight'

class resultCurve(LSByType):
    TYPE = 'resultCurve'

class revolvedPrimitive(LSByType):
    TYPE = 'revolvedPrimitive'

class shadingDependNode(LSByType):
    TYPE = 'shadingDependNode'

class shape(LSByType):
    TYPE = 'shape'

class subdBase(LSByType):
    TYPE = 'subdBase'

class subdModifier(LSByType):
    TYPE = 'subdModifier'

class subdModifierUV(LSByType):
    TYPE = 'subdModifierUV'

class subdModifierWorld(LSByType):
    TYPE = 'subdModifierWorld'

class surfaceShape(LSByType):
    TYPE = 'surfaceShape'

class texBaseDeformManip(LSByType):
    TYPE = 'texBaseDeformManip'

class texture2d(LSByType):
    TYPE = 'texture2d'

class texture3d(LSByType):
    TYPE = 'texture3d'

class textureEnv(LSByType):
    TYPE = 'textureEnv'

class threadedDevice(LSByType):
    TYPE = 'threadedDevice'

class writeToFrameBuffer(LSByType):
    TYPE = 'writeToFrameBuffer'


class AISEnvFacade(LSByType):
    TYPE = 'AISEnvFacade'


class AlembicNode(LSByType):
    TYPE = 'AlembicNode'


class ComputeGlobal(LSByType):
    TYPE = 'ComputeGlobal'


class ComputeLocal(LSByType):
    TYPE = 'ComputeLocal'


class CustomRigDefaultMappingNode(LSByType):
    TYPE = 'CustomRigDefaultMappingNode'


class CustomRigRetargeterNode(LSByType):
    TYPE = 'CustomRigRetargeterNode'


class HIKCharacterNode(LSByType):
    TYPE = 'HIKCharacterNode'


class HIKCharacterStateClient(LSByType):
    TYPE = 'HIKCharacterStateClient'


class HIKControlSetNode(LSByType):
    TYPE = 'HIKControlSetNode'


class HIKEffector2State(LSByType):
    TYPE = 'HIKEffector2State'


class HIKEffectorFromCharacter(LSByType):
    TYPE = 'HIKEffectorFromCharacter'


class HIKFK2State(LSByType):
    TYPE = 'HIKFK2State'


class HIKPinning2State(LSByType):
    TYPE = 'HIKPinning2State'


class HIKProperty2State(LSByType):
    TYPE = 'HIKProperty2State'


class HIKRetargeterNode(LSByType):
    TYPE = 'HIKRetargeterNode'


class HIKSK2State(LSByType):
    TYPE = 'HIKSK2State'


class HIKSkeletonGeneratorNode(LSByType):
    TYPE = 'HIKSkeletonGeneratorNode'


class HIKSolverNode(LSByType):
    TYPE = 'HIKSolverNode'


class HIKState2Effector(LSByType):
    TYPE = 'HIKState2Effector'


class HIKState2FK(LSByType):
    TYPE = 'HIKState2FK'


class HIKState2GlobalSK(LSByType):
    TYPE = 'HIKState2GlobalSK'


class HIKState2SK(LSByType):
    TYPE = 'HIKState2SK'


class ShaderfxShader(LSByType):
    TYPE = 'ShaderfxShader'


class StingrayPBS(LSByType):
    TYPE = 'StingrayPBS'


class Unfold3DOptimize(LSByType):
    TYPE = 'Unfold3DOptimize'


class Unfold3DUnfold(LSByType):
    TYPE = 'Unfold3DUnfold'


class aboutToSetValueTestNode(LSByType):
    TYPE = 'aboutToSetValueTestNode'


class addDoubleLinear(LSByType):
    TYPE = 'addDoubleLinear'


class addMatrix(LSByType):
    TYPE = 'addMatrix'


class adskMaterial(LSByType):
    TYPE = 'adskMaterial'


class adskPrepareRenderGlobals(LSByType):
    TYPE = 'adskPrepareRenderGlobals'


class aimConstraint(LSByType):
    TYPE = 'aimConstraint'


class airField(LSByType):
    TYPE = 'airField'


class airManip(LSByType):
    TYPE = 'airManip'


class alignCurve(LSByType):
    TYPE = 'alignCurve'


class alignManip(LSByType):
    TYPE = 'alignManip'


class alignSurface(LSByType):
    TYPE = 'alignSurface'


class ambientLight(LSByType):
    TYPE = 'ambientLight'


class angleBetween(LSByType):
    TYPE = 'angleBetween'


class angleDimension(LSByType):
    TYPE = 'angleDimension'


class animBlend(LSByType):
    TYPE = 'animBlend'


class animBlendInOut(LSByType):
    TYPE = 'animBlendInOut'


class animBlendNodeAdditive(LSByType):
    TYPE = 'animBlendNodeAdditive'


class animBlendNodeAdditiveDA(LSByType):
    TYPE = 'animBlendNodeAdditiveDA'


class animBlendNodeAdditiveDL(LSByType):
    TYPE = 'animBlendNodeAdditiveDL'


class animBlendNodeAdditiveF(LSByType):
    TYPE = 'animBlendNodeAdditiveF'


class animBlendNodeAdditiveFA(LSByType):
    TYPE = 'animBlendNodeAdditiveFA'


class animBlendNodeAdditiveFL(LSByType):
    TYPE = 'animBlendNodeAdditiveFL'


class animBlendNodeAdditiveI16(LSByType):
    TYPE = 'animBlendNodeAdditiveI16'


class animBlendNodeAdditiveI32(LSByType):
    TYPE = 'animBlendNodeAdditiveI32'


class animBlendNodeAdditiveRotation(LSByType):
    TYPE = 'animBlendNodeAdditiveRotation'


class animBlendNodeAdditiveScale(LSByType):
    TYPE = 'animBlendNodeAdditiveScale'


class animBlendNodeBoolean(LSByType):
    TYPE = 'animBlendNodeBoolean'


class animBlendNodeEnum(LSByType):
    TYPE = 'animBlendNodeEnum'


class animBlendNodeTime(LSByType):
    TYPE = 'animBlendNodeTime'


class animClip(LSByType):
    TYPE = 'animClip'


class animCurveTA(LSByType):
    TYPE = 'animCurveTA'


class animCurveTL(LSByType):
    TYPE = 'animCurveTL'


class animCurveTT(LSByType):
    TYPE = 'animCurveTT'


class animCurveTU(LSByType):
    TYPE = 'animCurveTU'


class animCurveUA(LSByType):
    TYPE = 'animCurveUA'


class animCurveUL(LSByType):
    TYPE = 'animCurveUL'


class animCurveUT(LSByType):
    TYPE = 'animCurveUT'


class animCurveUU(LSByType):
    TYPE = 'animCurveUU'


class animLayer(LSByType):
    TYPE = 'animLayer'


class animLayerClip(LSByType):
    TYPE = 'animLayerClip'


class animLayerClipContainer(LSByType):
    TYPE = 'animLayerClipContainer'


class animLayerClipRoster(LSByType):
    TYPE = 'animLayerClipRoster'


class animLayerClipRotation(LSByType):
    TYPE = 'animLayerClipRotation'


class animLayerClipSingle(LSByType):
    TYPE = 'animLayerClipSingle'


class animLayerClipTRS(LSByType):
    TYPE = 'animLayerClipTRS'


class anisotropic(LSByType):
    TYPE = 'anisotropic'


class annotationShape(LSByType):
    TYPE = 'annotationShape'


class apfEntityNode(LSByType):
    TYPE = 'apfEntityNode'


class apfFileNode(LSByType):
    TYPE = 'apfFileNode'


class arcLengthDimension(LSByType):
    TYPE = 'arcLengthDimension'


class areaLight(LSByType):
    TYPE = 'areaLight'


class arrayMapper(LSByType):
    TYPE = 'arrayMapper'


class arrowManip(LSByType):
    TYPE = 'arrowManip'


class assemblyDefinition(LSByType):
    TYPE = 'assemblyDefinition'


class assemblyReference(LSByType):
    TYPE = 'assemblyReference'


class attachCurve(LSByType):
    TYPE = 'attachCurve'


class attachSurface(LSByType):
    TYPE = 'attachSurface'


class attrHierarchyTest(LSByType):
    TYPE = 'attrHierarchyTest'


class audio(LSByType):
    TYPE = 'audio'


class avgCurves(LSByType):
    TYPE = 'avgCurves'


class avgCurvesManip(LSByType):
    TYPE = 'avgCurvesManip'


class avgNurbsSurfacePoints(LSByType):
    TYPE = 'avgNurbsSurfacePoints'


class avgSurfacePoints(LSByType):
    TYPE = 'avgSurfacePoints'


class axesActionManip(LSByType):
    TYPE = 'axesActionManip'


class ballProjManip(LSByType):
    TYPE = 'ballProjManip'


class barnDoorManip(LSByType):
    TYPE = 'barnDoorManip'


class baseLattice(LSByType):
    TYPE = 'baseLattice'


class bevel(LSByType):
    TYPE = 'bevel'


class bevelManip(LSByType):
    TYPE = 'bevelManip'


class bevelPlus(LSByType):
    TYPE = 'bevelPlus'


class bezierCurve(LSByType):
    TYPE = 'bezierCurve'


class bezierCurveToNurbs(LSByType):
    TYPE = 'bezierCurveToNurbs'


class bifrostAeroMaterial(LSByType):
    TYPE = 'bifrostAeroMaterial'


class bifrostAttrNotifier(LSByType):
    TYPE = 'bifrostAttrNotifier'


class bifrostContainer(LSByType):
    TYPE = 'bifrostContainer'


class bifrostFoamMaterial(LSByType):
    TYPE = 'bifrostFoamMaterial'


class bifrostLiquidMaterial(LSByType):
    TYPE = 'bifrostLiquidMaterial'


class bifrostShape(LSByType):
    TYPE = 'bifrostShape'


class blendColorSets(LSByType):
    TYPE = 'blendColorSets'


class blendColors(LSByType):
    TYPE = 'blendColors'


class blendDevice(LSByType):
    TYPE = 'blendDevice'


class blendManip(LSByType):
    TYPE = 'blendManip'


class blendShape(LSByType):
    TYPE = 'blendShape'


class blendTwoAttr(LSByType):
    TYPE = 'blendTwoAttr'


class blendWeighted(LSByType):
    TYPE = 'blendWeighted'


class blindDataTemplate(LSByType):
    TYPE = 'blindDataTemplate'


class blinn(LSByType):
    TYPE = 'blinn'


class boneLattice(LSByType):
    TYPE = 'boneLattice'


class boolean(LSByType):
    TYPE = 'boolean'


class boundary(LSByType):
    TYPE = 'boundary'


class brownian(LSByType):
    TYPE = 'brownian'


class brush(LSByType):
    TYPE = 'brush'


class bulge(LSByType):
    TYPE = 'bulge'


class bump2d(LSByType):
    TYPE = 'bump2d'


class bump3d(LSByType):
    TYPE = 'bump3d'


class buttonManip(LSByType):
    TYPE = 'buttonManip'


class cMuscleCreator(LSByType):
    TYPE = 'cMuscleCreator'


class cMuscleDebug(LSByType):
    TYPE = 'cMuscleDebug'


class cMuscleDirection(LSByType):
    TYPE = 'cMuscleDirection'


class cMuscleDisplace(LSByType):
    TYPE = 'cMuscleDisplace'


class cMuscleDisplay(LSByType):
    TYPE = 'cMuscleDisplay'


class cMuscleFalloff(LSByType):
    TYPE = 'cMuscleFalloff'


class cMuscleKeepOut(LSByType):
    TYPE = 'cMuscleKeepOut'


class cMuscleMultiCollide(LSByType):
    TYPE = 'cMuscleMultiCollide'


class cMuscleObject(LSByType):
    TYPE = 'cMuscleObject'


class cMuscleRelative(LSByType):
    TYPE = 'cMuscleRelative'


class cMuscleShader(LSByType):
    TYPE = 'cMuscleShader'


class cMuscleSmartCollide(LSByType):
    TYPE = 'cMuscleSmartCollide'


class cMuscleSmartConstraint(LSByType):
    TYPE = 'cMuscleSmartConstraint'


class cMuscleSpline(LSByType):
    TYPE = 'cMuscleSpline'


class cMuscleSplineDeformer(LSByType):
    TYPE = 'cMuscleSplineDeformer'


class cMuscleStretch(LSByType):
    TYPE = 'cMuscleStretch'


class cMuscleSurfAttach(LSByType):
    TYPE = 'cMuscleSurfAttach'


class cMuscleSystem(LSByType):
    TYPE = 'cMuscleSystem'


class cacheBlend(LSByType):
    TYPE = 'cacheBlend'


class cacheFile(LSByType):
    TYPE = 'cacheFile'


class caddyManip(LSByType):
    TYPE = 'caddyManip'


class caddyManipBase(LSByType):
    TYPE = 'caddyManipBase'


class camera(LSByType):
    TYPE = 'camera'


class cameraManip(LSByType):
    TYPE = 'cameraManip'


class cameraPlaneManip(LSByType):
    TYPE = 'cameraPlaneManip'


class cameraSet(LSByType):
    TYPE = 'cameraSet'


class cameraView(LSByType):
    TYPE = 'cameraView'


class centerManip(LSByType):
    TYPE = 'centerManip'


class character(LSByType):
    TYPE = 'character'


class characterMap(LSByType):
    TYPE = 'characterMap'


class characterOffset(LSByType):
    TYPE = 'characterOffset'


class checker(LSByType):
    TYPE = 'checker'


class choice(LSByType):
    TYPE = 'choice'


class chooser(LSByType):
    TYPE = 'chooser'


class circleManip(LSByType):
    TYPE = 'circleManip'


class circleSweepManip(LSByType):
    TYPE = 'circleSweepManip'


class clamp(LSByType):
    TYPE = 'clamp'


class clipGhostShape(LSByType):
    TYPE = 'clipGhostShape'


class clipLibrary(LSByType):
    TYPE = 'clipLibrary'


class clipScheduler(LSByType):
    TYPE = 'clipScheduler'


class clipToGhostData(LSByType):
    TYPE = 'clipToGhostData'


class closeCurve(LSByType):
    TYPE = 'closeCurve'


class closeSurface(LSByType):
    TYPE = 'closeSurface'


class closestPointOnMesh(LSByType):
    TYPE = 'closestPointOnMesh'


class closestPointOnSurface(LSByType):
    TYPE = 'closestPointOnSurface'


class cloth(LSByType):
    TYPE = 'cloth'


class cloud(LSByType):
    TYPE = 'cloud'


class cluster(LSByType):
    TYPE = 'cluster'


class clusterFlexorShape(LSByType):
    TYPE = 'clusterFlexorShape'


class clusterHandle(LSByType):
    TYPE = 'clusterHandle'


class coiManip(LSByType):
    TYPE = 'coiManip'


class collisionModel(LSByType):
    TYPE = 'collisionModel'


class colorManagementGlobals(LSByType):
    TYPE = 'colorManagementGlobals'


class colorProfile(LSByType):
    TYPE = 'colorProfile'


class compactPlugArrayTest(LSByType):
    TYPE = 'compactPlugArrayTest'


class componentManip(LSByType):
    TYPE = 'componentManip'


class composeMatrix(LSByType):
    TYPE = 'composeMatrix'


class concentricProjManip(LSByType):
    TYPE = 'concentricProjManip'


class condition(LSByType):
    TYPE = 'condition'


class container(LSByType):
    TYPE = 'container'


class containerBase(LSByType):
    TYPE = 'containerBase'


class contourProjManip(LSByType):
    TYPE = 'contourProjManip'


class contrast(LSByType):
    TYPE = 'contrast'


class controller(LSByType):
    TYPE = 'controller'


class copyColorSet(LSByType):
    TYPE = 'copyColorSet'


class copyUVSet(LSByType):
    TYPE = 'copyUVSet'


class cpManip(LSByType):
    TYPE = 'cpManip'


class crater(LSByType):
    TYPE = 'crater'


class creaseSet(LSByType):
    TYPE = 'creaseSet'


class createBPManip(LSByType):
    TYPE = 'createBPManip'


class createCVManip(LSByType):
    TYPE = 'createCVManip'


class createColorSet(LSByType):
    TYPE = 'createColorSet'


class createEPManip(LSByType):
    TYPE = 'createEPManip'


class createPtexUV(LSByType):
    TYPE = 'createPtexUV'


class createUVSet(LSByType):
    TYPE = 'createUVSet'


class cte(LSByType):
    TYPE = 'cte'


class cteAnimSource(LSByType):
    TYPE = 'cteAnimSource'


class cteCurveVisualizer(LSByType):
    TYPE = 'cteCurveVisualizer'


class cteInterpolatorRotation(LSByType):
    TYPE = 'cteInterpolatorRotation'


class cteInterpolatorSingle(LSByType):
    TYPE = 'cteInterpolatorSingle'


class cteInterpolatorTRS(LSByType):
    TYPE = 'cteInterpolatorTRS'


class cteRoster(LSByType):
    TYPE = 'cteRoster'


class cteTracks(LSByType):
    TYPE = 'cteTracks'


class cubeManip(LSByType):
    TYPE = 'cubeManip'


class cubicProjManip(LSByType):
    TYPE = 'cubicProjManip'


class curveEdManip(LSByType):
    TYPE = 'curveEdManip'


class curveFromMeshCoM(LSByType):
    TYPE = 'curveFromMeshCoM'


class curveFromMeshEdge(LSByType):
    TYPE = 'curveFromMeshEdge'


class curveFromSubdivEdge(LSByType):
    TYPE = 'curveFromSubdivEdge'


class curveFromSubdivFace(LSByType):
    TYPE = 'curveFromSubdivFace'


class curveFromSurfaceBnd(LSByType):
    TYPE = 'curveFromSurfaceBnd'


class curveFromSurfaceCoS(LSByType):
    TYPE = 'curveFromSurfaceCoS'


class curveFromSurfaceIso(LSByType):
    TYPE = 'curveFromSurfaceIso'


class curveInfo(LSByType):
    TYPE = 'curveInfo'


class curveIntersect(LSByType):
    TYPE = 'curveIntersect'


class curveNormalizerAngle(LSByType):
    TYPE = 'curveNormalizerAngle'


class curveNormalizerLinear(LSByType):
    TYPE = 'curveNormalizerLinear'


class curveSegmentManip(LSByType):
    TYPE = 'curveSegmentManip'


class curveVarGroup(LSByType):
    TYPE = 'curveVarGroup'


class cylindricalProjManip(LSByType):
    TYPE = 'cylindricalProjManip'


class dagContainer(LSByType):
    TYPE = 'dagContainer'


class dagPose(LSByType):
    TYPE = 'dagPose'


class dataBlockTest(LSByType):
    TYPE = 'dataBlockTest'


class decomposeMatrix(LSByType):
    TYPE = 'decomposeMatrix'


class defaultLightList(LSByType):
    TYPE = 'defaultLightList'


class defaultRenderUtilityList(LSByType):
    TYPE = 'defaultRenderUtilityList'


class defaultRenderingList(LSByType):
    TYPE = 'defaultRenderingList'


class defaultShaderList(LSByType):
    TYPE = 'defaultShaderList'


class defaultTextureList(LSByType):
    TYPE = 'defaultTextureList'


class deformBend(LSByType):
    TYPE = 'deformBend'


class deformBendManip(LSByType):
    TYPE = 'deformBendManip'


class deformFlare(LSByType):
    TYPE = 'deformFlare'


class deformFlareManip(LSByType):
    TYPE = 'deformFlareManip'


class deformSine(LSByType):
    TYPE = 'deformSine'


class deformSineManip(LSByType):
    TYPE = 'deformSineManip'


class deformSquash(LSByType):
    TYPE = 'deformSquash'


class deformSquashManip(LSByType):
    TYPE = 'deformSquashManip'


class deformTwist(LSByType):
    TYPE = 'deformTwist'


class deformTwistManip(LSByType):
    TYPE = 'deformTwistManip'


class deformWave(LSByType):
    TYPE = 'deformWave'


class deformWaveManip(LSByType):
    TYPE = 'deformWaveManip'


class deleteColorSet(LSByType):
    TYPE = 'deleteColorSet'


class deleteComponent(LSByType):
    TYPE = 'deleteComponent'


class deleteUVSet(LSByType):
    TYPE = 'deleteUVSet'


class deltaMush(LSByType):
    TYPE = 'deltaMush'


class detachCurve(LSByType):
    TYPE = 'detachCurve'


class detachSurface(LSByType):
    TYPE = 'detachSurface'


class directedDisc(LSByType):
    TYPE = 'directedDisc'


class directionManip(LSByType):
    TYPE = 'directionManip'


class directionalLight(LSByType):
    TYPE = 'directionalLight'


class discManip(LSByType):
    TYPE = 'discManip'


class diskCache(LSByType):
    TYPE = 'diskCache'


class displacementShader(LSByType):
    TYPE = 'displacementShader'


class displayLayer(LSByType):
    TYPE = 'displayLayer'


class displayLayerManager(LSByType):
    TYPE = 'displayLayerManager'


class distanceBetween(LSByType):
    TYPE = 'distanceBetween'


class distanceDimShape(LSByType):
    TYPE = 'distanceDimShape'


class distanceManip(LSByType):
    TYPE = 'distanceManip'


class dof(LSByType):
    TYPE = 'dof'


class dofManip(LSByType):
    TYPE = 'dofManip'


class doubleShadingSwitch(LSByType):
    TYPE = 'doubleShadingSwitch'


class dpBirailSrf(LSByType):
    TYPE = 'dpBirailSrf'


class dragField(LSByType):
    TYPE = 'dragField'


class dropoffLocator(LSByType):
    TYPE = 'dropoffLocator'


class dropoffManip(LSByType):
    TYPE = 'dropoffManip'


class dynAttenuationManip(LSByType):
    TYPE = 'dynAttenuationManip'


class dynController(LSByType):
    TYPE = 'dynController'


class dynGlobals(LSByType):
    TYPE = 'dynGlobals'


class dynHolder(LSByType):
    TYPE = 'dynHolder'


class dynSpreadManip(LSByType):
    TYPE = 'dynSpreadManip'


class dynamicConstraint(LSByType):
    TYPE = 'dynamicConstraint'


class editMetadata(LSByType):
    TYPE = 'editMetadata'


class editsManager(LSByType):
    TYPE = 'editsManager'


class emitterManip(LSByType):
    TYPE = 'emitterManip'


class enableManip(LSByType):
    TYPE = 'enableManip'


class envBall(LSByType):
    TYPE = 'envBall'


class envChrome(LSByType):
    TYPE = 'envChrome'


class envCube(LSByType):
    TYPE = 'envCube'


class envFacade(LSByType):
    TYPE = 'envFacade'


class envFog(LSByType):
    TYPE = 'envFog'


class envSky(LSByType):
    TYPE = 'envSky'


class envSphere(LSByType):
    TYPE = 'envSphere'


class environmentFog(LSByType):
    TYPE = 'environmentFog'


class eulerToQuat(LSByType):
    TYPE = 'eulerToQuat'


class explodeNurbsShell(LSByType):
    TYPE = 'explodeNurbsShell'


class expression(LSByType):
    TYPE = 'expression'


class extendCurve(LSByType):
    TYPE = 'extendCurve'


class extendCurveDistanceManip(LSByType):
    TYPE = 'extendCurveDistanceManip'


class extendSurface(LSByType):
    TYPE = 'extendSurface'


class extendSurfaceDistanceManip(LSByType):
    TYPE = 'extendSurfaceDistanceManip'


class extrude(LSByType):
    TYPE = 'extrude'


class extrudeManip(LSByType):
    TYPE = 'extrudeManip'


class facade(LSByType):
    TYPE = 'facade'


class ffBlendSrf(LSByType):
    TYPE = 'ffBlendSrf'


class ffBlendSrfObsolete(LSByType):
    TYPE = 'ffBlendSrfObsolete'


class ffFilletSrf(LSByType):
    TYPE = 'ffFilletSrf'


class ffd(LSByType):
    TYPE = 'ffd'


class fieldManip(LSByType):
    TYPE = 'fieldManip'


class fieldsManip(LSByType):
    TYPE = 'fieldsManip'


class file(LSByType):
    TYPE = 'file'


class filletCurve(LSByType):
    TYPE = 'filletCurve'


class filterClosestSample(LSByType):
    TYPE = 'filterClosestSample'


class filterEuler(LSByType):
    TYPE = 'filterEuler'


class filterResample(LSByType):
    TYPE = 'filterResample'


class filterSimplify(LSByType):
    TYPE = 'filterSimplify'


class fitBspline(LSByType):
    TYPE = 'fitBspline'


class flexorShape(LSByType):
    TYPE = 'flexorShape'


class flow(LSByType):
    TYPE = 'flow'


class fluidEmitter(LSByType):
    TYPE = 'fluidEmitter'


class fluidShape(LSByType):
    TYPE = 'fluidShape'


class fluidSliceManip(LSByType):
    TYPE = 'fluidSliceManip'


class fluidTexture2D(LSByType):
    TYPE = 'fluidTexture2D'


class fluidTexture3D(LSByType):
    TYPE = 'fluidTexture3D'


class follicle(LSByType):
    TYPE = 'follicle'


class forceUpdateManip(LSByType):
    TYPE = 'forceUpdateManip'


class fosterParent(LSByType):
    TYPE = 'fosterParent'


class fourByFourMatrix(LSByType):
    TYPE = 'fourByFourMatrix'


class fractal(LSByType):
    TYPE = 'fractal'


class frameCache(LSByType):
    TYPE = 'frameCache'


class freePointManip(LSByType):
    TYPE = 'freePointManip'


class freePointTriadManip(LSByType):
    TYPE = 'freePointTriadManip'


class gameFbxExporter(LSByType):
    TYPE = 'gameFbxExporter'


class gammaCorrect(LSByType):
    TYPE = 'gammaCorrect'


class geoConnectable(LSByType):
    TYPE = 'geoConnectable'


class geoConnector(LSByType):
    TYPE = 'geoConnector'


class geomBind(LSByType):
    TYPE = 'geomBind'


class geometryConstraint(LSByType):
    TYPE = 'geometryConstraint'


class geometryFilter(LSByType):
    TYPE = 'geometryFilter'


class geometryOnLineManip(LSByType):
    TYPE = 'geometryOnLineManip'


class geometryVarGroup(LSByType):
    TYPE = 'geometryVarGroup'


class globalCacheControl(LSByType):
    TYPE = 'globalCacheControl'


class globalStitch(LSByType):
    TYPE = 'globalStitch'


class gpuCache(LSByType):
    TYPE = 'gpuCache'


class granite(LSByType):
    TYPE = 'granite'


class gravityField(LSByType):
    TYPE = 'gravityField'


class greasePencilSequence(LSByType):
    TYPE = 'greasePencilSequence'


class greasePlane(LSByType):
    TYPE = 'greasePlane'


class greasePlaneRenderShape(LSByType):
    TYPE = 'greasePlaneRenderShape'


class grid(LSByType):
    TYPE = 'grid'


class groupId(LSByType):
    TYPE = 'groupId'


class groupParts(LSByType):
    TYPE = 'groupParts'


class guide(LSByType):
    TYPE = 'guide'


class hairConstraint(LSByType):
    TYPE = 'hairConstraint'


class hairSystem(LSByType):
    TYPE = 'hairSystem'


class hairTubeShader(LSByType):
    TYPE = 'hairTubeShader'


class hardenPoint(LSByType):
    TYPE = 'hardenPoint'


class hardwareRenderGlobals(LSByType):
    TYPE = 'hardwareRenderGlobals'


class hardwareRenderingGlobals(LSByType):
    TYPE = 'hardwareRenderingGlobals'


class heightField(LSByType):
    TYPE = 'heightField'


class hierarchyTestNode1(LSByType):
    TYPE = 'hierarchyTestNode1'


class hierarchyTestNode2(LSByType):
    TYPE = 'hierarchyTestNode2'


class hierarchyTestNode3(LSByType):
    TYPE = 'hierarchyTestNode3'


class hikEffector(LSByType):
    TYPE = 'hikEffector'


class hikFKJoint(LSByType):
    TYPE = 'hikFKJoint'


class hikFloorContactMarker(LSByType):
    TYPE = 'hikFloorContactMarker'


class hikGroundPlane(LSByType):
    TYPE = 'hikGroundPlane'


class hikHandle(LSByType):
    TYPE = 'hikHandle'


class hikIKEffector(LSByType):
    TYPE = 'hikIKEffector'


class hikSolver(LSByType):
    TYPE = 'hikSolver'


class historySwitch(LSByType):
    TYPE = 'historySwitch'


class holdMatrix(LSByType):
    TYPE = 'holdMatrix'


class hsvToRgb(LSByType):
    TYPE = 'hsvToRgb'


class hwReflectionMap(LSByType):
    TYPE = 'hwReflectionMap'


class hwRenderGlobals(LSByType):
    TYPE = 'hwRenderGlobals'


class hyperGraphInfo(LSByType):
    TYPE = 'hyperGraphInfo'


class hyperLayout(LSByType):
    TYPE = 'hyperLayout'


class hyperView(LSByType):
    TYPE = 'hyperView'


class igBrushManip(LSByType):
    TYPE = 'igBrushManip'


class igmDescription(LSByType):
    TYPE = 'igmDescription'


class ik2Bsolver(LSByType):
    TYPE = 'ik2Bsolver'


class ikEffector(LSByType):
    TYPE = 'ikEffector'


class ikHandle(LSByType):
    TYPE = 'ikHandle'


class ikMCsolver(LSByType):
    TYPE = 'ikMCsolver'


class ikPASolver(LSByType):
    TYPE = 'ikPASolver'


class ikRPManip(LSByType):
    TYPE = 'ikRPManip'


class ikRPsolver(LSByType):
    TYPE = 'ikRPsolver'


class ikSCsolver(LSByType):
    TYPE = 'ikSCsolver'


class ikSplineManip(LSByType):
    TYPE = 'ikSplineManip'


class ikSplineSolver(LSByType):
    TYPE = 'ikSplineSolver'


class ikSpringSolver(LSByType):
    TYPE = 'ikSpringSolver'


class ikSystem(LSByType):
    TYPE = 'ikSystem'


class imagePlane(LSByType):
    TYPE = 'imagePlane'


class implicitBox(LSByType):
    TYPE = 'implicitBox'


class implicitCone(LSByType):
    TYPE = 'implicitCone'


class implicitSphere(LSByType):
    TYPE = 'implicitSphere'


class indexManip(LSByType):
    TYPE = 'indexManip'


class insertKnotCurve(LSByType):
    TYPE = 'insertKnotCurve'


class insertKnotSurface(LSByType):
    TYPE = 'insertKnotSurface'


class instancer(LSByType):
    TYPE = 'instancer'


class intersectSurface(LSByType):
    TYPE = 'intersectSurface'


class inverseMatrix(LSByType):
    TYPE = 'inverseMatrix'


class isoparmManip(LSByType):
    TYPE = 'isoparmManip'


class jiggle(LSByType):
    TYPE = 'jiggle'


class joint(LSByType):
    TYPE = 'joint'


class jointCluster(LSByType):
    TYPE = 'jointCluster'


class jointClusterManip(LSByType):
    TYPE = 'jointClusterManip'


class jointFfd(LSByType):
    TYPE = 'jointFfd'


class jointLattice(LSByType):
    TYPE = 'jointLattice'


class jointTranslateManip(LSByType):
    TYPE = 'jointTranslateManip'


class keyframeRegionManip(LSByType):
    TYPE = 'keyframeRegionManip'


class keyingGroup(LSByType):
    TYPE = 'keyingGroup'


class lambert(LSByType):
    TYPE = 'lambert'


class lattice(LSByType):
    TYPE = 'lattice'


class layeredShader(LSByType):
    TYPE = 'layeredShader'


class layeredTexture(LSByType):
    TYPE = 'layeredTexture'


class leastSquaresModifier(LSByType):
    TYPE = 'leastSquaresModifier'


class leather(LSByType):
    TYPE = 'leather'


class lightFog(LSByType):
    TYPE = 'lightFog'


class lightInfo(LSByType):
    TYPE = 'lightInfo'


class lightLinker(LSByType):
    TYPE = 'lightLinker'


class lightList(LSByType):
    TYPE = 'lightList'


class lightManip(LSByType):
    TYPE = 'lightManip'


class limitManip(LSByType):
    TYPE = 'limitManip'


class lineManip(LSByType):
    TYPE = 'lineManip'


class lineModifier(LSByType):
    TYPE = 'lineModifier'


class locator(LSByType):
    TYPE = 'locator'


class lodGroup(LSByType):
    TYPE = 'lodGroup'


class lodThresholds(LSByType):
    TYPE = 'lodThresholds'


class loft(LSByType):
    TYPE = 'loft'


class lookAt(LSByType):
    TYPE = 'lookAt'


class luminance(LSByType):
    TYPE = 'luminance'


class makeGroup(LSByType):
    TYPE = 'makeGroup'


class makeIllustratorCurves(LSByType):
    TYPE = 'makeIllustratorCurves'


class makeNurbCircle(LSByType):
    TYPE = 'makeNurbCircle'


class makeNurbCone(LSByType):
    TYPE = 'makeNurbCone'


class makeNurbCube(LSByType):
    TYPE = 'makeNurbCube'


class makeNurbCylinder(LSByType):
    TYPE = 'makeNurbCylinder'


class makeNurbPlane(LSByType):
    TYPE = 'makeNurbPlane'


class makeNurbSphere(LSByType):
    TYPE = 'makeNurbSphere'


class makeNurbTorus(LSByType):
    TYPE = 'makeNurbTorus'


class makeNurbsSquare(LSByType):
    TYPE = 'makeNurbsSquare'


class makeTextCurves(LSByType):
    TYPE = 'makeTextCurves'


class makeThreePointCircularArc(LSByType):
    TYPE = 'makeThreePointCircularArc'


class makeThreePointCircularArcManip(LSByType):
    TYPE = 'makeThreePointCircularArcManip'


class makeTwoPointCircularArc(LSByType):
    TYPE = 'makeTwoPointCircularArc'


class makeTwoPointCircularArcManip(LSByType):
    TYPE = 'makeTwoPointCircularArcManip'


class mandelbrot(LSByType):
    TYPE = 'mandelbrot'


class mandelbrot3D(LSByType):
    TYPE = 'mandelbrot3D'


class manip2DContainer(LSByType):
    TYPE = 'manip2DContainer'


class manipContainer(LSByType):
    TYPE = 'manipContainer'


class marble(LSByType):
    TYPE = 'marble'


class markerManip(LSByType):
    TYPE = 'markerManip'


class materialFacade(LSByType):
    TYPE = 'materialFacade'


class materialInfo(LSByType):
    TYPE = 'materialInfo'


class membrane(LSByType):
    TYPE = 'membrane'


class mentalrayTexture(LSByType):
    TYPE = 'mentalrayTexture'


class mesh(LSByType):
    TYPE = 'mesh'


class meshVarGroup(LSByType):
    TYPE = 'meshVarGroup'


class motionPath(LSByType):
    TYPE = 'motionPath'


class motionPathManip(LSByType):
    TYPE = 'motionPathManip'


class motionTrail(LSByType):
    TYPE = 'motionTrail'


class motionTrailShape(LSByType):
    TYPE = 'motionTrailShape'


class mountain(LSByType):
    TYPE = 'mountain'


class moveBezierHandleManip(LSByType):
    TYPE = 'moveBezierHandleManip'


class moveVertexManip(LSByType):
    TYPE = 'moveVertexManip'


class movie(LSByType):
    TYPE = 'movie'


class mpBirailSrf(LSByType):
    TYPE = 'mpBirailSrf'


class multDoubleLinear(LSByType):
    TYPE = 'multDoubleLinear'


class multMatrix(LSByType):
    TYPE = 'multMatrix'


class multilisterLight(LSByType):
    TYPE = 'multilisterLight'


class multiplyDivide(LSByType):
    TYPE = 'multiplyDivide'


class mute(LSByType):
    TYPE = 'mute'


class nCloth(LSByType):
    TYPE = 'nCloth'


class nComponent(LSByType):
    TYPE = 'nComponent'


class nParticle(LSByType):
    TYPE = 'nParticle'


class nRigid(LSByType):
    TYPE = 'nRigid'


class nearestPointOnCurve(LSByType):
    TYPE = 'nearestPointOnCurve'


class network(LSByType):
    TYPE = 'network'


class newtonField(LSByType):
    TYPE = 'newtonField'


class newtonManip(LSByType):
    TYPE = 'newtonManip'


class nexManip(LSByType):
    TYPE = 'nexManip'


class nodeGraphEditorBookmarkInfo(LSByType):
    TYPE = 'nodeGraphEditorBookmarkInfo'


class nodeGraphEditorBookmarks(LSByType):
    TYPE = 'nodeGraphEditorBookmarks'


class nodeGraphEditorInfo(LSByType):
    TYPE = 'nodeGraphEditorInfo'


class noise(LSByType):
    TYPE = 'noise'


class nonLinear(LSByType):
    TYPE = 'nonLinear'


class normalConstraint(LSByType):
    TYPE = 'normalConstraint'


class nucleus(LSByType):
    TYPE = 'nucleus'


class nurbsCurve(LSByType):
    TYPE = 'nurbsCurve'


class nurbsCurveToBezier(LSByType):
    TYPE = 'nurbsCurveToBezier'


class nurbsSurface(LSByType):
    TYPE = 'nurbsSurface'


class nurbsTessellate(LSByType):
    TYPE = 'nurbsTessellate'


class nurbsToSubdiv(LSByType):
    TYPE = 'nurbsToSubdiv'


class nurbsToSubdivProc(LSByType):
    TYPE = 'nurbsToSubdivProc'


class objectAttrFilter(LSByType):
    TYPE = 'objectAttrFilter'


class objectBinFilter(LSByType):
    TYPE = 'objectBinFilter'


class objectFilter(LSByType):
    TYPE = 'objectFilter'


class objectMultiFilter(LSByType):
    TYPE = 'objectMultiFilter'


class objectNameFilter(LSByType):
    TYPE = 'objectNameFilter'


class objectRenderFilter(LSByType):
    TYPE = 'objectRenderFilter'


class objectScriptFilter(LSByType):
    TYPE = 'objectScriptFilter'


class objectSet(LSByType):
    TYPE = 'objectSet'


class objectTypeFilter(LSByType):
    TYPE = 'objectTypeFilter'


class ocean(LSByType):
    TYPE = 'ocean'


class oceanShader(LSByType):
    TYPE = 'oceanShader'


class offsetCos(LSByType):
    TYPE = 'offsetCos'


class offsetCosManip(LSByType):
    TYPE = 'offsetCosManip'


class offsetCurve(LSByType):
    TYPE = 'offsetCurve'


class offsetCurveManip(LSByType):
    TYPE = 'offsetCurveManip'


class offsetSurface(LSByType):
    TYPE = 'offsetSurface'


class offsetSurfaceManip(LSByType):
    TYPE = 'offsetSurfaceManip'


class oldBlindDataBase(LSByType):
    TYPE = 'oldBlindDataBase'


class oldGeometryConstraint(LSByType):
    TYPE = 'oldGeometryConstraint'


class oldNormalConstraint(LSByType):
    TYPE = 'oldNormalConstraint'


class oldTangentConstraint(LSByType):
    TYPE = 'oldTangentConstraint'


class opticalFX(LSByType):
    TYPE = 'opticalFX'


class orientConstraint(LSByType):
    TYPE = 'orientConstraint'


class orientationMarker(LSByType):
    TYPE = 'orientationMarker'


class pairBlend(LSByType):
    TYPE = 'pairBlend'


class paramDimension(LSByType):
    TYPE = 'paramDimension'


class parentConstraint(LSByType):
    TYPE = 'parentConstraint'


class particle(LSByType):
    TYPE = 'particle'


class particleAgeMapper(LSByType):
    TYPE = 'particleAgeMapper'


class particleCloud(LSByType):
    TYPE = 'particleCloud'


class particleColorMapper(LSByType):
    TYPE = 'particleColorMapper'


class particleIncandMapper(LSByType):
    TYPE = 'particleIncandMapper'


class particleSamplerInfo(LSByType):
    TYPE = 'particleSamplerInfo'


class particleTranspMapper(LSByType):
    TYPE = 'particleTranspMapper'


class partition(LSByType):
    TYPE = 'partition'


class passContributionMap(LSByType):
    TYPE = 'passContributionMap'


class passMatrix(LSByType):
    TYPE = 'passMatrix'


class pfxHair(LSByType):
    TYPE = 'pfxHair'


class pfxToon(LSByType):
    TYPE = 'pfxToon'


class phong(LSByType):
    TYPE = 'phong'


class phongE(LSByType):
    TYPE = 'phongE'


class pivot2dManip(LSByType):
    TYPE = 'pivot2dManip'


class pivotAndOrientManip(LSByType):
    TYPE = 'pivotAndOrientManip'


class place2dTexture(LSByType):
    TYPE = 'place2dTexture'


class place3dTexture(LSByType):
    TYPE = 'place3dTexture'


class planarProjManip(LSByType):
    TYPE = 'planarProjManip'


class planarTrimSurface(LSByType):
    TYPE = 'planarTrimSurface'


class plusMinusAverage(LSByType):
    TYPE = 'plusMinusAverage'


class pointConstraint(LSByType):
    TYPE = 'pointConstraint'


class pointEmitter(LSByType):
    TYPE = 'pointEmitter'


class pointLight(LSByType):
    TYPE = 'pointLight'


class pointMatrixMult(LSByType):
    TYPE = 'pointMatrixMult'


class pointOnCurveInfo(LSByType):
    TYPE = 'pointOnCurveInfo'


class pointOnCurveManip(LSByType):
    TYPE = 'pointOnCurveManip'


class pointOnLineManip(LSByType):
    TYPE = 'pointOnLineManip'


class pointOnPolyConstraint(LSByType):
    TYPE = 'pointOnPolyConstraint'


class pointOnSurfManip(LSByType):
    TYPE = 'pointOnSurfManip'


class pointOnSurfaceInfo(LSByType):
    TYPE = 'pointOnSurfaceInfo'


class pointOnSurfaceManip(LSByType):
    TYPE = 'pointOnSurfaceManip'


class poleVectorConstraint(LSByType):
    TYPE = 'poleVectorConstraint'


class polyAppend(LSByType):
    TYPE = 'polyAppend'


class polyAppendVertex(LSByType):
    TYPE = 'polyAppendVertex'


class polyAutoProj(LSByType):
    TYPE = 'polyAutoProj'


class polyAutoProjManip(LSByType):
    TYPE = 'polyAutoProjManip'


class polyAverageVertex(LSByType):
    TYPE = 'polyAverageVertex'


class polyBevel(LSByType):
    TYPE = 'polyBevel'


class polyBevel2(LSByType):
    TYPE = 'polyBevel2'


class polyBevel3(LSByType):
    TYPE = 'polyBevel3'


class polyBlindData(LSByType):
    TYPE = 'polyBlindData'


class polyBoolOp(LSByType):
    TYPE = 'polyBoolOp'


class polyBridgeEdge(LSByType):
    TYPE = 'polyBridgeEdge'


class polyCBoolOp(LSByType):
    TYPE = 'polyCBoolOp'


class polyCaddyManip(LSByType):
    TYPE = 'polyCaddyManip'


class polyChipOff(LSByType):
    TYPE = 'polyChipOff'


class polyCloseBorder(LSByType):
    TYPE = 'polyCloseBorder'


class polyCollapseEdge(LSByType):
    TYPE = 'polyCollapseEdge'


class polyCollapseF(LSByType):
    TYPE = 'polyCollapseF'


class polyColorDel(LSByType):
    TYPE = 'polyColorDel'


class polyColorMod(LSByType):
    TYPE = 'polyColorMod'


class polyColorPerVertex(LSByType):
    TYPE = 'polyColorPerVertex'


class polyCone(LSByType):
    TYPE = 'polyCone'


class polyConnectComponents(LSByType):
    TYPE = 'polyConnectComponents'


class polyContourProj(LSByType):
    TYPE = 'polyContourProj'


class polyCopyUV(LSByType):
    TYPE = 'polyCopyUV'


class polyCrease(LSByType):
    TYPE = 'polyCrease'


class polyCreaseEdge(LSByType):
    TYPE = 'polyCreaseEdge'


class polyCreateFace(LSByType):
    TYPE = 'polyCreateFace'


class polyCreateToolManip(LSByType):
    TYPE = 'polyCreateToolManip'


class polyCube(LSByType):
    TYPE = 'polyCube'


class polyCut(LSByType):
    TYPE = 'polyCut'


class polyCutManip(LSByType):
    TYPE = 'polyCutManip'


class polyCutManipContainer(LSByType):
    TYPE = 'polyCutManipContainer'


class polyCylProj(LSByType):
    TYPE = 'polyCylProj'


class polyCylinder(LSByType):
    TYPE = 'polyCylinder'


class polyDelEdge(LSByType):
    TYPE = 'polyDelEdge'


class polyDelFacet(LSByType):
    TYPE = 'polyDelFacet'


class polyDelVertex(LSByType):
    TYPE = 'polyDelVertex'


class polyDuplicateEdge(LSByType):
    TYPE = 'polyDuplicateEdge'


class polyEdgeToCurve(LSByType):
    TYPE = 'polyEdgeToCurve'


class polyEditEdgeFlow(LSByType):
    TYPE = 'polyEditEdgeFlow'


class polyExtrudeEdge(LSByType):
    TYPE = 'polyExtrudeEdge'


class polyExtrudeFace(LSByType):
    TYPE = 'polyExtrudeFace'


class polyExtrudeVertex(LSByType):
    TYPE = 'polyExtrudeVertex'


class polyFlipEdge(LSByType):
    TYPE = 'polyFlipEdge'


class polyFlipUV(LSByType):
    TYPE = 'polyFlipUV'


class polyHelix(LSByType):
    TYPE = 'polyHelix'


class polyHoleFace(LSByType):
    TYPE = 'polyHoleFace'


class polyLayoutUV(LSByType):
    TYPE = 'polyLayoutUV'


class polyMapCut(LSByType):
    TYPE = 'polyMapCut'


class polyMapDel(LSByType):
    TYPE = 'polyMapDel'


class polyMapSew(LSByType):
    TYPE = 'polyMapSew'


class polyMapSewMove(LSByType):
    TYPE = 'polyMapSewMove'


class polyMappingManip(LSByType):
    TYPE = 'polyMappingManip'


class polyMergeEdge(LSByType):
    TYPE = 'polyMergeEdge'


class polyMergeFace(LSByType):
    TYPE = 'polyMergeFace'


class polyMergeUV(LSByType):
    TYPE = 'polyMergeUV'


class polyMergeVert(LSByType):
    TYPE = 'polyMergeVert'


class polyMergeVertsManip(LSByType):
    TYPE = 'polyMergeVertsManip'


class polyMirror(LSByType):
    TYPE = 'polyMirror'


class polyModifierManip(LSByType):
    TYPE = 'polyModifierManip'


class polyModifierManipContainer(LSByType):
    TYPE = 'polyModifierManipContainer'


class polyMoveEdge(LSByType):
    TYPE = 'polyMoveEdge'


class polyMoveFace(LSByType):
    TYPE = 'polyMoveFace'


class polyMoveFacetUV(LSByType):
    TYPE = 'polyMoveFacetUV'


class polyMoveUV(LSByType):
    TYPE = 'polyMoveUV'


class polyMoveUVManip(LSByType):
    TYPE = 'polyMoveUVManip'


class polyMoveVertex(LSByType):
    TYPE = 'polyMoveVertex'


class polyMoveVertexManip(LSByType):
    TYPE = 'polyMoveVertexManip'


class polyNormal(LSByType):
    TYPE = 'polyNormal'


class polyNormalPerVertex(LSByType):
    TYPE = 'polyNormalPerVertex'


class polyNormalizeUV(LSByType):
    TYPE = 'polyNormalizeUV'


class polyOptUvs(LSByType):
    TYPE = 'polyOptUvs'


class polyPassThru(LSByType):
    TYPE = 'polyPassThru'


class polyPinUV(LSByType):
    TYPE = 'polyPinUV'


class polyPipe(LSByType):
    TYPE = 'polyPipe'


class polyPlanarProj(LSByType):
    TYPE = 'polyPlanarProj'


class polyPlane(LSByType):
    TYPE = 'polyPlane'


class polyPlatonicSolid(LSByType):
    TYPE = 'polyPlatonicSolid'


class polyPoke(LSByType):
    TYPE = 'polyPoke'


class polyPokeManip(LSByType):
    TYPE = 'polyPokeManip'


class polyPrimitiveMisc(LSByType):
    TYPE = 'polyPrimitiveMisc'


class polyPrism(LSByType):
    TYPE = 'polyPrism'


class polyProj(LSByType):
    TYPE = 'polyProj'


class polyProjManip(LSByType):
    TYPE = 'polyProjManip'


class polyProjectCurve(LSByType):
    TYPE = 'polyProjectCurve'


class polyPyramid(LSByType):
    TYPE = 'polyPyramid'


class polyQuad(LSByType):
    TYPE = 'polyQuad'


class polyReduce(LSByType):
    TYPE = 'polyReduce'


class polyRemesh(LSByType):
    TYPE = 'polyRemesh'


class polySelectEditFeedbackManip(LSByType):
    TYPE = 'polySelectEditFeedbackManip'


class polySeparate(LSByType):
    TYPE = 'polySeparate'


class polySewEdge(LSByType):
    TYPE = 'polySewEdge'


class polySmooth(LSByType):
    TYPE = 'polySmooth'


class polySmoothFace(LSByType):
    TYPE = 'polySmoothFace'


class polySmoothProxy(LSByType):
    TYPE = 'polySmoothProxy'


class polySoftEdge(LSByType):
    TYPE = 'polySoftEdge'


class polySphProj(LSByType):
    TYPE = 'polySphProj'


class polySphere(LSByType):
    TYPE = 'polySphere'


class polySpinEdge(LSByType):
    TYPE = 'polySpinEdge'


class polySplit(LSByType):
    TYPE = 'polySplit'


class polySplitEdge(LSByType):
    TYPE = 'polySplitEdge'


class polySplitRing(LSByType):
    TYPE = 'polySplitRing'


class polySplitToolManip1(LSByType):
    TYPE = 'polySplitToolManip1'


class polySplitVert(LSByType):
    TYPE = 'polySplitVert'


class polyStraightenUVBorder(LSByType):
    TYPE = 'polyStraightenUVBorder'


class polySubdEdge(LSByType):
    TYPE = 'polySubdEdge'


class polySubdFace(LSByType):
    TYPE = 'polySubdFace'


class polyToSubdiv(LSByType):
    TYPE = 'polyToSubdiv'


class polyToolFeedbackManip(LSByType):
    TYPE = 'polyToolFeedbackManip'


class polyTorus(LSByType):
    TYPE = 'polyTorus'


class polyTransfer(LSByType):
    TYPE = 'polyTransfer'


class polyTriangulate(LSByType):
    TYPE = 'polyTriangulate'


class polyTweak(LSByType):
    TYPE = 'polyTweak'


class polyTweakUV(LSByType):
    TYPE = 'polyTweakUV'


class polyUVRectangle(LSByType):
    TYPE = 'polyUVRectangle'


class polyUnite(LSByType):
    TYPE = 'polyUnite'


class polyVertexNormalManip(LSByType):
    TYPE = 'polyVertexNormalManip'


class polyWedgeFace(LSByType):
    TYPE = 'polyWedgeFace'


class positionMarker(LSByType):
    TYPE = 'positionMarker'


class postProcessList(LSByType):
    TYPE = 'postProcessList'


class precompExport(LSByType):
    TYPE = 'precompExport'


class projectCurve(LSByType):
    TYPE = 'projectCurve'


class projectTangent(LSByType):
    TYPE = 'projectTangent'


class projectTangentManip(LSByType):
    TYPE = 'projectTangentManip'


class projection(LSByType):
    TYPE = 'projection'


class projectionManip(LSByType):
    TYPE = 'projectionManip'


class projectionMultiManip(LSByType):
    TYPE = 'projectionMultiManip'


class projectionUVManip(LSByType):
    TYPE = 'projectionUVManip'


class propModManip(LSByType):
    TYPE = 'propModManip'


class propMoveTriadManip(LSByType):
    TYPE = 'propMoveTriadManip'


class proxyManager(LSByType):
    TYPE = 'proxyManager'


class psdFileTex(LSByType):
    TYPE = 'psdFileTex'


class quadPtOnLineManip(LSByType):
    TYPE = 'quadPtOnLineManip'


class quadShadingSwitch(LSByType):
    TYPE = 'quadShadingSwitch'


class quatAdd(LSByType):
    TYPE = 'quatAdd'


class quatConjugate(LSByType):
    TYPE = 'quatConjugate'


class quatInvert(LSByType):
    TYPE = 'quatInvert'


class quatNegate(LSByType):
    TYPE = 'quatNegate'


class quatNormalize(LSByType):
    TYPE = 'quatNormalize'


class quatProd(LSByType):
    TYPE = 'quatProd'


class quatSub(LSByType):
    TYPE = 'quatSub'


class quatToEuler(LSByType):
    TYPE = 'quatToEuler'


class radialField(LSByType):
    TYPE = 'radialField'


class ramp(LSByType):
    TYPE = 'ramp'


class rampShader(LSByType):
    TYPE = 'rampShader'


class rbfSrf(LSByType):
    TYPE = 'rbfSrf'


class rbfSrfManip(LSByType):
    TYPE = 'rbfSrfManip'


class rebuildCurve(LSByType):
    TYPE = 'rebuildCurve'


class rebuildSurface(LSByType):
    TYPE = 'rebuildSurface'


class record(LSByType):
    TYPE = 'record'


class reference(LSByType):
    TYPE = 'reference'


class remapColor(LSByType):
    TYPE = 'remapColor'


class remapHsv(LSByType):
    TYPE = 'remapHsv'


class remapValue(LSByType):
    TYPE = 'remapValue'


class renderBox(LSByType):
    TYPE = 'renderBox'


class renderCone(LSByType):
    TYPE = 'renderCone'


class renderGlobals(LSByType):
    TYPE = 'renderGlobals'


class renderGlobalsList(LSByType):
    TYPE = 'renderGlobalsList'


class renderLayer(LSByType):
    TYPE = 'renderLayer'


class renderLayerManager(LSByType):
    TYPE = 'renderLayerManager'


class renderPass(LSByType):
    TYPE = 'renderPass'


class renderPassSet(LSByType):
    TYPE = 'renderPassSet'


class renderQuality(LSByType):
    TYPE = 'renderQuality'


class renderRect(LSByType):
    TYPE = 'renderRect'


class renderSphere(LSByType):
    TYPE = 'renderSphere'


class renderTarget(LSByType):
    TYPE = 'renderTarget'


class renderedImageSource(LSByType):
    TYPE = 'renderedImageSource'


class resolution(LSByType):
    TYPE = 'resolution'


class resultCurveTimeToAngular(LSByType):
    TYPE = 'resultCurveTimeToAngular'


class resultCurveTimeToLinear(LSByType):
    TYPE = 'resultCurveTimeToLinear'


class resultCurveTimeToTime(LSByType):
    TYPE = 'resultCurveTimeToTime'


class resultCurveTimeToUnitless(LSByType):
    TYPE = 'resultCurveTimeToUnitless'


class reverse(LSByType):
    TYPE = 'reverse'


class reverseCurve(LSByType):
    TYPE = 'reverseCurve'


class reverseCurveManip(LSByType):
    TYPE = 'reverseCurveManip'


class reverseSurface(LSByType):
    TYPE = 'reverseSurface'


class reverseSurfaceManip(LSByType):
    TYPE = 'reverseSurfaceManip'


class revolve(LSByType):
    TYPE = 'revolve'


class revolveManip(LSByType):
    TYPE = 'revolveManip'


class revolvedPrimitiveManip(LSByType):
    TYPE = 'revolvedPrimitiveManip'


class rgbToHsv(LSByType):
    TYPE = 'rgbToHsv'


class rigidBody(LSByType):
    TYPE = 'rigidBody'


class rigidConstraint(LSByType):
    TYPE = 'rigidConstraint'


class rigidSolver(LSByType):
    TYPE = 'rigidSolver'


class rock(LSByType):
    TYPE = 'rock'


class rotateHelper(LSByType):
    TYPE = 'rotateHelper'


class rotateLimitsManip(LSByType):
    TYPE = 'rotateLimitsManip'


class rotateManip(LSByType):
    TYPE = 'rotateManip'


class rotateUV2dManip(LSByType):
    TYPE = 'rotateUV2dManip'


class roundConstantRadius(LSByType):
    TYPE = 'roundConstantRadius'


class roundConstantRadiusManip(LSByType):
    TYPE = 'roundConstantRadiusManip'


class roundRadiusCrvManip(LSByType):
    TYPE = 'roundRadiusCrvManip'


class roundRadiusManip(LSByType):
    TYPE = 'roundRadiusManip'


class sampler(LSByType):
    TYPE = 'sampler'


class samplerInfo(LSByType):
    TYPE = 'samplerInfo'


class scaleConstraint(LSByType):
    TYPE = 'scaleConstraint'


class scaleLimitsManip(LSByType):
    TYPE = 'scaleLimitsManip'


class scaleManip(LSByType):
    TYPE = 'scaleManip'


class scaleUV2dManip(LSByType):
    TYPE = 'scaleUV2dManip'


class screenAlignedCircleManip(LSByType):
    TYPE = 'screenAlignedCircleManip'


class script(LSByType):
    TYPE = 'script'


class scriptManip(LSByType):
    TYPE = 'scriptManip'


class sculpt(LSByType):
    TYPE = 'sculpt'


class selectionListOperator(LSByType):
    TYPE = 'selectionListOperator'


class sequenceManager(LSByType):
    TYPE = 'sequenceManager'


class sequencer(LSByType):
    TYPE = 'sequencer'


class setRange(LSByType):
    TYPE = 'setRange'


class shaderGlow(LSByType):
    TYPE = 'shaderGlow'


class shadingEngine(LSByType):
    TYPE = 'shadingEngine'


class shadingMap(LSByType):
    TYPE = 'shadingMap'


class shellTessellate(LSByType):
    TYPE = 'shellTessellate'


class shot(LSByType):
    TYPE = 'shot'


class shrinkWrap(LSByType):
    TYPE = 'shrinkWrap'


class simpleTestNode(LSByType):
    TYPE = 'simpleTestNode'


class simpleVolumeShader(LSByType):
    TYPE = 'simpleVolumeShader'


class singleShadingSwitch(LSByType):
    TYPE = 'singleShadingSwitch'


class sketchPlane(LSByType):
    TYPE = 'sketchPlane'


class skinBinding(LSByType):
    TYPE = 'skinBinding'


class skinCluster(LSByType):
    TYPE = 'skinCluster'


class smear(LSByType):
    TYPE = 'smear'


class smoothCurve(LSByType):
    TYPE = 'smoothCurve'


class smoothTangentSrf(LSByType):
    TYPE = 'smoothTangentSrf'


class snapUV2dManip(LSByType):
    TYPE = 'snapUV2dManip'


class snapshot(LSByType):
    TYPE = 'snapshot'


class snapshotShape(LSByType):
    TYPE = 'snapshotShape'


class snow(LSByType):
    TYPE = 'snow'


class softMod(LSByType):
    TYPE = 'softMod'


class softModHandle(LSByType):
    TYPE = 'softModHandle'


class softModManip(LSByType):
    TYPE = 'softModManip'


class solidFractal(LSByType):
    TYPE = 'solidFractal'


class spBirailSrf(LSByType):
    TYPE = 'spBirailSrf'


class sphericalProjManip(LSByType):
    TYPE = 'sphericalProjManip'


class spotCylinderManip(LSByType):
    TYPE = 'spotCylinderManip'


class spotLight(LSByType):
    TYPE = 'spotLight'


class spotManip(LSByType):
    TYPE = 'spotManip'


class spring(LSByType):
    TYPE = 'spring'


class squareSrf(LSByType):
    TYPE = 'squareSrf'


class squareSrfManip(LSByType):
    TYPE = 'squareSrfManip'


class stencil(LSByType):
    TYPE = 'stencil'


class stereoRigCamera(LSByType):
    TYPE = 'stereoRigCamera'


class stitchAsNurbsShell(LSByType):
    TYPE = 'stitchAsNurbsShell'


class stitchSrf(LSByType):
    TYPE = 'stitchSrf'


class stitchSrfManip(LSByType):
    TYPE = 'stitchSrfManip'


class stroke(LSByType):
    TYPE = 'stroke'


class strokeGlobals(LSByType):
    TYPE = 'strokeGlobals'


class stucco(LSByType):
    TYPE = 'stucco'


class studioClearCoat(LSByType):
    TYPE = 'studioClearCoat'


class styleCurve(LSByType):
    TYPE = 'styleCurve'


class subCurve(LSByType):
    TYPE = 'subCurve'


class subSurface(LSByType):
    TYPE = 'subSurface'


class subdAddTopology(LSByType):
    TYPE = 'subdAddTopology'


class subdAutoProj(LSByType):
    TYPE = 'subdAutoProj'


class subdBlindData(LSByType):
    TYPE = 'subdBlindData'


class subdCleanTopology(LSByType):
    TYPE = 'subdCleanTopology'


class subdHierBlind(LSByType):
    TYPE = 'subdHierBlind'


class subdLayoutUV(LSByType):
    TYPE = 'subdLayoutUV'


class subdMapCut(LSByType):
    TYPE = 'subdMapCut'


class subdMapSewMove(LSByType):
    TYPE = 'subdMapSewMove'


class subdMappingManip(LSByType):
    TYPE = 'subdMappingManip'


class subdPlanarProj(LSByType):
    TYPE = 'subdPlanarProj'


class subdProjManip(LSByType):
    TYPE = 'subdProjManip'


class subdTweak(LSByType):
    TYPE = 'subdTweak'


class subdTweakUV(LSByType):
    TYPE = 'subdTweakUV'


class subdiv(LSByType):
    TYPE = 'subdiv'


class subdivCollapse(LSByType):
    TYPE = 'subdivCollapse'


class subdivComponentId(LSByType):
    TYPE = 'subdivComponentId'


class subdivReverseFaces(LSByType):
    TYPE = 'subdivReverseFaces'


class subdivSurfaceVarGroup(LSByType):
    TYPE = 'subdivSurfaceVarGroup'


class subdivToNurbs(LSByType):
    TYPE = 'subdivToNurbs'


class subdivToPoly(LSByType):
    TYPE = 'subdivToPoly'


class substance(LSByType):
    TYPE = 'substance'


class substanceOutput(LSByType):
    TYPE = 'substanceOutput'


class surfaceEdManip(LSByType):
    TYPE = 'surfaceEdManip'


class surfaceInfo(LSByType):
    TYPE = 'surfaceInfo'


class surfaceLuminance(LSByType):
    TYPE = 'surfaceLuminance'


class surfaceShader(LSByType):
    TYPE = 'surfaceShader'


class surfaceVarGroup(LSByType):
    TYPE = 'surfaceVarGroup'


class symmetryConstraint(LSByType):
    TYPE = 'symmetryConstraint'


class tangentConstraint(LSByType):
    TYPE = 'tangentConstraint'


class texLattice(LSByType):
    TYPE = 'texLattice'


class texLatticeDeformManip(LSByType):
    TYPE = 'texLatticeDeformManip'


class texMoveShellManip(LSByType):
    TYPE = 'texMoveShellManip'


class texSmoothManip(LSByType):
    TYPE = 'texSmoothManip'


class texSmudgeUVManip(LSByType):
    TYPE = 'texSmudgeUVManip'


class textButtonManip(LSByType):
    TYPE = 'textButtonManip'


class textManip2D(LSByType):
    TYPE = 'textManip2D'


class texture3dManip(LSByType):
    TYPE = 'texture3dManip'


class textureBakeSet(LSByType):
    TYPE = 'textureBakeSet'


class textureDeformer(LSByType):
    TYPE = 'textureDeformer'


class textureDeformerHandle(LSByType):
    TYPE = 'textureDeformerHandle'


class textureToGeom(LSByType):
    TYPE = 'textureToGeom'


class time(LSByType):
    TYPE = 'time'


class timeFunction(LSByType):
    TYPE = 'timeFunction'


class timeToUnitConversion(LSByType):
    TYPE = 'timeToUnitConversion'


class timeWarp(LSByType):
    TYPE = 'timeWarp'


class toggleManip(LSByType):
    TYPE = 'toggleManip'


class toggleOnLineManip(LSByType):
    TYPE = 'toggleOnLineManip'


class toolDrawManip(LSByType):
    TYPE = 'toolDrawManip'


class toolDrawManip2D(LSByType):
    TYPE = 'toolDrawManip2D'


class toonLineAttributes(LSByType):
    TYPE = 'toonLineAttributes'


class towPointOnCurveManip(LSByType):
    TYPE = 'towPointOnCurveManip'


class towPointOnSurfaceManip(LSByType):
    TYPE = 'towPointOnSurfaceManip'


class trackInfoManager(LSByType):
    TYPE = 'trackInfoManager'


class trans2dManip(LSByType):
    TYPE = 'trans2dManip'


class transUV2dManip(LSByType):
    TYPE = 'transUV2dManip'


class transferAttributes(LSByType):
    TYPE = 'transferAttributes'


class transform(LSByType):
    TYPE = 'transform'


class transformGeometry(LSByType):
    TYPE = 'transformGeometry'


class translateLimitsManip(LSByType):
    TYPE = 'translateLimitsManip'


class translateManip(LSByType):
    TYPE = 'translateManip'


class translateUVManip(LSByType):
    TYPE = 'translateUVManip'


class transposeMatrix(LSByType):
    TYPE = 'transposeMatrix'


class trim(LSByType):
    TYPE = 'trim'


class trimManip(LSByType):
    TYPE = 'trimManip'


class trimWithBoundaries(LSByType):
    TYPE = 'trimWithBoundaries'


class triplanarProjManip(LSByType):
    TYPE = 'triplanarProjManip'


class tripleShadingSwitch(LSByType):
    TYPE = 'tripleShadingSwitch'


class trsInsertManip(LSByType):
    TYPE = 'trsInsertManip'


class trsManip(LSByType):
    TYPE = 'trsManip'


class turbulenceField(LSByType):
    TYPE = 'turbulenceField'


class turbulenceManip(LSByType):
    TYPE = 'turbulenceManip'


class tweak(LSByType):
    TYPE = 'tweak'


class uniformField(LSByType):
    TYPE = 'uniformField'


class unitConversion(LSByType):
    TYPE = 'unitConversion'


class unitToTimeConversion(LSByType):
    TYPE = 'unitToTimeConversion'


class unknown(LSByType):
    TYPE = 'unknown'


class unknownDag(LSByType):
    TYPE = 'unknownDag'


class unknownTransform(LSByType):
    TYPE = 'unknownTransform'


class untrim(LSByType):
    TYPE = 'untrim'


class useBackground(LSByType):
    TYPE = 'useBackground'


class uv2dManip(LSByType):
    TYPE = 'uv2dManip'


class uvChooser(LSByType):
    TYPE = 'uvChooser'


class vectorProduct(LSByType):
    TYPE = 'vectorProduct'


class vectorRenderGlobals(LSByType):
    TYPE = 'vectorRenderGlobals'


class vertexBakeSet(LSByType):
    TYPE = 'vertexBakeSet'


class viewColorManager(LSByType):
    TYPE = 'viewColorManager'


class volumeAxisField(LSByType):
    TYPE = 'volumeAxisField'


class volumeBindManip(LSByType):
    TYPE = 'volumeBindManip'


class volumeFog(LSByType):
    TYPE = 'volumeFog'


class volumeLight(LSByType):
    TYPE = 'volumeLight'


class volumeNoise(LSByType):
    TYPE = 'volumeNoise'


class volumeShader(LSByType):
    TYPE = 'volumeShader'


class vortexField(LSByType):
    TYPE = 'vortexField'


class water(LSByType):
    TYPE = 'water'


class weightGeometryFilter(LSByType):
    TYPE = 'weightGeometryFilter'


class wire(LSByType):
    TYPE = 'wire'


class wood(LSByType):
    TYPE = 'wood'


class wrap(LSByType):
    TYPE = 'wrap'


class writeToColorBuffer(LSByType):
    TYPE = 'writeToColorBuffer'


class writeToDepthBuffer(LSByType):
    TYPE = 'writeToDepthBuffer'


class writeToLabelBuffer(LSByType):
    TYPE = 'writeToLabelBuffer'


class writeToVectorBuffer(LSByType):
    TYPE = 'writeToVectorBuffer'


class wtAddMatrix(LSByType):
    TYPE = 'wtAddMatrix'


class xformManip(LSByType):
    TYPE = 'xformManip'


class xgmArchiveGuide(LSByType):
    TYPE = 'xgmArchiveGuide'


class xgmCardGuide(LSByType):
    TYPE = 'xgmCardGuide'


class xgmConnectivity(LSByType):
    TYPE = 'xgmConnectivity'


class xgmDescription(LSByType):
    TYPE = 'xgmDescription'


class xgmGuide(LSByType):
    TYPE = 'xgmGuide'


class xgmGuideManip(LSByType):
    TYPE = 'xgmGuideManip'


class xgmGuideSculptManip(LSByType):
    TYPE = 'xgmGuideSculptManip'


class xgmMakeGuide(LSByType):
    TYPE = 'xgmMakeGuide'


class xgmNurbsPatch(LSByType):
    TYPE = 'xgmNurbsPatch'


class xgmPalette(LSByType):
    TYPE = 'xgmPalette'


class xgmPatch(LSByType):
    TYPE = 'xgmPatch'


class xgmPointsManip(LSByType):
    TYPE = 'xgmPointsManip'


class xgmPointsViewer(LSByType):
    TYPE = 'xgmPointsViewer'


class xgmSphereGuide(LSByType):
    TYPE = 'xgmSphereGuide'


class xgmSplineGuide(LSByType):
    TYPE = 'xgmSplineGuide'


class xgmSubdPatch(LSByType):
    TYPE = 'xgmSubdPatch'
