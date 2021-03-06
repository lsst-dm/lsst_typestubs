from typing import Any

class Timer:
    def __init__(self, name: str = ..., doPrint: bool = ...) -> None: ...
    def start(self): ...
    def stop(self): ...
    def dump(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any): ...
