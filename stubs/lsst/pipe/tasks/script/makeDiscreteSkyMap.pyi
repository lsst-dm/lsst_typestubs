from lsst.daf.butler import Butler as Butler
from lsst.obs.base.utils import getInstrument as getInstrument
from lsst.pipe.tasks.makeDiscreteSkyMap import MakeDiscreteSkyMapConfig as MakeDiscreteSkyMapConfig, MakeDiscreteSkyMapTask as MakeDiscreteSkyMapTask
from lsst.skymap import BaseSkyMap as BaseSkyMap
from typing import Any, Optional

def makeDiscreteSkyMap(repo: Any, config_file: Any, collections: Any, instrument: Any, skymap_id: str = ..., old_skymap_id: Optional[Any] = ...) -> None: ...
