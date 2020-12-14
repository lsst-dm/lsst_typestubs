from ..utils import MWOptionDecorator as MWOptionDecorator, split_commas as split_commas, split_kv as split_kv, unwrap as unwrap, yaml_presets as yaml_presets
from lsst.daf.butler.registry import CollectionType as CollectionType
from typing import Any

class CollectionTypeCallback:
    collectionTypes: Any = ...
    @staticmethod
    def makeCollectionTypes(context: Any, param: Any, value: Any): ...

collection_type_option: Any
collections_option: Any
components_option: Any
config_option: Any
config_file_option: Any
dataset_type_option: Any
datasets_option: Any
logLevelChoices: Any
log_level_option: Any
long_log_option: Any
options_file_option: Any
processes_option: Any
regex_option: Any
run_option: Any
transfer_option: Any
verbose_option: Any
where_option: Any
