from .stamps import AbstractStamp, StampsBase
from enum import Enum
from lsst.afw.image import MaskedImage
from typing import Any, Optional

class RadiiEnum(Enum):
    INNER_RADIUS: Any = ...
    OUTER_RADIUS: Any = ...

class BrightStarStamp(AbstractStamp):
    stamp_im: MaskedImage
    gaiaGMag: float
    gaiaId: int
    annularFlux: float
    @classmethod
    def factory(cls, stamp_im: Any, metadata: Any, idx: Any): ...
    def __init__(self, stamp_im: Any, gaiaGMag: Any, gaiaId: Any, annularFlux: Any) -> None: ...

class BrightStarStamps(StampsBase):
    def __init__(self, starStamps: Any, innerRadius: Optional[Any] = ..., outerRadius: Optional[Any] = ..., metadata: Optional[Any] = ..., use_mask: bool = ..., use_variance: bool = ...) -> None: ...
    @classmethod
    def readFits(cls, filename: Any): ...
    @classmethod
    def readFitsWithOptions(cls, filename: Any, options: Any): ...
    def append(self, item: Any, innerRadius: Any, outerRadius: Any) -> None: ...
    def extend(self, bss: Any) -> None: ...
    def getMagnitudes(self): ...
    def getGaiaIds(self): ...
    def getAnnularFluxes(self): ...
    def selectByMag(self, magMin: Optional[Any] = ..., magMax: Optional[Any] = ...): ...
