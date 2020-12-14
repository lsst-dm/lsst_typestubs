from lsst.ip.isr import CrosstalkCalib as CrosstalkCalib, Defects as Defects, Linearizer as Linearizer
from lsst.meas.algorithms.simple_curve import Curve as Curve
from typing import Any

def read_one_chip(root: Any, chip_name: Any, chip_id: Any): ...
def check_metadata(obj: Any, valid_start: Any, instrument: Any, chip_id: Any, filepath: Any, data_name: Any) -> None: ...
def read_all(root: Any, camera: Any): ...
