import lsst.log as pipeBase
from typing import Any, Optional

def countMaskedPixels(maskedIm: Any, maskPlane: Any): ...

class PairedVisitListTaskRunner(pipeBase.TaskRunner):
    @staticmethod
    def getTargetList(parsedCmd: Any, **kwargs: Any): ...

def parseCmdlineNumberString(inputString: Any): ...

class SingleVisitListTaskRunner(pipeBase.TaskRunner):
    @staticmethod
    def getTargetList(parsedCmd: Any, **kwargs: Any): ...

class NonexistentDatasetTaskDataIdContainer(pipeBase.DataIdContainer):
    def makeDataRefList(self, namespace: Any) -> None: ...

def checkExpLengthEqual(exp1: Any, exp2: Any, v1: Optional[Any] = ..., v2: Optional[Any] = ..., raiseWithMessage: bool = ...): ...
def ddict2dict(d: Any): ...
