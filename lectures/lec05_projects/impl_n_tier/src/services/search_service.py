from typing import List
from src.domain.entities.tool import Tool

class SearchService:
    """Service for search and filtering operations"""
    
    @staticmethod
    def search_tools(tools: List[Tool], search_term: str) -> List[Tool]:
        """Search tools by name or description"""
        if not search_term:
            return tools
        
        return [tool for tool in tools if tool.matches_search(search_term)]
    
    @staticmethod
    def sort_tools_by_date(tools: List[Tool], reverse: bool = True) -> List[Tool]:
        """Sort tools by date added"""
        return sorted(tools, key=lambda t: t.date_added, reverse=reverse)
    
    @staticmethod
    def sort_tools_by_name(tools: List[Tool]) -> List[Tool]:
        """Sort tools alphabetically by name"""
        return sorted(tools, key=lambda t: t.name.lower())