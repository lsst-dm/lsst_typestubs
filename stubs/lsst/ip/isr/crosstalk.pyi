from lsst.ip.isr import IsrCalib
from lsst.pex.config import Config
from lsst.pipe.base import Task
from typing import Any, Optional

class CrosstalkCalib(IsrCalib):
    hasCrosstalk: bool = ...
    nAmp: Any = ...
    crosstalkShape: Any = ...
    coeffs: Any = ...
    coeffErr: Any = ...
    coeffNum: Any = ...
    coeffValid: Any = ...
    interChip: Any = ...
    def __init__(self, detector: Optional[Any] = ..., nAmp: int = ..., **kwargs: Any) -> None: ...
    def updateMetadata(self, setDate: bool = ..., **kwargs: Any) -> None: ...
    def fromDetector(self, detector: Any, coeffVector: Optional[Any] = ...): ...
    @classmethod
    def fromDict(cls, dictionary: Any): ...
    def toDict(self): ...
    @classmethod
    def fromTable(cls, tableList: Any): ...
    def toTable(self): ...
    @staticmethod
    def extractAmp(image: Any, amp: Any, ampTarget: Any, isTrimmed: bool = ...): ...
    @staticmethod
    def calculateBackground(mi: Any, badPixels: Any = ...): ...
    def subtractCrosstalk(self, thisExposure: Any, sourceExposure: Optional[Any] = ..., crosstalkCoeffs: Optional[Any] = ..., badPixels: Any = ..., minPixelToMask: int = ..., crosstalkStr: str = ..., isTrimmed: bool = ..., backgroundMethod: str = ...) -> None: ...

class CrosstalkConfig(Config):
    minPixelToMask: Any = ...
    crosstalkMaskPlane: Any = ...
    crosstalkBackgroundMethod: Any = ...
    useConfigCoefficients: Any = ...
    crosstalkValues: Any = ...
    crosstalkShape: Any = ...
    def getCrosstalk(self, detector: Optional[Any] = ...): ...
    def hasCrosstalk(self, detector: Optional[Any] = ...): ...

class CrosstalkTask(Task):
    ConfigClass: Any = ...
    def prepCrosstalk(self, dataRef: Any, crosstalk: Optional[Any] = ...) -> None: ...
    def run(self, exposure: Any, crosstalk: Optional[Any] = ..., crosstalkSources: Optional[Any] = ..., isTrimmed: bool = ...) -> None: ...

class NullCrosstalkTask(CrosstalkTask):
    def run(self, exposure: Any, crosstalkSources: Optional[Any] = ...) -> None: ...
