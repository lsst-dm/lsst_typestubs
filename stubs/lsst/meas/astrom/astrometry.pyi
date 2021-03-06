from .ref_match import RefMatchConfig, RefMatchTask
from typing import Any, Optional

class AstrometryConfig(RefMatchConfig):
    wcsFitter: Any = ...
    forceKnownWcs: Any = ...
    maxIter: Any = ...
    minMatchDistanceArcSec: Any = ...
    sourceFluxType: str = ...
    def setDefaults(self) -> None: ...

class AstrometryTask(RefMatchTask):
    ConfigClass: Any = ...
    usedKey: Any = ...
    def __init__(self, refObjLoader: Any, schema: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def run(self, sourceCat: Any, exposure: Any): ...
    def solve(self, exposure: Any, sourceCat: Any): ...
