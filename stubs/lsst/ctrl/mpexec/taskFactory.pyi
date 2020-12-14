from lsst.pipe.base import TaskFactory as BaseTaskFactory
from typing import Any

class TaskFactory(BaseTaskFactory):
    def makeTask(self, taskClass: Any, config: Any, overrides: Any, butler: Any): ...
