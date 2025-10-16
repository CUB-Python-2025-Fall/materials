from dataclasses import dataclass, asdict
import numpy as np

@dataclass
class AbstractDTO:
     
     def to_dict(self) -> dict:
       return asdict(self)

@dataclass
class ArticleEmbeddingDTO(AbstractDTO):
    article_id: str
    embedding: np.ndarray
   
@dataclass
class ArticleDTO(AbstractDTO):
    id: str
    title: str
    author_id: str

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class AuthorDTO(AbstractDTO):
    id: str
    name: str

    def to_dict(self) -> dict:
        return asdict(self)

@dataclass
class UserDTO(AbstractDTO):
    id: str
    name: str
    

@dataclass
class UserEmbeddingDTO(AbstractDTO):
    user_id: str
    embedding: np.ndarray