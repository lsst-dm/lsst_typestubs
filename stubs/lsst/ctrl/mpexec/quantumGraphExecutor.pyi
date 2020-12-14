import abc
from abc import ABC, abstractmethod
from typing import Any

class QuantumExecutor(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def execute(self, taskDef: Any, quantum: Any, butler: Any) -> Any: ...

class QuantumGraphExecutor(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def execute(self, graph: Any, butler: Any) -> Any: ...
