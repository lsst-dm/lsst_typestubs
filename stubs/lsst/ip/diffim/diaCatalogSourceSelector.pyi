import lsst.meas.algorithms as measAlg
from typing import Any, Optional

class DiaCatalogSourceSelectorConfig(measAlg.BaseStarSelectorConfig):
    fluxLim: Any = ...
    fluxMax: Any = ...
    selectStar: Any = ...
    selectGalaxy: Any = ...
    includeVariable: Any = ...
    grMin: Any = ...
    grMax: Any = ...
    badFlags: Any = ...
    def setDefaults(self) -> None: ...

class CheckSource:
    keys: Any = ...
    fluxLim: Any = ...
    fluxMax: Any = ...
    def __init__(self, table: Any, fluxLim: Any, fluxMax: Any, badFlags: Any) -> None: ...
    def __call__(self, source: Any): ...

class DiaCatalogSourceSelectorTask(measAlg.BaseSourceSelectorTask):
    ConfigClass: Any = ...
    usesMatches: bool = ...
    def selectSources(self, sourceCat: Any, matches: Optional[Any] = ..., exposure: Optional[Any] = ...): ...
