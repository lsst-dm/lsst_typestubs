import yaml
from typing import Any, Optional

Loader = yaml.FullLoader
Loader = yaml.Loader

def read_test_file(filename: Any, dir: Optional[Any] = ...): ...

class MetadataAssertHelper:
    def assertCoordinatesConsistent(self, obsinfo: Any, max_sep: float = ..., amdelta: float = ...) -> None: ...
    def assertObservationInfoFromYaml(self, file: Any, dir: Optional[Any] = ..., check_wcs: bool = ..., wcs_params: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def assertObservationInfo(self, header: Any, filename: Optional[Any] = ..., check_wcs: bool = ..., wcs_params: Optional[Any] = ..., **kwargs: Any): ...