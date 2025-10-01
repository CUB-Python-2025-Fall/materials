from src.domain.exceptions.domain_exceptions import InvalidContactInfoException

class ContactInfo:
    """Value object for contact information"""
    
    def __init__(self, name: str, phone: str = "", email: str = ""):
        if not name or not name.strip():
            raise InvalidContactInfoException("Contact name is required")
        
        if not phone.strip() and not email.strip():
            raise InvalidContactInfoException("At least one contact method (phone or email) is required")
        
        self.name = name.strip()
        self.phone = phone.strip()
        self.email = email.strip()
    
    def to_dict(self):
        """Convert to dictionary for serialization"""
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create from dictionary"""
        return cls(
            name=data.get("name", ""),
            phone=data.get("phone", ""),
            email=data.get("email", "")
        )
    
    def __str__(self):
        contact_methods = []
        if self.phone:
            contact_methods.append(f"Phone: {self.phone}")
        if self.email:
            contact_methods.append(f"Email: {self.email}")
        return f"{self.name} ({', '.join(contact_methods)})"