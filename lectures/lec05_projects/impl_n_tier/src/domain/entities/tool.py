from datetime import datetime
from src.domain.value_objects.contact_info import ContactInfo
from src.domain.exceptions.domain_exceptions import InvalidToolDataException

class Tool:
    """Tool entity representing a shareable tool"""
    
    def __init__(self, name: str, description: str, contact_info: ContactInfo, 
                 photo: str = "", tool_id: str = None, date_added: str = None):
        if not name or not name.strip():
            raise InvalidToolDataException("Tool name is required")
        
        if not description or not description.strip():
            raise InvalidToolDataException("Tool description is required")
        
        self.id = tool_id or self._generate_id()
        self.name = name.strip()
        self.description = description.strip()
        self.photo = photo.strip()
        self.contact_info = contact_info
        self.date_added = date_added or datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def _generate_id(self) -> str:
        """Generate unique ID for the tool"""
        return datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    
    def to_dict(self):
        """Convert tool to dictionary for serialization"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "photo": self.photo,
            "contact_info": self.contact_info.to_dict(),
            "date_added": self.date_added
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create tool from dictionary"""
        contact_info = ContactInfo.from_dict(data.get("contact_info", {}))
        return cls(
            name=data.get("name", ""),
            description=data.get("description", ""),
            contact_info=contact_info,
            photo=data.get("photo", ""),
            tool_id=data.get("id"),
            date_added=data.get("date_added")
        )
    
    def matches_search(self, search_term: str) -> bool:
        """Check if tool matches search term"""
        if not search_term:
            return True
        
        search_term = search_term.lower()
        return (search_term in self.name.lower() or 
                search_term in self.description.lower())
    
    def __str__(self):
        return f"{self.name}: {self.description}"