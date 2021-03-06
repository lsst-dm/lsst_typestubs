import lsst.pipe.base as pexConfig
import lsst.pipe.base as pipeBase
from typing import Any, Optional

class SourceDetectionConfig(pexConfig.Config):
    minPixels: Any = ...
    isotropicGrow: Any = ...
    combinedGrow: Any = ...
    nSigmaToGrow: Any = ...
    returnOriginalFootprints: Any = ...
    thresholdValue: Any = ...
    includeThresholdMultiplier: Any = ...
    thresholdType: Any = ...
    thresholdPolarity: Any = ...
    adjustBackground: Any = ...
    reEstimateBackground: Any = ...
    background: Any = ...
    tempLocalBackground: Any = ...
    doTempLocalBackground: Any = ...
    tempWideBackground: Any = ...
    doTempWideBackground: Any = ...
    nPeaksMaxSimple: Any = ...
    nSigmaForKernel: Any = ...
    statsMask: Any = ...
    def setDefaults(self) -> None: ...

class SourceDetectionTask(pipeBase.Task):
    ConfigClass: Any = ...
    negativeFlagKey: Any = ...
    def __init__(self, schema: Optional[Any] = ..., **kwds: Any) -> None: ...
    def run(self, table: Any, exposure: Any, doSmooth: bool = ..., sigma: Optional[Any] = ..., clearMask: bool = ..., expId: Optional[Any] = ...): ...
    def display(self, exposure: Any, results: Any, convolvedImage: Optional[Any] = ...) -> None: ...
    def applyTempLocalBackground(self, exposure: Any, middle: Any, results: Any) -> None: ...
    def clearMask(self, mask: Any) -> None: ...
    def calculateKernelSize(self, sigma: Any): ...
    def getPsf(self, exposure: Any, sigma: Optional[Any] = ...): ...
    def convolveImage(self, maskedImage: Any, psf: Any, doSmooth: bool = ...): ...
    def applyThreshold(self, middle: Any, bbox: Any, factor: float = ...): ...
    def finalizeFootprints(self, mask: Any, results: Any, sigma: Any, factor: float = ...) -> None: ...
    def reEstimateBackground(self, maskedImage: Any, backgrounds: Any): ...
    def clearUnwantedResults(self, mask: Any, results: Any) -> None: ...
    def detectFootprints(self, exposure: Any, doSmooth: bool = ..., sigma: Optional[Any] = ..., clearMask: bool = ..., expId: Optional[Any] = ...): ...
    def makeThreshold(self, image: Any, thresholdParity: Any, factor: float = ...): ...
    def updatePeaks(self, fpSet: Any, image: Any, threshold: Any) -> None: ...
    @staticmethod
    def setEdgeBits(maskedImage: Any, goodBBox: Any, edgeBitmask: Any) -> None: ...
    def tempWideBackgroundContext(self, exposure: Any) -> None: ...

def addExposures(exposureList: Any): ...
