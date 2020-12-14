from ._butlerUri import ButlerURI

class ButlerInMemoryURI(ButlerURI):
    def exists(self) -> bool: ...
