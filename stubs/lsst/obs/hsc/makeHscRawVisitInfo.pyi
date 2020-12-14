from lsst.obs.base import MakeRawVisitInfoViaObsInfo
from typing import Any

class MakeHscRawVisitInfo(MakeRawVisitInfoViaObsInfo):
    metadataTranslator: Any = ...
