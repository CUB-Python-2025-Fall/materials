class StorageException(Exception):
    """Base exception for storage operations"""
    pass

class DataLoadException(StorageException):
    """Raised when data cannot be loaded"""
    pass

class DataSaveException(StorageException):
    """Raised when data cannot be saved"""
    pass