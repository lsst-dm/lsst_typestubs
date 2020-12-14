import abc
import lsst.log as pexConfig
import lsst.log as pipeBase
from typing import Any, Optional

class _FilterCatalog:
    region: Any = ...
    def __init__(self, region: Any) -> None: ...
    def __call__(self, refCat: Any, catRegion: Any): ...

class ReferenceObjectLoader:
    dataIds: Any = ...
    refCats: Any = ...
    log: Any = ...
    config: Any = ...
    def __init__(self, dataIds: Any, refCats: Any, config: Any, log: Optional[Any] = ...) -> None: ...
    def loadPixelBox(self, bbox: Any, wcs: Any, filterName: Optional[Any] = ..., epoch: Optional[Any] = ..., photoCalib: Optional[Any] = ..., bboxPadding: int = ...): ...
    def loadRegion(self, region: Any, filtFunc: Optional[Any] = ..., filterName: Optional[Any] = ..., epoch: Optional[Any] = ...): ...
    def loadSkyCircle(self, ctrCoord: Any, radius: Any, filterName: Optional[Any] = ..., epoch: Optional[Any] = ...): ...
    def joinMatchListWithCatalog(self, matchCat: Any, sourceCat: Any): ...
    @classmethod
    def getMetadataBox(cls, bbox: Any, wcs: Any, filterName: Optional[Any] = ..., photoCalib: Optional[Any] = ..., epoch: Optional[Any] = ..., bboxPadding: int = ...): ...
    @staticmethod
    def getMetadataCircle(coord: Any, radius: Any, filterName: Any, photoCalib: Optional[Any] = ..., epoch: Optional[Any] = ...): ...
    @staticmethod
    def addFluxAliases(refCat: Any, defaultFilter: Any, filterReferenceMap: Any): ...
    @staticmethod
    def remapReferenceCatalogSchema(refCat: Any, *, filterNameList: Optional[Any] = ..., position: bool = ..., photometric: bool = ...): ...

def getRefFluxField(schema: Any, filterName: Optional[Any] = ...): ...
def getRefFluxKeys(schema: Any, filterName: Optional[Any] = ...): ...

class LoadReferenceObjectsConfig(pexConfig.Config):
    pixelMargin: Any = ...
    defaultFilter: Any = ...
    anyFilterMapsToThis: Any = ...
    filterMap: Any = ...
    requireProperMotion: Any = ...
    def validate(self) -> None: ...

class LoadReferenceObjectsTask(pipeBase.Task, metaclass=abc.ABCMeta):
    ConfigClass: Any = ...
    butler: Any = ...
    def __init__(self, butler: Optional[Any] = ..., *args: Any, **kwargs: Any) -> None: ...
    def loadPixelBox(self, bbox: Any, wcs: Any, filterName: Optional[Any] = ..., photoCalib: Optional[Any] = ..., epoch: Optional[Any] = ...): ...
    @abc.abstractmethod
    def loadSkyCircle(self, ctrCoord: Any, radius: Any, filterName: Optional[Any] = ..., epoch: Optional[Any] = ..., centroids: bool = ...) -> Any: ...
    @staticmethod
    def makeMinimalSchema(filterNameList: Any, *, addCentroid: bool = ..., addIsPhotometric: bool = ..., addIsResolved: bool = ..., addIsVariable: bool = ..., coordErrDim: int = ..., addProperMotion: bool = ..., properMotionErrDim: int = ..., addParallax: bool = ...): ...
    def getMetadataBox(self, bbox: Any, wcs: Any, filterName: Optional[Any] = ..., photoCalib: Optional[Any] = ..., epoch: Optional[Any] = ...): ...
    def getMetadataCircle(self, coord: Any, radius: Any, filterName: Any, photoCalib: Optional[Any] = ..., epoch: Optional[Any] = ...): ...
    def joinMatchListWithCatalog(self, matchCat: Any, sourceCat: Any): ...
    def applyProperMotions(self, catalog: Any, epoch: Any) -> None: ...
