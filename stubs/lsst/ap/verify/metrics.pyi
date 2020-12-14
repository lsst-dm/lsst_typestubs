import argparse
import collections
from typing import Any

class MetricsParser(argparse.ArgumentParser):
    def __init__(self) -> None: ...

class _OptionalFormatDict(collections.UserDict):
    def __missing__(self, key: Any): ...

def computeMetrics(workspace: Any, dataIds: Any, args: Any) -> None: ...
