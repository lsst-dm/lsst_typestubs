from .formatter import FormatterParameter
from .storageClass import StorageClass
from typing import Optional

class StoredDatastoreItemInfo: ...

class StoredFileInfo(StoredDatastoreItemInfo):
    def __init__(self, formatter: FormatterParameter, path: str, storageClass: StorageClass, component: Optional[str], checksum: Optional[str], file_size: int) -> None: ...
    formatter: str
    path: str
    storageClass: StorageClass
    component: Optional[str]
    checksum: Optional[str]
    file_size: int
