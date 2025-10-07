class UIException(Exception):
    """Base exception for UI layer"""
    pass

class UserInputException(UIException):
    """Raised when user input is invalid"""
    pass

class DisplayException(UIException):
    """Raised when there's an issue with displaying data"""
    pass