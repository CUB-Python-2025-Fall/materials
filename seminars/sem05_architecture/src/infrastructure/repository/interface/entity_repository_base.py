from abc import ABC, abstractmethod
from typing import Any

class EntityRepositoryBase(ABC):
    """Abstract base class for entity repository backends."""

    @property
    @abstractmethod
    def _entity_type(self) -> str:
        """Child classes must specify the entity type."""
        pass
    
    @abstractmethod
    def add(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def update(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def get(self, *args, **kwargs) -> Any:
        pass

    @abstractmethod
    def list_all(self, *args, **kwargs) -> list[Any]:
        pass

    @abstractmethod
    def remove(self, *args, **kwargs) -> Any:
        pass
