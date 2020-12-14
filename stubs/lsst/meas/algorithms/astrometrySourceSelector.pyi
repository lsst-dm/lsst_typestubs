from .sourceSelector import BaseSourceSelectorConfig as BaseSourceSelectorConfig, BaseSourceSelectorTask as BaseSourceSelectorTask, sourceSelectorRegistry as sourceSelectorRegistry
from lsst.pipe.base import Struct as Struct
from typing import Any, Optional

class AstrometrySourceSelectorConfig(BaseSourceSelectorConfig):
    badFlags: Any = ...
    sourceFluxType: Any = ...
    minSnr: Any = ...

class AstrometrySourceSelectorTask(BaseSourceSelectorTask):
    ConfigClass: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def selectSources(self, sourceCat: Any, matches: Optional[Any] = ..., exposure: Optional[Any] = ...): ...