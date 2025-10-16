from dataclasses import dataclass, field
from typing import Optional, List
import numpy as np

@dataclass
class Article:
    id: str
    title: str
    author_id: str
    embedding: Optional[np.ndarray] = field(default=None)

    def update_title(self, new_title: str):
        if not new_title:
            raise ValueError("Article title cannot be empty")
        self.title = new_title

    def set_embedding(self, vector: np.ndarray):
        if vector.ndim != 1:
            raise ValueError("Embedding must be a 1D vector")
        self.embedding = vector