import lsst.pipe.base
from typing import Any, Optional

class BaseReferencesConfig(lsst.pex.config.Config):
    removePatchOverlaps: Any = ...
    filter: Any = ...

class BaseReferencesTask(lsst.pipe.base.Task):
    ConfigClass: Any = ...
    def __init__(self, butler: Optional[Any] = ..., schema: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def getSchema(self, butler: Any) -> None: ...
    def getWcs(self, dataRef: Any) -> None: ...
    def fetchInBox(self, dataRef: Any, bbox: Any, wcs: Any) -> None: ...
    def fetchInPatches(self, dataRef: Any, patchList: Any) -> None: ...
    def subset(self, sources: Any, bbox: Any, wcs: Any) -> None: ...

class CoaddSrcReferencesConfig(BaseReferencesTask.ConfigClass):
    coaddName: Any = ...
    skipMissing: Any = ...
    def validate(self) -> None: ...

class CoaddSrcReferencesTask(BaseReferencesTask):
    ConfigClass: Any = ...
    datasetSuffix: str = ...
    schema: Any = ...
    def __init__(self, butler: Optional[Any] = ..., schema: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def getWcs(self, dataRef: Any): ...
    def fetchInPatches(self, dataRef: Any, patchList: Any) -> None: ...
    def fetchInBox(self, dataRef: Any, bbox: Any, wcs: Any, pad: int = ...): ...

class MultiBandReferencesConfig(CoaddSrcReferencesTask.ConfigClass):
    def validate(self) -> None: ...

class MultiBandReferencesTask(CoaddSrcReferencesTask):
    ConfigClass: Any = ...
    datasetSuffix: str = ...