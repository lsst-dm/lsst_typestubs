from typing import Any, Optional

def getComparisonName(name1: Any, name2: Any): ...
def compareScalars(name: Any, v1: Any, v2: Any, output: Any, rtol: float = ..., atol: float = ..., dtype: Optional[Any] = ...): ...
def compareConfigs(name: Any, c1: Any, c2: Any, shortcut: bool = ..., rtol: float = ..., atol: float = ..., output: Optional[Any] = ...): ...
