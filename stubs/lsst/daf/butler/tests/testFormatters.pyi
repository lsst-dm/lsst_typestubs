from ..core import Formatter, Location
from ..formatters.yaml import YamlFormatter
from typing import Any, Mapping, Optional

class DoNothingFormatter(Formatter):
    def read(self, component: Optional[str]=...) -> Any: ...
    def write(self, inMemoryDataset: Any) -> str: ...

class FormatterTest(Formatter):
    supportedWriteParameters: Any = ...
    def read(self, component: Optional[str]=...) -> Any: ...
    def write(self, inMemoryDataset: Any) -> str: ...
    @staticmethod
    def validateWriteRecipes(recipes: Optional[Mapping[str, Any]]) -> Optional[Mapping[str, Any]]: ...

class SingleExtensionFormatter(DoNothingFormatter):
    extension: str = ...

class MultipleExtensionsFormatter(SingleExtensionFormatter):
    supportedExtensions: Any = ...

class LenientYamlFormatter(YamlFormatter):
    extension: str = ...
    @classmethod
    def validateExtension(cls: Any, location: Location) -> None: ...

class MetricsExampleFormatter(Formatter):
    extension: str = ...
    def read(self, component: Optional[Any] = ...): ...
    def write(self, inMemoryDataset: Any) -> str: ...

class MetricsExampleDataFormatter(Formatter):
    unsupportedParameters: Any = ...
    extension: str = ...
    def read(self, component: Optional[Any] = ...): ...
    def write(self, inMemoryDataset: Any) -> str: ...
