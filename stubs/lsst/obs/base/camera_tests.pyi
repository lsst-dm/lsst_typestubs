import abc
from typing import Any, Optional

class CameraTests(metaclass=abc.ABCMeta):
    camera_data: Any = ...
    def setUp_camera(self, camera_name: Optional[Any] = ..., n_detectors: Optional[Any] = ..., first_detector_name: Optional[Any] = ..., plate_scale: Optional[Any] = ...) -> None: ...
    def test_iterable(self) -> None: ...
    def test_camera_butler(self) -> None: ...
    def test_plate_scale(self) -> None: ...
