from lsst.pipe.base import Struct as Struct, TaskRunner as TaskRunner
from lsst.pipe.tasks.coaddBase import CoaddDataIdContainer as CoaddDataIdContainer
from lsst.pipe.tasks.selectImages import BaseExposureInfo as BaseExposureInfo, BaseSelectImagesTask as BaseSelectImagesTask
from typing import Any

class ButlerTaskRunner(TaskRunner):
    @staticmethod
    def getTargetList(parsedCmd: Any, **kwargs: Any): ...

def getDataRef(butler: Any, dataId: Any, datasetType: str = ...): ...

class NullSelectImagesTask(BaseSelectImagesTask):
    def runDataRef(self, patchRef: Any, coordList: Any, makeDataRefList: bool = ..., selectDataList: Any = ...): ...

class TractDataIdContainer(CoaddDataIdContainer):
    refList: Any = ...
    def makeDataRefList(self, namespace: Any): ...
