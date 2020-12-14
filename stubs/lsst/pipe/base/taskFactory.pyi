from abc import ABCMeta, abstractmethod
from typing import Any

class TaskFactory(metaclass=ABCMeta):
    @abstractmethod
    def makeTask(self, taskClass: Any, config: Any, overrides: Any, butler: Any) -> Any: ...
