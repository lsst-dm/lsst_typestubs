import lsst.meas.algorithms as pexConfig
import lsst.meas.algorithms as pipeBase
from typing import Any, Optional

class CoaddBaseConfig(pexConfig.Config):
    coaddName: Any = ...
    select: Any = ...
    badMaskPlanes: Any = ...
    inputRecorder: Any = ...
    doPsfMatch: Any = ...
    modelPsf: Any = ...
    doApplyUberCal: Any = ...
    doApplyExternalPhotoCalib: Any = ...
    externalPhotoCalibName: Any = ...
    doApplyExternalSkyWcs: Any = ...
    externalSkyWcsName: Any = ...
    includeCalibVar: Any = ...
    matchingKernelSize: Any = ...

class CoaddTaskRunner(pipeBase.TaskRunner):
    @staticmethod
    def getTargetList(parsedCmd: Any, **kwargs: Any): ...

class CoaddBaseTask(pipeBase.CmdLineTask):
    ConfigClass: Any = ...
    RunnerClass: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def selectExposures(self, patchRef: Any, skyInfo: Optional[Any] = ..., selectDataList: Any = ...): ...
    def getSkyInfo(self, patchRef: Any): ...
    def getCoaddDatasetName(self, warpType: str = ...): ...
    def getTempExpDatasetName(self, warpType: str = ...): ...
    def getBadPixelMask(self): ...

class SelectDataIdContainer(pipeBase.DataIdContainer):
    dataList: Any = ...
    def makeDataRefList(self, namespace: Any) -> None: ...

def getSkyInfo(coaddName: Any, patchRef: Any): ...
def makeSkyInfo(skyMap: Any, tractId: Any, patchId: Any): ...
def makeCoaddSuffix(warpType: str = ...): ...