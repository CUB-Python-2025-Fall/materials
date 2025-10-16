from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import Any
import numpy as np

class AbstractDBO(ABC):
    
    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def from_dict(self, obj: dict) -> Any:
        pass

@dataclass
class UserDBO(AbstractDBO):

    id: str
    name: str
    login: str
    email: str
    
    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(obj: dict) -> Any:
        return UserDBO(**obj)

@dataclass
class ArticleDBO(AbstractDBO):

    id: str
    title: str
    author_id: str
    
    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(obj: dict) -> Any:
        return ArticleDBO(**obj)
    

@dataclass
class AuthorDBO(AbstractDBO):

    id: str
    title: str
    name: str
    author_id: str
    
    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(obj: dict) -> Any:
        return AuthorDBO(**obj)
    

@dataclass
class EmbeddingDBO:

    id: str
    embedding: np.ndarray