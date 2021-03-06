import lsst.pipe.base.connectionTypes as pipeBase
from lsst.ctrl.pool.parallel import BatchPoolTask
from typing import Any

class SkyCorrectionConnections(pipeBase.PipelineTaskConnections):
    rawLinker: Any = ...
    calExpArray: Any = ...
    calBkgArray: Any = ...
    camera: Any = ...
    skyCalibs: Any = ...
    calExpCamera: Any = ...
    skyCorr: Any = ...

class SkyCorrectionConfig(pipeBase.PipelineTaskConfig):
    bgModel: Any = ...
    bgModel2: Any = ...
    sky: Any = ...
    maskObjects: Any = ...
    doMaskObjects: Any = ...
    doBgModel: Any = ...
    doBgModel2: Any = ...
    doSky: Any = ...
    binning: Any = ...
    calexpType: Any = ...
    def setDefaults(self) -> None: ...

class SkyCorrectionTask(pipeBase.PipelineTask, BatchPoolTask):
    ConfigClass: Any = ...
    def runQuantum(self, butlerQC: Any, inputRefs: Any, outputRefs: Any) -> None: ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def batchWallTime(cls, time: Any, parsedCmd: Any, numCores: Any): ...
    def runDataRef(self, expRef: Any) -> None: ...
    def focalPlaneBackground(self, camera: Any, pool: Any, dataIdList: Any, config: Any): ...
    def focalPlaneBackgroundRun(self, camera: Any, cacheExposures: Any, idList: Any, config: Any): ...
    def run(self, calExpArray: Any, calBkgArray: Any, skyCalibs: Any, camera: Any): ...
    def loadImage(self, cache: Any, dataId: Any): ...
    def loadImageRun(self, calExp: Any, calExpBkg: Any): ...
    def measureSkyFrame(self, cache: Any, dataId: Any): ...
    def subtractSkyFrame(self, cache: Any, dataId: Any, scale: Any): ...
    def accumulateModel(self, cache: Any, data: Any): ...
    def subtractModel(self, cache: Any, dataId: Any, bgModel: Any): ...
    def subtractModelRun(self, exposure: Any, bgModel: Any): ...
    def realiseModel(self, cache: Any, dataId: Any, bgModel: Any): ...
    def collectBinnedImage(self, exposure: Any, image: Any): ...
    def collect(self, cache: Any): ...
    def collectOriginal(self, cache: Any, dataId: Any): ...
    def collectSky(self, cache: Any, dataId: Any): ...
    def collectMask(self, cache: Any, dataId: Any): ...
    def write(self, cache: Any, dataId: Any) -> None: ...
