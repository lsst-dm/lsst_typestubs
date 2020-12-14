from .._topology import TopologicalFamily, TopologicalSpace
from ..named import NamedValueAbstractSet
from ._elements import Dimension, DimensionElement
from ._governor import GovernorDimension
from ._universe import DimensionUniverse
from typing import AbstractSet, Any, Iterable, Iterator, Mapping, Optional, Tuple, Union

class DimensionGraph:
    universe: Any = ...
    dimensions: Any = ...
    elements: Any = ...
    def __new__(cls: Any, universe: DimensionUniverse, dimensions: Optional[Iterable[Dimension]]=..., names: Optional[Iterable[str]]=..., conform: bool=...) -> DimensionGraph: ...
    def __getnewargs__(self) -> tuple: ...
    def __deepcopy__(self, memo: dict) -> DimensionGraph: ...
    @property
    def names(self) -> AbstractSet[str]: ...
    def __iter__(self) -> Iterator[Dimension]: ...
    def __len__(self) -> int: ...
    def __contains__(self, element: Union[str, DimensionElement]) -> bool: ...
    def __getitem__(self, name: str) -> DimensionElement: ...
    def get(self, name: str, default: Any=...) -> DimensionElement: ...
    def isdisjoint(self, other: DimensionGraph) -> bool: ...
    def issubset(self, other: DimensionGraph) -> bool: ...
    def issuperset(self, other: DimensionGraph) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: DimensionGraph) -> bool: ...
    def __ge__(self, other: DimensionGraph) -> bool: ...
    def __lt__(self, other: DimensionGraph) -> bool: ...
    def __gt__(self, other: DimensionGraph) -> bool: ...
    def union(self, *others: DimensionGraph) -> DimensionGraph: ...
    def intersection(self, *others: DimensionGraph) -> DimensionGraph: ...
    def __or__(self, other: DimensionGraph) -> DimensionGraph: ...
    def __and__(self, other: DimensionGraph) -> DimensionGraph: ...
    @property
    def primaryKeyTraversalOrder(self) -> Tuple[DimensionElement, ...]: ...
    @property
    def spatial(self) -> NamedValueAbstractSet[TopologicalFamily]: ...
    @property
    def temporal(self) -> NamedValueAbstractSet[TopologicalFamily]: ...
    governors: NamedValueAbstractSet[GovernorDimension]
    required: NamedValueAbstractSet[Dimension]
    implied: NamedValueAbstractSet[Dimension]
    topology: Mapping[TopologicalSpace, NamedValueAbstractSet[TopologicalFamily]]
