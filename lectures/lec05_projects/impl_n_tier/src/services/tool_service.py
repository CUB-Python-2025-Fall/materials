from typing import List
from src.domain.entities.tool import Tool
from src.domain.value_objects.contact_info import ContactInfo
from src.infrastructure.storage.storage_interface import StorageInterface
from src.services.validation_service import ValidationService
from src.services.search_service import SearchService

class ToolService:
    """Service for tool-related business operations"""
    
    def __init__(self, storage: StorageInterface):
        self.storage = storage
        self.validation_service = ValidationService()
        self.search_service = SearchService()
    
    def add_tool(self, name: str, description: str, contact_name: str,
                phone: str, email: str, photo: str = "") -> Tool:
        """Add a new tool to the system"""
        # Create validated tool
        tool = self.validation_service.create_validated_tool(
            name, description, contact_name, phone, email, photo
        )
        
        # Load existing tools
        tools = self.get_all_tools()
        
        # Add new tool
        tools.append(tool)
        
        # Save all tools
        self._save_tools(tools)
        
        return tool
    
    def get_all_tools(self) -> List[Tool]:
        """Get all tools from storage"""
        data = self.storage.load_data()
        return [Tool.from_dict(tool_data) for tool_data in data]
    
    def search_tools(self, search_term: str = "") -> List[Tool]:
        """Search for tools by name or description"""
        all_tools = self.get_all_tools()
        return self.search_service.search_tools(all_tools, search_term)
    
    def _save_tools(self, tools: List[Tool]) -> None:
        """Save tools to storage"""
        data = [tool.to_dict() for tool in tools]
        self.storage.save_data(data)