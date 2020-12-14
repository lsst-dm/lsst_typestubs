import abc
from ..tasks.metricTask import MetricTask as Gen3MetricTask

class MetricTask(Gen3MetricTask, metaclass=abc.ABCMeta): ...
