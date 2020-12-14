from .fileDatastore import FileDatastore

class S3Datastore(FileDatastore):
    defaultConfigFile: str = ...
