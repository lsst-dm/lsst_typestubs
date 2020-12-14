from lsst.obs.base import MakeRawVisitInfoViaObsInfo
from typing import Any

class MakeMegacamRawVisitInfo(MakeRawVisitInfoViaObsInfo):
    metadataTranslator: Any = ...
