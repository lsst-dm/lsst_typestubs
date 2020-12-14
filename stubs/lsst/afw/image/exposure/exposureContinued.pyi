from lsst.utils import TemplateMeta
from typing import Any

class Exposure(metaclass=TemplateMeta):
    def __reduce__(self): ...
    def convertF(self): ...
    def convertD(self): ...
    def getImage(self): ...
    def setImage(self, image: Any) -> None: ...
    image: Any = ...
    def getMask(self): ...
    def setMask(self, mask: Any) -> None: ...
    mask: Any = ...
    def getVariance(self): ...
    def setVariance(self, variance: Any) -> None: ...
    variance: Any = ...
    readFitsWithOptions: Any = ...
    writeFitsWithOptions: Any = ...
