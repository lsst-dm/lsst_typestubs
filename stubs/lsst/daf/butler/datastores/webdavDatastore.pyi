from .fileDatastore import FileDatastore

class WebdavDatastore(FileDatastore):
    defaultConfigFile: str = ...
