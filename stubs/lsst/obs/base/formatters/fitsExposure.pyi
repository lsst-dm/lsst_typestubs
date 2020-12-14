from lsst.daf.butler import Formatter
from typing import Any, Optional

class FitsExposureFormatter(Formatter):
    supportedExtensions: Any = ...
    extension: str = ...
    supportedWriteParameters: Any = ...
    unsupportedParameters: Any = ...
    @property
    def metadata(self): ...
    def readMetadata(self): ...
    def stripMetadata(self) -> None: ...
    def readComponent(self, component: Any, parameters: Optional[Any] = ...): ...
    def readFull(self, parameters: Optional[Any] = ...): ...
    def read(self, component: Optional[Any] = ...): ...
    def write(self, inMemoryDataset: Any) -> None: ...
    def getImageCompressionSettings(self, recipeName: Any): ...
    @classmethod
    def validateWriteRecipes(cls, recipes: Any): ...

class FitsImageFormatter(FitsExposureFormatter): ...
class FitsMaskFormatter(FitsExposureFormatter): ...
class FitsMaskedImageFormatter(FitsExposureFormatter): ...
