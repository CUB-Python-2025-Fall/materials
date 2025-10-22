from dataclasses import dataclass, field
from typing import Optional, List
import numpy as np

@dataclass
class User:
    id: str
    name: str
    embedding: Optional[np.ndarray] = field(default=None)
    favorite_articles: List[str] = field(default_factory=list)  # example domain feature

    def rename(self, new_name: str):
        if not new_name:
            raise ValueError("User name cannot be empty")
        self.name = new_name

    def set_embedding(self, vector: np.ndarray):
        if vector.ndim != 1:
            raise ValueError("Embedding must be a 1D vector")
        self.embedding = vector

    def add_favorite_article(self, article_id: str):
        if article_id not in self.favorite_articles:
            self.favorite_articles.append(article_id)