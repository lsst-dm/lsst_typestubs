from .jsonmixin import JsonSerializationMixin
from typing import Any, Optional

class MetricSet(JsonSerializationMixin):
    def __init__(self, metrics: Optional[Any] = ...) -> None: ...
    @classmethod
    def load_metrics_package(cls, package_name_or_path: str = ..., subset: Optional[Any] = ...): ...
    @classmethod
    def load_single_package(cls, metrics_yaml_path: Any): ...
    @classmethod
    def deserialize(cls, metrics: Optional[Any] = ...): ...
    @property
    def json(self): ...
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def __len__(self): ...
    def __contains__(self, key: Any): ...
    def __iter__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __iadd__(self, other: Any): ...
    def insert(self, metric: Any) -> None: ...
    def keys(self): ...
    def items(self) -> None: ...
    def subset(self, package: Optional[Any] = ..., tags: Optional[Any] = ...): ...
    def update(self, other: Any) -> None: ...
