from .file import ButlerFileURI

class ButlerSchemelessURI(ButlerFileURI):
    quotePaths: bool = ...
    @property
    def ospath(self) -> str: ...
    def isabs(self) -> bool: ...
