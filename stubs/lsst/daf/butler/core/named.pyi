import abc
from abc import abstractmethod
from typing import AbstractSet, Any, Dict, ItemsView, Iterable, Iterator, KeysView, Mapping, MutableMapping, MutableSet, TypeVar, Union, ValuesView

class Named:
    @property
    def name(self) -> str: ...
Named = Any
K = TypeVar('K', bound=Named)
K_co = TypeVar('K_co', bound=Named, covariant=True)
V = TypeVar('V')
V_co = TypeVar('V_co', covariant=True)

class NamedKeyMapping(Mapping[K_co, V_co], metaclass=abc.ABCMeta):
    @property
    @abstractmethod
    def names(self) -> AbstractSet[str]: ...
    def byName(self) -> Dict[str, V_co]: ...
    @abstractmethod
    def keys(self) -> NamedValueAbstractSet[K_co]: ...
    @abstractmethod
    def __getitem__(self, key: Union[str, K_co]) -> V_co: ...
    def get(self, key: Union[str, K_co], default: Any=...) -> Any: ...
NameLookupMapping = Union[NamedKeyMapping[K_co, V_co], Mapping[str, V_co]]

class NamedKeyMutableMapping(NamedKeyMapping[K, V], MutableMapping[K, V], metaclass=abc.ABCMeta):
    @abstractmethod
    def __setitem__(self, key: Union[str, K], value: V) -> None: ...
    @abstractmethod
    def __delitem__(self, key: Union[str, K]) -> None: ...
    def pop(self, key: Union[str, K], default: Any=...) -> Any: ...

class NamedKeyDict(NamedKeyMutableMapping[K, V]):
    def __init__(self, *args: Any) -> None: ...
    @property
    def names(self) -> KeysView[str]: ...
    def byName(self) -> Dict[str, V]: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[K]: ...
    def __getitem__(self, key: Union[str, K]) -> V: ...
    def __setitem__(self, key: Union[str, K], value: V) -> None: ...
    def __delitem__(self, key: Union[str, K]) -> None: ...
    def keys(self) -> NamedValueAbstractSet[K]: ...
    def values(self) -> ValuesView[V]: ...
    def items(self) -> ItemsView[K, V]: ...
    def copy(self) -> NamedKeyDict[K, V]: ...
    def freeze(self) -> NamedKeyMapping[K, V]: ...

class NamedValueAbstractSet(AbstractSet[K_co], metaclass=abc.ABCMeta):
    @property
    @abstractmethod
    def names(self) -> AbstractSet[str]: ...
    @abstractmethod
    def asMapping(self) -> Mapping[str, K_co]: ...
    @abstractmethod
    def __getitem__(self, key: Union[str, K_co]) -> K_co: ...
    def get(self, key: Union[str, K_co], default: Any=...) -> Any: ...

class NameMappingSetView(NamedValueAbstractSet[K_co]):
    def __init__(self, mapping: Mapping[str, K_co]) -> None: ...
    @property
    def names(self) -> AbstractSet[str]: ...
    def asMapping(self) -> Mapping[str, K_co]: ...
    def __getitem__(self, key: Union[str, K_co]) -> K_co: ...
    def __contains__(self, key: Any) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[K_co]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __le__(self, other: AbstractSet[K]) -> bool: ...
    def __ge__(self, other: AbstractSet[K]) -> bool: ...

class NamedValueMutableSet(NamedValueAbstractSet[K], MutableSet[K], metaclass=abc.ABCMeta):
    @abstractmethod
    def __delitem__(self, name: str) -> None: ...
    @abstractmethod
    def remove(self, element: Union[str, K]) -> Any: ...
    @abstractmethod
    def discard(self, element: Union[str, K]) -> Any: ...
    @abstractmethod
    def pop(self, *args: str) -> K: ...

class NamedValueSet(NameMappingSetView[K], NamedValueMutableSet[K]):
    def __init__(self, elements: Iterable[K]=...) -> None: ...
    def issubset(self, other: AbstractSet[K]) -> bool: ...
    def issuperset(self, other: AbstractSet[K]) -> bool: ...
    def __delitem__(self, name: str) -> None: ...
    def add(self, element: K) -> None: ...
    def remove(self, element: Union[str, K]) -> Any: ...
    def discard(self, element: Union[str, K]) -> Any: ...
    def pop(self, *args: str) -> K: ...
    def update(self, elements: Iterable[K]) -> None: ...
    def copy(self) -> NamedValueSet[K]: ...
    def freeze(self) -> NamedValueAbstractSet[K]: ...