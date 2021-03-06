import abc
from typing import Any, Optional

class ButlerGetTests(metaclass=abc.ABCMeta):
    butler_get_data: Any = ...
    def setUp_butler_get(self, ccdExposureId_bits: Optional[Any] = ..., exposureIds: Optional[Any] = ..., filters: Optional[Any] = ..., exptimes: Optional[Any] = ..., detectorIds: Optional[Any] = ..., detector_names: Optional[Any] = ..., detector_serials: Optional[Any] = ..., dimensions: Optional[Any] = ..., sky_origin: Optional[Any] = ..., raw_subsets: Optional[Any] = ..., good_detectorIds: Optional[Any] = ..., bad_detectorIds: Optional[Any] = ..., linearizer_type: Optional[Any] = ..., raw_header_wcs: Optional[Any] = ...) -> None: ...
    def test_exposureId_bits(self) -> None: ...
    def test_raw(self) -> None: ...
    def test_bias(self) -> None: ...
    def test_dark(self) -> None: ...
    def test_flat(self) -> None: ...
    def test_raw_header_wcs(self) -> None: ...
    def test_raw_sub_bbox(self) -> None: ...
    def test_subset_raw(self) -> None: ...
    def test_get_linearizer(self) -> None: ...
    def test_get_linearizer_bad_detectorIds(self) -> None: ...
