from lsst.utils import TemplateMeta
from typing import Any

class Image(metaclass=TemplateMeta):
    def __reduce__(self): ...
    readFitsWithOptions: Any = ...
    writeFitsWithOptions: Any = ...

class DecoratedImage(metaclass=TemplateMeta):
    def convertF(self): ...
    def convertD(self): ...
    readFitsWithOptions: Any = ...
    writeFitsWithOptions: Any = ...
