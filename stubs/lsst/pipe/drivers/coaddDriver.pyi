from lsst.afw.fits.fitsLib import FitsError as FitsError
from lsst.ctrl.pool.parallel import BatchPoolTask as BatchPoolTask
from lsst.ctrl.pool.pool import NODE as NODE, Pool as Pool, abortOnError as abortOnError
from lsst.pex.config import Config as Config, ConfigurableField as ConfigurableField, Field as Field
from lsst.pipe.base import ArgumentParser as ArgumentParser, ConfigDatasetType as ConfigDatasetType, Struct as Struct
from lsst.pipe.drivers.utils import NullSelectImagesTask as NullSelectImagesTask, TractDataIdContainer as TractDataIdContainer, getDataRef as getDataRef
from lsst.pipe.tasks.assembleCoadd import SafeClipAssembleCoaddTask as SafeClipAssembleCoaddTask
from lsst.pipe.tasks.coaddBase import CoaddTaskRunner as CoaddTaskRunner
from lsst.pipe.tasks.makeCoaddTempExp import MakeCoaddTempExpTask as MakeCoaddTempExpTask
from lsst.pipe.tasks.multiBand import DetectCoaddSourcesTask as DetectCoaddSourcesTask
from lsst.pipe.tasks.selectImages import WcsSelectImagesTask as WcsSelectImagesTask
from typing import Any, Optional

class CoaddDriverConfig(Config):
    coaddName: Any = ...
    select: Any = ...
    makeCoaddTempExp: Any = ...
    doBackgroundReference: Any = ...
    backgroundReference: Any = ...
    assembleCoadd: Any = ...
    doDetection: Any = ...
    detectCoaddSources: Any = ...
    hasFakes: Any = ...
    calexpType: Any = ...
    def setDefaults(self) -> None: ...
    def validate(self) -> None: ...

class CoaddDriverTaskRunner(CoaddTaskRunner):
    reuse: Any = ...
    def __init__(self, TaskClass: Any, parsedCmd: Any, doReturnResults: bool = ...) -> None: ...
    def makeTask(self, parsedCmd: Optional[Any] = ..., args: Optional[Any] = ...): ...
    @staticmethod
    def getTargetList(parsedCmd: Any, **kwargs: Any): ...

def unpickle(factory: Any, args: Any, kwargs: Any): ...

class CoaddDriverTask(BatchPoolTask):
    ConfigClass: Any = ...
    RunnerClass: Any = ...
    reuse: Any = ...
    calexpType: str = ...
    def __init__(self, reuse: Any = ..., **kwargs: Any) -> None: ...
    def __reduce__(self): ...
    @classmethod
    def batchWallTime(cls, time: Any, parsedCmd: Any, numCores: Any): ...
    def runDataRef(self, tractPatchRefList: Any, butler: Any, selectIdList: Any = ...): ...
    def run(self, patchRefList: Any, butler: Any, selectDataList: Any = ...): ...
    def readSelection(self, cache: Any, selectId: Any): ...
    def checkTract(self, cache: Any, tractId: Any, selectIdList: Any): ...
    def warp(self, cache: Any, patchId: Any, selectDataList: Any): ...
    def coadd(self, cache: Any, data: Any) -> None: ...
    def selectExposures(self, patchRef: Any, selectDataList: Any): ...
    def writeMetadata(self, dataRef: Any) -> None: ...
