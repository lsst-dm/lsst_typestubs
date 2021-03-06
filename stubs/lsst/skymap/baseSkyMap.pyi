import lsst.pex.config as pexConfig
from typing import Any, Optional

class BaseSkyMapConfig(pexConfig.Config):
    patchInnerDimensions: Any = ...
    patchBorder: Any = ...
    tractOverlap: Any = ...
    pixelScale: Any = ...
    projection: Any = ...
    rotation: Any = ...

class BaseSkyMap:
    ConfigClass: Any = ...
    config: Any = ...
    def __init__(self, config: Optional[Any] = ...) -> None: ...
    def findTract(self, coord: Any): ...
    def findTractPatchList(self, coordList: Any): ...
    def findClosestTractPatchList(self, coordList: Any): ...
    def __getitem__(self, ind: Any): ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def __hash__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def logSkyMapInfo(self, log: Any) -> None: ...
    def getSha1(self): ...
    def updateSha1(self, sha1: Any) -> None: ...
    SKYMAP_RUN_COLLECTION_NAME: str = ...
    SKYMAP_DATASET_TYPE_NAME: str = ...
    def register(self, name: Any, butler: Any) -> None: ...
