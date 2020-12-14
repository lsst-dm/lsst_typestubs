from .fileDatastore import FileDatastore
from typing import ClassVar, Optional

class PosixDatastore(FileDatastore):
    defaultConfigFile: ClassVar[Optional[str]] = ...
