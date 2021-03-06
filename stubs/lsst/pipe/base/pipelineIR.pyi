import yaml
from typing import Any, Generator, List, MutableMapping, Optional, Set, Union

class PipelineYamlLoader(yaml.SafeLoader):
    def construct_mapping(self, node: Any, deep: bool = ...): ...

class ContractError(Exception): ...

class ContractIR:
    contract: str
    msg: Union[str, None] = ...
    def to_primitives(self) -> dict: ...
    def __eq__(self, other: ContractIR) -> Any: ...
    def __init__(self, contract: Any, msg: Any) -> None: ...

class LabeledSubset:
    label: str
    subset: Set[str]
    description: Optional[str]
    @staticmethod
    def from_primatives(label: str, value: Union[List[str], dict]) -> LabeledSubset: ...
    def to_primitives(self) -> dict: ...
    def __init__(self, label: Any, subset: Any, description: Any) -> None: ...

class ParametersIR:
    mapping: MutableMapping[str, str]
    def update(self, other: Optional[ParametersIR]) -> Any: ...
    def to_primitives(self) -> MutableMapping[str, str]: ...
    def __contains__(self, value: str) -> bool: ...
    def __getitem__(self, item: str) -> Any: ...
    def __bool__(self) -> bool: ...
    def __init__(self, mapping: Any) -> None: ...

class ConfigIR:
    python: Union[str, None] = ...
    dataId: Union[dict, None] = ...
    file: List[str] = ...
    rest: dict = ...
    def to_primitives(self) -> dict: ...
    def formatted(self, parameters: ParametersIR) -> ConfigIR: ...
    def maybe_merge(self, other_config: ConfigIR) -> Generator[ConfigIR, None, None]: ...
    def __eq__(self, other: ConfigIR) -> Any: ...
    def __init__(self, python: Any, dataId: Any, file: Any, rest: Any) -> None: ...

class TaskIR:
    label: str
    klass: str
    config: Union[List[ConfigIR], None] = ...
    def to_primitives(self) -> dict: ...
    def add_or_update_config(self, other_config: ConfigIR) -> Any: ...
    def __eq__(self, other: TaskIR) -> Any: ...
    def __init__(self, label: Any, klass: Any, config: Any) -> None: ...

class InheritIR:
    location: str
    include: Union[List[str], None] = ...
    exclude: Union[List[str], None] = ...
    importContracts: bool = ...
    def toPipelineIR(self, instrument: Any=...) -> PipelineIR: ...
    def __eq__(self, other: InheritIR) -> Any: ...
    def __init__(self, location: Any, include: Any, exclude: Any, importContracts: Any) -> None: ...

class PipelineIR:
    description: Any = ...
    instrument: Any = ...
    def __init__(self, loaded_yaml: Any) -> None: ...
    def subset_from_labels(self, labelSpecifier: Set[str]) -> PipelineIR: ...
    @classmethod
    def from_string(cls: Any, pipeline_string: str) -> Any: ...
    @classmethod
    def from_file(cls: Any, filename: str) -> Any: ...
    def to_file(self, filename: str) -> Any: ...
    def to_primitives(self): ...
    def __eq__(self, other: PipelineIR) -> Any: ...
