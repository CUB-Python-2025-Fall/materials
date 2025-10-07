import json
import os
from typing import List, Dict, Any
from src.infrastructure.storage.storage_interface import StorageInterface
from src.infrastructure.exceptions.storage_exceptions import DataLoadException, DataSaveException

class JsonStorage(StorageInterface):
    """JSON file storage implementation"""
    
    def __init__(self, file_path: str = "tools.json"):
        self.file_path = file_path
    
    def load_data(self) -> List[Dict[str, Any]]:
        """Load tools from JSON file"""
        if not os.path.exists(self.file_path):
            return []
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            raise DataLoadException(f"Failed to load data from {self.file_path}: {str(e)}")
    
    def save_data(self, data: List[Dict[str, Any]]) -> None:
        """Save tools to JSON file"""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except IOError as e:
            raise DataSaveException(f"Failed to save data to {self.file_path}: {str(e)}")