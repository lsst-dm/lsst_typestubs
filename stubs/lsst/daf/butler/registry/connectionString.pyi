from ._config import RegistryConfig
from sqlalchemy.engine import url
from typing import Any

DB_AUTH_ENVVAR: str
DB_AUTH_PATH: str

class ConnectionStringFactory:
    keys: Any = ...
    @classmethod
    def fromConfig(cls: Any, registryConfig: RegistryConfig) -> url.URL: ...
