from .. import Butler as Butler, PurgeUnsupportedPruneCollectionsError as PurgeUnsupportedPruneCollectionsError, PurgeWithoutUnstorePruneCollectionsError as PurgeWithoutUnstorePruneCollectionsError, RunWithoutPurgePruneCollectionsError as RunWithoutPurgePruneCollectionsError
from typing import Any

def pruneCollection(repo: Any, collection: Any, purge: Any, unstore: Any) -> None: ...
