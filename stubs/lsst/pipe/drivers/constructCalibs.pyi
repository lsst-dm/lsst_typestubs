import argparse
from .checksum import checksum as checksum
from .utils import getDataRef as getDataRef
from lsst.ctrl.pool.parallel import BatchPoolTask as BatchPoolTask
from lsst.ctrl.pool.pool import NODE as NODE, Pool as Pool
from lsst.ip.isr import IsrTask as IsrTask
from lsst.pex.config import Config as Config, ConfigField as ConfigField, ConfigurableField as ConfigurableField, Field as Field, ListField as ListField
from lsst.pipe.base import ArgumentParser as ArgumentParser, Struct as Struct, Task as Task, TaskRunner as TaskRunner
from lsst.pipe.drivers.background import FocalPlaneBackground as FocalPlaneBackground, FocalPlaneBackgroundConfig as FocalPlaneBackgroundConfig, MaskObjectsTask as MaskObjectsTask, SkyMeasurementTask as SkyMeasurementTask
from lsst.pipe.drivers.visualizeVisit import makeCameraImage as makeCameraImage
from lsst.pipe.tasks.repair import RepairTask as RepairTask
from typing import Any, Optional

class CalibStatsConfig(Config):
    stat: Any = ...
    clip: Any = ...
    nIter: Any = ...
    maxVisitsToCalcErrorFromInputVariance: Any = ...
    mask: Any = ...

class CalibStatsTask(Task):
    ConfigClass: Any = ...
    def run(self, exposureOrImage: Any): ...

class CalibCombineConfig(Config):
    rows: Any = ...
    mask: Any = ...
    combine: Any = ...
    clip: Any = ...
    nIter: Any = ...
    stats: Any = ...

class CalibCombineTask(Task):
    ConfigClass: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def run(self, sensorRefList: Any, expScales: Optional[Any] = ..., finalScale: Optional[Any] = ..., inputName: str = ...): ...
    def getDimensions(self, sensorRefList: Any, inputName: str = ...): ...
    def applyScale(self, exposure: Any, scale: Optional[Any] = ...) -> None: ...
    def combine(self, target: Any, imageList: Any, stats: Any) -> None: ...

def getSize(dimList: Any): ...
def dictToTuple(dict_: Any, keys: Any): ...
def getCcdIdListFromExposures(expRefList: Any, level: str = ..., ccdKeys: Any = ...): ...
def mapToMatrix(pool: Any, func: Any, ccdIdLists: Any, *args: Any, **kwargs: Any): ...

class CalibIdAction(argparse.Action):
    def __call__(self, parser: Any, namespace: Any, values: Any, option_string: Any) -> None: ...

class CalibArgumentParser(ArgumentParser):
    calibName: Any = ...
    def __init__(self, calibName: Any, *args: Any, **kwargs: Any) -> None: ...
    def parse_args(self, *args: Any, **kwargs: Any): ...

class CalibConfig(Config):
    clobber: Any = ...
    isr: Any = ...
    dateObs: Any = ...
    dateCalib: Any = ...
    filter: Any = ...
    combination: Any = ...
    ccdKeys: Any = ...
    visitKeys: Any = ...
    calibKeys: Any = ...
    doCameraImage: Any = ...
    binning: Any = ...
    def setDefaults(self) -> None: ...

class CalibTaskRunner(TaskRunner):
    @staticmethod
    def getTargetList(parsedCmd: Any, **kwargs: Any): ...
    def __call__(self, args: Any): ...

class CalibTask(BatchPoolTask):
    ConfigClass: Any = ...
    RunnerClass: Any = ...
    filterName: Any = ...
    calibName: Any = ...
    exposureTime: float = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def batchWallTime(cls, time: Any, parsedCmd: Any, numCores: Any): ...
    def runDataRef(self, expRefList: Any, butler: Any, calibId: Any): ...
    def getOutputId(self, expRefList: Any, calibId: Any): ...
    def getMjd(self, butler: Any, dataId: Any, timescale: Any = ...): ...
    def getFilter(self, butler: Any, dataId: Any): ...
    def addMissingKeys(self, dataId: Any, butler: Any, missingKeys: Optional[Any] = ..., calibName: Optional[Any] = ...) -> None: ...
    def updateMetadata(self, calibImage: Any, exposureTime: Any, darkTime: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def scatterProcess(self, pool: Any, ccdIdLists: Any): ...
    def process(self, cache: Any, ccdId: Any, outputName: str = ..., **kwargs: Any): ...
    def processSingle(self, dataRef: Any): ...
    def processWrite(self, dataRef: Any, exposure: Any, outputName: str = ...) -> None: ...
    def processResult(self, exposure: Any) -> None: ...
    def scale(self, ccdIdLists: Any, data: Any): ...
    def scatterCombine(self, pool: Any, outputId: Any, ccdIdLists: Any, scales: Any): ...
    def getFullyQualifiedOutputId(self, ccdName: Any, butler: Any, outputId: Any): ...
    def combine(self, cache: Any, struct: Any, outputId: Any): ...
    def calculateOutputHeaderFromRaws(self, butler: Any, calib: Any, dataIdList: Any, outputId: Any) -> None: ...
    def recordCalibInputs(self, butler: Any, calib: Any, dataIdList: Any, outputId: Any) -> None: ...
    def interpolateNans(self, image: Any) -> None: ...
    def write(self, butler: Any, exposure: Any, dataId: Any) -> None: ...
    def makeCameraImage(self, camera: Any, dataId: Any, calibs: Any): ...
    def checkCcdIdLists(self, ccdIdLists: Any): ...

class BiasConfig(CalibConfig): ...

class BiasTask(CalibTask):
    ConfigClass: Any = ...
    calibName: str = ...
    filterName: str = ...
    exposureTime: float = ...
    @classmethod
    def applyOverrides(cls, config: Any) -> None: ...

class DarkConfig(CalibConfig):
    doRepair: Any = ...
    psfFwhm: Any = ...
    psfSize: Any = ...
    crGrow: Any = ...
    repair: Any = ...
    def setDefaults(self) -> None: ...

class DarkTask(CalibTask):
    ConfigClass: Any = ...
    calibName: str = ...
    filterName: str = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def applyOverrides(cls, config: Any) -> None: ...
    def processSingle(self, sensorRef: Any): ...
    def getDarkTime(self, exposure: Any): ...

class FlatConfig(CalibConfig):
    iterations: Any = ...
    stats: Any = ...

class FlatTask(CalibTask):
    ConfigClass: Any = ...
    calibName: str = ...
    @classmethod
    def applyOverrides(cls, config: Any) -> None: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def processResult(self, exposure: Any): ...
    def scale(self, ccdIdLists: Any, data: Any): ...

class FringeConfig(CalibConfig):
    stats: Any = ...
    subtractBackground: Any = ...
    detection: Any = ...
    detectSigma: Any = ...
    def setDefaults(self) -> None: ...

class FringeTask(CalibTask):
    ConfigClass: Any = ...
    calibName: str = ...
    @classmethod
    def applyOverrides(cls, config: Any) -> None: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def processSingle(self, sensorRef: Any): ...

class SkyConfig(CalibConfig):
    detectSigma: Any = ...
    maskObjects: Any = ...
    largeScaleBackground: Any = ...
    sky: Any = ...
    maskThresh: Any = ...
    mask: Any = ...

class SkyTask(CalibTask):
    ConfigClass: Any = ...
    calibName: str = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def scatterProcess(self, pool: Any, ccdIdLists: Any): ...
    def measureBackground(self, cache: Any, dataId: Any): ...
    def processSingleBackground(self, dataRef: Any): ...
    def processSingle(self, dataRef: Any, backgrounds: Any, scales: Any): ...
    def combine(self, cache: Any, struct: Any, outputId: Any): ...
