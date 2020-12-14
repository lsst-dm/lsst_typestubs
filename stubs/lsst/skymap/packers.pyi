from lsst.daf.butler import DataCoordinate, DimensionGraph, DimensionPacker
from typing import Any

class SkyMapDimensionPacker(DimensionPacker):
    SUPPORTED_FILTERS: Any = ...
    @classmethod
    def getIntFromFilter(cls, name: Any): ...
    @classmethod
    def getFilterNameFromInt(cls, num: Any): ...
    @classmethod
    def getMaxIntForFilters(cls): ...
    @classmethod
    def configure(cls, dimensions: Any): ...
    def __init__(self, fixed: DataCoordinate, dimensions: DimensionGraph) -> None: ...
    @property
    def maxBits(self) -> int: ...
    def unpack(self, packedId: int) -> DataCoordinate: ...
