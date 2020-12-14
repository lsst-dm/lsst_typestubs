import abc
from abc import ABC, abstractmethod
from lsst.pipe.base import QuantumGraph

class ExecutionGraphFixup(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def fixupQuanta(self, graph: QuantumGraph) -> QuantumGraph: ...
