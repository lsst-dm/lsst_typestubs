import lsst.afw.table as pexConfig
import lsst.afw.table as pipeBase
from typing import Any, Optional

class FgcmFitCycleConfig(pexConfig.Config):
    bands: Any = ...
    fitFlag: Any = ...
    fitBands: Any = ...
    requiredFlag: Any = ...
    requiredBands: Any = ...
    filterMap: Any = ...
    doReferenceCalibration: Any = ...
    refStarSnMin: Any = ...
    refStarOutlierNSig: Any = ...
    applyRefStarColorCuts: Any = ...
    nCore: Any = ...
    nStarPerRun: Any = ...
    nExpPerRun: Any = ...
    reserveFraction: Any = ...
    freezeStdAtmosphere: Any = ...
    precomputeSuperStarInitialCycle: Any = ...
    superStarSubCcd: Any = ...
    superStarSubCcdDict: Any = ...
    superStarSubCcdChebyshevOrder: Any = ...
    superStarSubCcdTriangular: Any = ...
    superStarSigmaClip: Any = ...
    focalPlaneSigmaClip: Any = ...
    ccdGraySubCcd: Any = ...
    ccdGraySubCcdDict: Any = ...
    ccdGraySubCcdChebyshevOrder: Any = ...
    ccdGraySubCcdTriangular: Any = ...
    ccdGrayFocalPlaneDict: Any = ...
    ccdGrayFocalPlaneFitMinCcd: Any = ...
    ccdGrayFocalPlaneChebyshevOrder: Any = ...
    cycleNumber: Any = ...
    isFinalCycle: Any = ...
    maxIterBeforeFinalCycle: Any = ...
    deltaMagBkgOffsetPercentile: Any = ...
    deltaMagBkgPerCcd: Any = ...
    utBoundary: Any = ...
    washMjds: Any = ...
    epochMjds: Any = ...
    minObsPerBand: Any = ...
    latitude: Any = ...
    brightObsGrayMax: Any = ...
    minStarPerCcd: Any = ...
    minCcdPerExp: Any = ...
    maxCcdGrayErr: Any = ...
    minStarPerExp: Any = ...
    minExpPerNight: Any = ...
    expGrayInitialCut: Any = ...
    expGrayPhotometricCut: Any = ...
    expGrayPhotometricCutDict: Any = ...
    expGrayHighCut: Any = ...
    expGrayHighCutDict: Any = ...
    expGrayRecoverCut: Any = ...
    expVarGrayPhotometricCut: Any = ...
    expVarGrayPhotometricCutDict: Any = ...
    expGrayErrRecoverCut: Any = ...
    aperCorrFitNBins: Any = ...
    aperCorrInputSlopes: Any = ...
    aperCorrInputSlopeDict: Any = ...
    sedFudgeFactors: Any = ...
    sedboundaryterms: Any = ...
    sedterms: Any = ...
    sigFgcmMaxErr: Any = ...
    sigFgcmMaxEGray: Any = ...
    sigFgcmMaxEGrayDict: Any = ...
    ccdGrayMaxStarErr: Any = ...
    approxThroughput: Any = ...
    approxThroughputDict: Any = ...
    sigmaCalRange: Any = ...
    sigmaCalFitPercentile: Any = ...
    sigmaCalPlotPercentile: Any = ...
    sigma0Phot: Any = ...
    mapLongitudeRef: Any = ...
    mapNSide: Any = ...
    outfileBase: Any = ...
    starColorCuts: Any = ...
    colorSplitIndices: Any = ...
    colorSplitBands: Any = ...
    modelMagErrors: Any = ...
    useQuadraticPwv: Any = ...
    instrumentParsPerBand: Any = ...
    instrumentSlopeMinDeltaT: Any = ...
    fitMirrorChromaticity: Any = ...
    coatingMjds: Any = ...
    outputStandardsBeforeFinalCycle: Any = ...
    outputZeropointsBeforeFinalCycle: Any = ...
    useRepeatabilityForExpGrayCuts: Any = ...
    useRepeatabilityForExpGrayCutsDict: Any = ...
    autoPhotometricCutNSig: Any = ...
    autoHighCutNSig: Any = ...
    quietMode: Any = ...
    randomSeed: Any = ...
    def setDefaults(self) -> None: ...
    def validate(self) -> None: ...

class FgcmFitCycleRunner(pipeBase.ButlerInitializedTaskRunner):
    @staticmethod
    def getTargetList(parsedCmd: Any): ...
    def __call__(self, butler: Any): ...
    def run(self, parsedCmd: Any): ...

class FgcmFitCycleTask(pipeBase.CmdLineTask):
    ConfigClass: Any = ...
    RunnerClass: Any = ...
    def __init__(self, butler: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def runDataRef(self, butler: Any) -> None: ...
    def writeConfig(self, butler: Any, clobber: bool = ..., doBackup: bool = ...) -> None: ...
