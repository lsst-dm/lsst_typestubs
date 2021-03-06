import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from typing import Any

class DetectionConfig(pexConfig.Config):
    detThreshold: Any = ...
    detThresholdType: Any = ...
    detOnTemplate: Any = ...
    badMaskPlanes: Any = ...
    fpNpixMin: Any = ...
    fpNpixMax: Any = ...
    fpGrowKernelScaling: Any = ...
    fpGrowPix: Any = ...
    scaleByFwhm: Any = ...

class PsfMatchConfig(pexConfig.Config):
    warpingConfig: Any = ...
    detectionConfig: Any = ...
    afwBackgroundConfig: Any = ...
    useAfwBackground: Any = ...
    fitForBackground: Any = ...
    kernelBasisSet: Any = ...
    kernelSize: Any = ...
    scaleByFwhm: Any = ...
    kernelSizeFwhmScaling: Any = ...
    kernelSizeMin: Any = ...
    kernelSizeMax: Any = ...
    spatialModelType: Any = ...
    spatialKernelOrder: Any = ...
    spatialBgOrder: Any = ...
    sizeCellX: Any = ...
    sizeCellY: Any = ...
    nStarPerCell: Any = ...
    maxSpatialIterations: Any = ...
    usePcaForSpatialKernel: Any = ...
    subtractMeanForPca: Any = ...
    numPrincipalComponents: Any = ...
    singleKernelClipping: Any = ...
    kernelSumClipping: Any = ...
    spatialKernelClipping: Any = ...
    checkConditionNumber: Any = ...
    badMaskPlanes: Any = ...
    candidateResidualMeanMax: Any = ...
    candidateResidualStdMax: Any = ...
    useCoreStats: Any = ...
    candidateCoreRadius: Any = ...
    maxKsumSigma: Any = ...
    maxConditionNumber: Any = ...
    conditionNumberType: Any = ...
    maxSpatialConditionNumber: Any = ...
    iterateSingleKernel: Any = ...
    constantVarianceWeighting: Any = ...
    calculateKernelUncertainty: Any = ...
    useBicForKernelBasis: Any = ...

class PsfMatchConfigAL(PsfMatchConfig):
    kernelBasisSet: str = ...
    maxConditionNumber: float = ...
    def setDefaults(self) -> None: ...
    alardNGauss: Any = ...
    alardDegGauss: Any = ...
    alardSigGauss: Any = ...
    alardGaussBeta: Any = ...
    alardMinSig: Any = ...
    alardDegGaussDeconv: Any = ...
    alardMinSigDeconv: Any = ...
    alardNGaussDeconv: Any = ...

class PsfMatchConfigDF(PsfMatchConfig):
    kernelBasisSet: str = ...
    maxConditionNumber: float = ...
    usePcaForSpatialKernel: bool = ...
    subtractMeanForPca: bool = ...
    useBicForKernelBasis: bool = ...
    def setDefaults(self) -> None: ...
    useRegularization: Any = ...
    regularizationType: Any = ...
    centralRegularizationStencil: Any = ...
    forwardRegularizationOrders: Any = ...
    regularizationBorderPenalty: Any = ...
    lambdaType: Any = ...
    lambdaValue: Any = ...
    lambdaScaling: Any = ...
    lambdaStepType: Any = ...
    lambdaMin: Any = ...
    lambdaMax: Any = ...
    lambdaStep: Any = ...

class PsfMatchTask(pipeBase.Task):
    ConfigClass: Any = ...
    kConfig: Any = ...
    useRegularization: Any = ...
    hMat: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
PsfMatch = PsfMatchTask
