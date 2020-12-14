import lsst.log as pipeBase
from typing import Any

class TractCheckDataIdContainer(pipeBase.DataIdContainer):
    def castDataIds(self, butler: Any) -> None: ...
    def makeDataRefList(self, namespace: Any) -> None: ...