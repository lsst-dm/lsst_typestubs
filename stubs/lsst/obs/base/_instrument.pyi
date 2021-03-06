import datetime
from .gen2to3 import TranslatorFactory
from abc import ABCMeta, abstractmethod
from lsst.afw.cameraGeom import Camera
from lsst.daf.butler import Butler, DataId, Registry
from typing import Any, Optional, Sequence, Set, Tuple, Union

class Instrument(metaclass=ABCMeta):
    configPaths: Sequence[str] = ...
    policyName: Optional[str] = ...
    obsDataPackage: Optional[str] = ...
    standardCuratedDatasetTypes: Set[str] = ...
    additionalCuratedDatasetTypes: Set[str] = ...
    @property
    @abstractmethod
    def filterDefinitions(self) -> Any: ...
    def __init__(self) -> None: ...
    @classmethod
    @abstractmethod
    def getName(cls) -> Any: ...
    @classmethod
    def getCuratedCalibrationNames(cls: Any) -> Set[str]: ...
    @abstractmethod
    def getCamera(self) -> Any: ...
    @abstractmethod
    def register(self, registry: Any) -> Any: ...
    @classmethod
    def getObsDataPackageDir(cls): ...
    @staticmethod
    def fromName(name: str, registry: Registry) -> Instrument: ...
    @staticmethod
    def importAll(registry: Registry) -> None: ...
    @abstractmethod
    def getRawFormatter(self, dataId: Any) -> Any: ...
    def applyConfigOverrides(self, name: Any, config: Any) -> None: ...
    def writeCuratedCalibrations(self, butler: Butler, collection: Optional[str]=..., labels: Sequence[str]=...) -> None: ...
    def writeAdditionalCuratedCalibrations(self, butler: Butler, collection: Optional[str]=..., labels: Sequence[str]=...) -> None: ...
    def writeCameraGeom(self, butler: Butler, collection: Optional[str]=..., labels: Sequence[str]=...) -> None: ...
    def writeStandardTextCuratedCalibrations(self, butler: Butler, collection: Optional[str]=..., labels: Sequence[str]=...) -> None: ...
    @abstractmethod
    def makeDataIdTranslatorFactory(self) -> TranslatorFactory: ...
    @staticmethod
    def formatCollectionTimestamp(timestamp: Union[str, datetime.datetime]) -> str: ...
    @staticmethod
    def makeCollectionTimestamp() -> str: ...
    @classmethod
    def makeDefaultRawIngestRunName(cls: Any) -> str: ...
    @classmethod
    def makeUnboundedCalibrationRunName(cls: Any, *labels: str) -> str: ...
    @classmethod
    def makeCuratedCalibrationRunName(cls: Any, calibDate: str, *labels: str) -> str: ...
    @classmethod
    def makeCalibrationCollectionName(cls: Any, *labels: str) -> str: ...
    @staticmethod
    def makeRefCatCollectionName(*labels: str) -> str: ...
    @classmethod
    def makeUmbrellaCollectionName(cls: Any) -> str: ...
    @classmethod
    def makeCollectionName(cls: Any, *labels: str) -> str: ...

def makeExposureRecordFromObsInfo(obsInfo: Any, universe: Any): ...
def loadCamera(butler: Butler, dataId: DataId, *, collections: Any=...) -> Tuple[Camera, bool]: ...
