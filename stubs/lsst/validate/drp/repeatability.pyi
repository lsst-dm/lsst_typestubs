from lsst.verify import Datum as Datum, Measurement as Measurement
from typing import Any

thousandDivSqrtTwo: Any

def measurePhotRepeat(metric: Any, filterName: Any, *args: Any, **kwargs: Any): ...
def calcPhotRepeat(matches: Any, magKey: Any, numRandomShuffles: int = ...): ...
def calcPhotRepeatSample(matches: Any, magKey: Any): ...
def getRandomDiffRmsInMmags(array: Any): ...
def getRandomDiff(array: Any): ...
def computeWidths(array: Any): ...
