from lsst.obs.base import MakeRawVisitInfoViaObsInfo
from typing import Any

class MakeDecamRawVisitInfo(MakeRawVisitInfoViaObsInfo):
    metadataTranslator: Any = ...
