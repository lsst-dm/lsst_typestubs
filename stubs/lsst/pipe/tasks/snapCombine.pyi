import lsst.meas.algorithms as pexConfig
import lsst.meas.algorithms as pipeBase
from .repair import RepairTask as RepairTask
from lsst.afw.display import getDisplay as getDisplay
from lsst.coadd.utils import addToCoadd as addToCoadd, setCoaddEdgeBits as setCoaddEdgeBits
from lsst.ip.diffim import SnapPsfMatchTask as SnapPsfMatchTask
from lsst.meas.algorithms import SourceDetectionTask as SourceDetectionTask
from lsst.meas.base import SingleFrameMeasurementTask as SingleFrameMeasurementTask
from typing import Any, Optional

class InitialPsfConfig(pexConfig.Config):
    model: Any = ...
    pixelScale: Any = ...
    fwhm: Any = ...
    size: Any = ...

class SnapCombineConfig(pexConfig.Config):
    doRepair: Any = ...
    repairPsfFwhm: Any = ...
    doDiffIm: Any = ...
    doPsfMatch: Any = ...
    doMeasurement: Any = ...
    badMaskPlanes: Any = ...
    averageKeys: Any = ...
    sumKeys: Any = ...
    repair: Any = ...
    diffim: Any = ...
    detection: Any = ...
    initialPsf: Any = ...
    measurement: Any = ...
    def setDefaults(self) -> None: ...
    def validate(self) -> None: ...

class SnapCombineTask(pipeBase.Task):
    ConfigClass: Any = ...
    schema: Any = ...
    algMetadata: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def run(self, snap0: Any, snap1: Any, defects: Optional[Any] = ...): ...
    def addSnaps(self, snap0: Any, snap1: Any): ...
    def fixMetadata(self, combinedMetadata: Any, metadata0: Any, metadata1: Any) -> None: ...
    def makeInitialPsf(self, exposure: Any, fwhmPix: Optional[Any] = ...): ...