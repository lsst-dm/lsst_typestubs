from ..pipeline import TaskDef
from lsst.daf.butler import Quantum
from typing import Any

BuildId: Any

class NodeId:
    number: int
    buildId: BuildId
    def __init__(self, number: Any, buildId: Any) -> None: ...

class QuantumNode:
    quantum: Quantum
    taskDef: TaskDef
    nodeId: NodeId
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __init__(self, quantum: Any, taskDef: Any, nodeId: Any) -> None: ...
