import lsst.pex.exceptions
from lsst.obs.base.ingest import RawFileData
from lsst.pipe.tasks.ingest import ParseTask
from typing import Any

class MegaPrimeRawIngestTask(lsst.obs.base.RawIngestTask):
    def extractMetadata(self, filename: str) -> RawFileData: ...

class MegacamParseTask(ParseTask):
    def translate_ccd(self, md: Any): ...
    def translate_filter(self, md: Any): ...
    def translate_taiObs(self, md: Any): ...
    def translate_defects(self, md: Any): ...
    def getInfo(self, filename: Any): ...
    def getExtensionName(self, md: Any): ...
