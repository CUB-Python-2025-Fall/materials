class DomainException(Exception):
    """Base exception for domain layer"""
    pass

class InvalidToolDataException(DomainException):
    """Raised when tool data violates business rules"""
    pass

class InvalidContactInfoException(DomainException):
    """Raised when contact information is invalid"""
    pass