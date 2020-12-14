from lsst.daf.butler import Butler as Butler
from lsst.daf.butler.core.utils import findFileResources as findFileResources
from lsst.pipe.base.configOverrides import ConfigOverrides as ConfigOverrides
from lsst.utils import doImport as doImport
from typing import Any, Optional

def ingestRaws(repo: Any, locations: Any, regex: Any, output_run: Any, config: Optional[Any] = ..., config_file: Optional[Any] = ..., transfer: str = ..., processes: int = ..., ingest_task: str = ...) -> None: ...
