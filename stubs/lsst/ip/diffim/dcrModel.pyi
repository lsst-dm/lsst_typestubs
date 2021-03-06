from typing import Any, Optional

class DcrModel:
    dcrNumSubfilters: Any = ...
    modelImages: Any = ...
    photoCalib: Any = ...
    def __init__(self, modelImages: Any, effectiveWavelength: Any, bandwidth: Any, filterInfo: Optional[Any] = ..., psf: Optional[Any] = ..., mask: Optional[Any] = ..., variance: Optional[Any] = ..., photoCalib: Optional[Any] = ...) -> None: ...
    @classmethod
    def fromImage(cls, maskedImage: Any, dcrNumSubfilters: Any, effectiveWavelength: Any, bandwidth: Any, filterInfo: Optional[Any] = ..., psf: Optional[Any] = ..., photoCalib: Optional[Any] = ...): ...
    @classmethod
    def fromDataRef(cls, dataRef: Any, effectiveWavelength: Any, bandwidth: Any, datasetType: str = ..., numSubfilters: Optional[Any] = ..., **kwargs: Any): ...
    @classmethod
    def fromQuantum(cls, availableCoaddRefs: Any, effectiveWavelength: Any, bandwidth: Any): ...
    def __len__(self): ...
    def __getitem__(self, subfilter: Any): ...
    def __setitem__(self, subfilter: Any, maskedImage: Any) -> None: ...
    @property
    def effectiveWavelength(self): ...
    @property
    def filter(self): ...
    @property
    def bandwidth(self): ...
    @property
    def psf(self): ...
    @property
    def bbox(self): ...
    @property
    def mask(self): ...
    @property
    def variance(self): ...
    def getReferenceImage(self, bbox: Optional[Any] = ...): ...
    def assign(self, dcrSubModel: Any, bbox: Optional[Any] = ...) -> None: ...
    def buildMatchedTemplate(self, exposure: Optional[Any] = ..., order: int = ..., visitInfo: Optional[Any] = ..., bbox: Optional[Any] = ..., wcs: Optional[Any] = ..., mask: Optional[Any] = ..., splitSubfilters: bool = ..., splitThreshold: float = ..., amplifyModel: float = ...): ...
    def buildMatchedExposure(self, exposure: Optional[Any] = ..., visitInfo: Optional[Any] = ..., bbox: Optional[Any] = ..., wcs: Optional[Any] = ..., mask: Optional[Any] = ...): ...
    def conditionDcrModel(self, modelImages: Any, bbox: Any, gain: float = ...) -> None: ...
    def regularizeModelIter(self, subfilter: Any, newModel: Any, bbox: Any, regularizationFactor: Any, regularizationWidth: int = ...) -> None: ...
    def regularizeModelFreq(self, modelImages: Any, bbox: Any, statsCtrl: Any, regularizationFactor: Any, regularizationWidth: int = ..., mask: Optional[Any] = ..., convergenceMaskPlanes: str = ...) -> None: ...
    def calculateNoiseCutoff(self, image: Any, statsCtrl: Any, bufferSize: Any, convergenceMaskPlanes: str = ..., mask: Optional[Any] = ..., bbox: Optional[Any] = ...): ...
    def applyImageThresholds(self, image: Any, highThreshold: Optional[Any] = ..., lowThreshold: Optional[Any] = ..., regularizationWidth: int = ...) -> None: ...

def applyDcr(image: Any, dcr: Any, useInverse: bool = ..., splitSubfilters: bool = ..., splitThreshold: float = ..., doPrefilter: bool = ..., order: int = ...): ...
def calculateDcr(visitInfo: Any, wcs: Any, effectiveWavelength: Any, bandwidth: Any, dcrNumSubfilters: Any, splitSubfilters: bool = ...): ...
def calculateImageParallacticAngle(visitInfo: Any, wcs: Any): ...
