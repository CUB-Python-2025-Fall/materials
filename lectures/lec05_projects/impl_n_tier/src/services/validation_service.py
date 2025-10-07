from src.domain.entities.tool import Tool
from src.domain.value_objects.contact_info import ContactInfo
from src.domain.exceptions.domain_exceptions import InvalidToolDataException, InvalidContactInfoException

class ValidationService:
    """Service for business validation rules"""
    
    @staticmethod
    def validate_tool_data(name: str, description: str, contact_name: str, 
                          phone: str, email: str, photo: str = "") -> None:
        """Validate tool input data"""
        if not name or not name.strip():
            raise InvalidToolDataException("Tool name cannot be empty")
        
        if not description or not description.strip():
            raise InvalidToolDataException("Tool description cannot be empty")
        
        if not contact_name or not contact_name.strip():
            raise InvalidContactInfoException("Contact name cannot be empty")
        
        if not phone.strip() and not email.strip():
            raise InvalidContactInfoException("At least one contact method is required")
    
    @staticmethod
    def create_validated_tool(name: str, description: str, contact_name: str,
                            phone: str, email: str, photo: str = "") -> Tool:
        """Create a validated tool instance"""
        ValidationService.validate_tool_data(name, description, contact_name, phone, email, photo)
        
        contact_info = ContactInfo(contact_name, phone, email)
        return Tool(name, description, contact_info, photo)