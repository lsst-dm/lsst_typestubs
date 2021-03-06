from . import plugins as plugins
from typing import Any, Optional

DEFAULT_PLUGINS: Any

class DeblenderResult:
    filters: Any = ...
    log: Any = ...
    mMaskedImage: Any = ...
    footprint: Any = ...
    psfs: Any = ...
    peakCount: Any = ...
    deblendedParents: Any = ...
    peaks: Any = ...
    blend: Any = ...
    failed: bool = ...
    def __init__(self, footprint: Any, mMaskedImage: Any, psfs: Any, psffwhms: Any, log: Any, maxNumberOfPeaks: int = ..., avgNoise: Optional[Any] = ...) -> None: ...
    def getParentProperty(self, propertyName: Any): ...
    def setTemplateSums(self, templateSums: Any, fidx: Optional[Any] = ...) -> None: ...

class DeblendedParent:
    filter: Any = ...
    fp: Any = ...
    maskedImage: Any = ...
    psf: Any = ...
    psffwhm: Any = ...
    img: Any = ...
    imbb: Any = ...
    varimg: Any = ...
    mask: Any = ...
    avgNoise: Any = ...
    debResult: Any = ...
    peakCount: Any = ...
    templateSum: Any = ...
    peaks: Any = ...
    def __init__(self, filterName: Any, footprint: Any, maskedImage: Any, psf: Any, psffwhm: Any, avgNoise: Any, maxNumberOfPeaks: Any, debResult: Any) -> None: ...
    bb: Any = ...
    def updateFootprintBbox(self) -> None: ...

class MultiColorPeak:
    filters: Any = ...
    deblendedPeaks: Any = ...
    parent: Any = ...
    pki: Any = ...
    skip: bool = ...
    deblendedAsPsf: bool = ...
    x: Any = ...
    y: Any = ...
    def __init__(self, peaks: Any, pki: Any, parent: Any) -> None: ...

class DeblendedPeak:
    peak: Any = ...
    pki: Any = ...
    parent: Any = ...
    multiColorPeak: Any = ...
    skip: bool = ...
    outOfBounds: bool = ...
    tinyFootprint: bool = ...
    noValidPixels: bool = ...
    deblendedAsPsf: bool = ...
    degenerate: bool = ...
    psfFitFailed: bool = ...
    psfFitBadDof: bool = ...
    psfFit1: Any = ...
    psfFit2: Any = ...
    psfFit3: Any = ...
    psfFitBigDecenter: bool = ...
    psfFitWithDecenter: bool = ...
    psfFitR0: Any = ...
    psfFitR1: Any = ...
    psfFitStampExtent: Any = ...
    psfFitCenter: Any = ...
    psfFitBest: Any = ...
    psfFitParams: Any = ...
    psfFitFlux: Any = ...
    psfFitNOthers: Any = ...
    psfFitDebugPsf0Img: Any = ...
    psfFitDebugPsfImg: Any = ...
    psfFitDebugPsfDerivImg: Any = ...
    psfFitDebugPsfModel: Any = ...
    failedSymmetricTemplate: bool = ...
    templateImage: Any = ...
    templateFootprint: Any = ...
    fluxPortion: Any = ...
    strayFlux: Any = ...
    hasRampedTemplate: bool = ...
    patched: bool = ...
    origTemplate: Any = ...
    origFootprint: Any = ...
    rampedTemplate: Any = ...
    medianFilteredTemplate: Any = ...
    templateWeight: float = ...
    def __init__(self, peak: Any, pki: Any, parent: Any, multiColorPeak: Optional[Any] = ...) -> None: ...
    @property
    def psfFitChisq(self): ...
    @property
    def psfFitDof(self): ...
    def getFluxPortion(self, strayFlux: bool = ...): ...
    def setStrayFlux(self, stray: Any) -> None: ...
    def setFluxPortion(self, mimg: Any) -> None: ...
    def setTemplateWeight(self, w: Any) -> None: ...
    def setPatched(self) -> None: ...
    def setOrigTemplate(self, t: Any, tfoot: Any) -> None: ...
    def setRampedTemplate(self, t: Any, tfoot: Any) -> None: ...
    def setMedianFilteredTemplate(self, t: Any, tfoot: Any) -> None: ...
    psfFootprint: Any = ...
    psfTemplate: Any = ...
    def setPsfTemplate(self, tim: Any, tfoot: Any) -> None: ...
    def setOutOfBounds(self) -> None: ...
    def setTinyFootprint(self) -> None: ...
    def setNoValidPixels(self) -> None: ...
    def setPsfFitFailed(self) -> None: ...
    def setBadPsfDof(self) -> None: ...
    def setDeblendedAsPsf(self) -> None: ...
    def setFailedSymmetricTemplate(self) -> None: ...
    def setTemplate(self, image: Any, footprint: Any) -> None: ...

def deblend(footprint: Any, maskedImage: Any, psf: Any, psffwhm: Any, psfChisqCut1: float = ..., psfChisqCut2: float = ..., psfChisqCut2b: float = ..., fitPsfs: bool = ..., medianSmoothTemplate: bool = ..., medianFilterHalfsize: int = ..., monotonicTemplate: bool = ..., weightTemplates: bool = ..., log: Optional[Any] = ..., verbose: bool = ..., sigma1: Optional[Any] = ..., maxNumberOfPeaks: int = ..., assignStrayFlux: bool = ..., strayFluxToPointSources: str = ..., strayFluxAssignment: str = ..., rampFluxAtEdge: bool = ..., patchEdges: bool = ..., tinyFootprintSize: int = ..., getTemplateSum: bool = ..., clipStrayFluxFraction: float = ..., clipFootprintToNonzero: bool = ..., removeDegenerateTemplates: bool = ..., maxTempDotProd: float = ...): ...
def newDeblend(debPlugins: Any, footprint: Any, mMaskedImage: Any, psfs: Any, psfFwhms: Any, log: Optional[Any] = ..., verbose: bool = ..., avgNoise: Optional[Any] = ..., maxNumberOfPeaks: int = ...): ...

class CachingPsf:
    cache: Any = ...
    psf: Any = ...
    def __init__(self, psf: Any) -> None: ...
    def computeImage(self, cx: Any, cy: Any): ...
