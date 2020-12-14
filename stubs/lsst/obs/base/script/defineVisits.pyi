from ..utils import getInstrument as getInstrument
from lsst.daf.butler import Butler as Butler
from lsst.obs.base import DefineVisitsConfig as DefineVisitsConfig, DefineVisitsTask as DefineVisitsTask
from typing import Any

def defineVisits(repo: Any, config_file: Any, collections: Any, instrument: Any, processes: int = ...) -> None: ...
