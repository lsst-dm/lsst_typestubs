import abc
from typing import Any

class JsonSerializationMixin(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def json(self) -> Any: ...
    @staticmethod
    def jsonify_dict(d: Any): ...
    def write_json(self, filepath: Any) -> None: ...
