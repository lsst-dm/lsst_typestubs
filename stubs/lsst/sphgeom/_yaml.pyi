from ._sphgeom import Box as Box, Circle as Circle, ConvexPolygon as ConvexPolygon, Ellipse as Ellipse, HtmPixelization as HtmPixelization, Mq3cPixelization as Mq3cPixelization, Q3cPixelization as Q3cPixelization, Region as Region
from typing import Any

YamlLoaders: Any

def region_representer(dumper: Any, data: Any): ...
def region_constructor(loader: Any, node: Any): ...
def pixel_representer(dumper: Any, data: Any): ...
def pixel_constructor(loader: Any, node: Any): ...
