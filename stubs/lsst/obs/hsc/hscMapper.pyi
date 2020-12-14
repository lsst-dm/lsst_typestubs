from .hscFilters import HSC_FILTER_DEFINITIONS as HSC_FILTER_DEFINITIONS
from .hscPupil import HscPupilFactory as HscPupilFactory
from .makeHscRawVisitInfo import MakeHscRawVisitInfo as MakeHscRawVisitInfo
from lsst.daf.persistence import ButlerLocation as ButlerLocation, Policy as Policy
from lsst.ip.isr import Linearizer as Linearizer
from lsst.obs.base import CameraMapper as CameraMapper
from typing import Any

class HscMapper(CameraMapper):
    packageName: str = ...
    MakeRawVisitInfoClass: Any = ...
    PupilFactoryClass: Any = ...
    @classmethod
    def addFilters(cls) -> None: ...
    filters: Any = ...
    defaultFilterName: str = ...
    def __init__(self, **kwargs: Any) -> None: ...
    @classmethod
    def clearCache(cls) -> None: ...
    def map(self, datasetType: Any, dataId: Any, write: bool = ...): ...
    def std_raw_md(self, md: Any, dataId: Any): ...
    def std_dark(self, item: Any, dataId: Any): ...
    def bypass_ccdExposureId(self, datasetType: Any, pythonType: Any, location: Any, dataId: Any): ...
    def bypass_ccdExposureId_bits(self, datasetType: Any, pythonType: Any, location: Any, dataId: Any): ...
    def map_linearizer(self, dataId: Any, write: bool = ...): ...
    def map_crosstalk(self, dataId: Any, write: bool = ...) -> None: ...
    def bypass_linearizer(self, datasetType: Any, pythonType: Any, butlerLocation: Any, dataId: Any): ...
    def bypass_deepCoaddId_bits(self, *args: Any, **kwargs: Any): ...
    def bypass_deepCoaddId(self, datasetType: Any, pythonType: Any, location: Any, dataId: Any): ...
    def bypass_deepMergedCoaddId_bits(self, *args: Any, **kwargs: Any): ...
    def bypass_deepMergedCoaddId(self, datasetType: Any, pythonType: Any, location: Any, dataId: Any): ...
    def map_psf(self, dataId: Any, write: bool = ...): ...
    def std_psf(self, calexp: Any, dataId: Any): ...
    @classmethod
    def getCameraName(cls): ...
