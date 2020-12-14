import lsst.daf.persistence.butlerExceptions as pexConfig
import lsst.daf.persistence.butlerExceptions as pipeBase
from typing import Any, Optional

class MakeBrighterFatterKernelTaskConfig(pexConfig.Config):
    isr: Any = ...
    isrMandatorySteps: Any = ...
    isrForbiddenSteps: Any = ...
    isrDesirableSteps: Any = ...
    doCalcGains: Any = ...
    doPlotPtcs: Any = ...
    forceZeroSum: Any = ...
    correlationQuadraticFit: Any = ...
    correlationModelRadius: Any = ...
    correlationModelSlope: Any = ...
    ccdKey: Any = ...
    minMeanSignal: Any = ...
    maxMeanSignal: Any = ...
    maxIterRegression: Any = ...
    nSigmaClipGainCalc: Any = ...
    nSigmaClipRegression: Any = ...
    xcorrCheckRejectLevel: Any = ...
    maxIterSuccessiveOverRelaxation: Any = ...
    eLevelSuccessiveOverRelaxation: Any = ...
    nSigmaClipKernelGen: Any = ...
    nSigmaClipXCorr: Any = ...
    maxLag: Any = ...
    nPixBorderGainCalc: Any = ...
    nPixBorderXCorr: Any = ...
    biasCorr: Any = ...
    backgroundBinSize: Any = ...
    fixPtcThroughOrigin: Any = ...
    level: Any = ...
    ignoreAmpsForAveraging: Any = ...
    backgroundWarnLevel: Any = ...

class BrighterFatterKernelTaskDataIdContainer(pipeBase.DataIdContainer):
    def makeDataRefList(self, namespace: Any) -> None: ...

class BrighterFatterKernel:
    def __init__(self, originalLevel: Any, **kwargs: Any) -> None: ...
    def __setattr__(self, attribute: Any, value: Any) -> None: ...
    def replaceDetectorKernelWithAmpKernel(self, ampName: Any, detectorName: Any) -> None: ...
    def makeDetectorKernelFromAmpwiseKernels(self, detectorName: Any, ampsToExclude: Any = ..., overwrite: bool = ...) -> None: ...

class BrighterFatterGain:
    gains: dict
    ptcResults: dict
    def __init__(self, gains: Any, ptcResults: Any) -> None: ...

class MakeBrighterFatterKernelTask(pipeBase.CmdLineTask):
    RunnerClass: Any = ...
    ConfigClass: Any = ...
    debug: Any = ...
    disp1: Any = ...
    disp2: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def validateIsrConfig(self) -> None: ...
    def runDataRef(self, dataRef: Any, visitPairs: Any): ...
    def estimateGains(self, dataRef: Any, visitPairs: Any): ...
    def generateKernel(self, corrs: Any, means: Any, objId: Any, rejectLevel: Optional[Any] = ...): ...
    def successiveOverRelax(self, source: Any, maxIter: Optional[Any] = ..., eLevel: Optional[Any] = ...): ...

def calcBiasCorr(fluxLevels: Any, imageShape: Any, repeats: int = ..., seed: int = ..., addCorrelations: bool = ..., correlationStrength: float = ..., maxLag: int = ..., nSigmaClip: int = ..., border: int = ..., logger: Optional[Any] = ...): ...
