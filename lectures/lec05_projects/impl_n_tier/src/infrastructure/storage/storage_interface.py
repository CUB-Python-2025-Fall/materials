from abc import ABC, abstractmethod
from typing import List, Dict, Any

class StorageInterface(ABC):
    """Abstract interface for data storage"""
    
    @abstractmethod
    def load_data(self) -> List[Dict[str, Any]]:
        """Load all tools data"""
        pass
    
    @abstractmethod
    def save_data(self, data: List[Dict[str, Any]]) -> None:
        """Save tools data"""
        pass