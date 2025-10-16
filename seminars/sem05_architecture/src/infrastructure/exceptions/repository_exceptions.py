class DocumentRepositoryError(Exception):
    """Base class for all document repository exceptions."""
    pass

class DocumentExistsError(DocumentRepositoryError):
    """Raised when trying to add a document with an existing id."""
    pass

class DocumentNotFoundError(DocumentRepositoryError):
    """Raised when a document with the specified id is not found."""
    pass

class VectorRepositoryError(Exception):
    """Base class for all vector repository exceptions."""
    pass

class VectorExistsError(VectorRepositoryError):
    """Raised when trying to add a vector with an existing id."""
    pass

class VectorNotFoundError(VectorRepositoryError):
    """Raised when a vector with the specified id is not found."""
    pass
