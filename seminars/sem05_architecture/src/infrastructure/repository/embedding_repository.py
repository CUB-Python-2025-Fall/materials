from src.infrastructure.repository.vector_entity_repository import VectorEntityRepository
from typing import Optional
from src.infrastructure.dbo.dbos import EmbeddingDBO
import numpy as np

#very boring class
class EmbeddingRepository(VectorEntityRepository):

    def find_by_id(self, obj_id: str) -> Optional[np.ndarray]:
        return self.get(obj_id, is_strict=False)
    
    @property
    def _entity_type(self) -> str:
        return "embedding"