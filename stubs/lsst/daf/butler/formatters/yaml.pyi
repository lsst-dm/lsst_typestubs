from .file import FileFormatter
from typing import Any

class YamlFormatter(FileFormatter):
    extension: str = ...
    unsupportedParameters: Any = ...
    supportedWriteParameters: Any = ...
