import urllib.parse
from ..datastore import DatastoreTransaction
from .utils import NoTransaction
from typing import Any, Iterator, Optional, Tuple, Union

class ButlerURI:
    transferModes: Tuple[str, ...] = ...
    transferDefault: str = ...
    quotePaths: bool = ...
    isLocal: bool = ...
    isTemporary: bool
    dirLike: Any = ...
    def __new__(cls: Any, uri: Union[str, urllib.parse.ParseResult, ButlerURI], root: Optional[Union[str, ButlerURI]]=..., forceAbsolute: bool=..., forceDirectory: bool=..., isTemporary: bool=...) -> ButlerURI: ...
    @property
    def scheme(self) -> str: ...
    @property
    def netloc(self) -> str: ...
    @property
    def path(self) -> str: ...
    @property
    def unquoted_path(self) -> str: ...
    @property
    def ospath(self) -> str: ...
    @property
    def relativeToPathRoot(self) -> str: ...
    @property
    def is_root(self) -> bool: ...
    @property
    def fragment(self) -> str: ...
    @property
    def params(self) -> str: ...
    @property
    def query(self) -> str: ...
    def geturl(self) -> str: ...
    def split(self) -> Tuple[ButlerURI, str]: ...
    def basename(self) -> str: ...
    def dirname(self) -> ButlerURI: ...
    def parent(self) -> ButlerURI: ...
    def replace(self, **kwargs: Any) -> ButlerURI: ...
    def updateFile(self, newfile: str) -> None: ...
    def updateExtension(self, ext: Optional[str]) -> None: ...
    def getExtension(self) -> str: ...
    def join(self, path: Union[str, ButlerURI]) -> ButlerURI: ...
    def relative_to(self, other: ButlerURI) -> Optional[str]: ...
    def exists(self) -> bool: ...
    def remove(self) -> None: ...
    def isabs(self) -> bool: ...
    def as_local(self) -> Iterator[ButlerURI]: ...
    def read(self, size: int=...) -> bytes: ...
    def write(self, data: bytes, overwrite: bool=...) -> None: ...
    def mkdir(self) -> None: ...
    def size(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __copy__(self) -> ButlerURI: ...
    def __deepcopy__(self, memo: Any) -> ButlerURI: ...
    def __getnewargs__(self) -> Tuple: ...
    def transfer_from(self, src: ButlerURI, transfer: str, overwrite: bool=..., transaction: Optional[Union[DatastoreTransaction, NoTransaction]]=...) -> None: ...
