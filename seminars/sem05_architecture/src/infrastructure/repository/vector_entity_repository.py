from src.infrastructure.db.numpy_db import NumpyDB
from src.infrastructure.repository.interface.entity_repository_base import EntityRepositoryBase
from src.infrastructure.exceptions.repository_exceptions import VectorExistsError, VectorNotFoundError
from src.infrastructure.dbo.dbos import EmbeddingDBO
from typing import Optional
from abc import ABC
import numpy as np

class VectorEntityRepository(EntityRepositoryBase):
    """
    Repository for vector entities using NumpyDB as the backend.
    Each row in the underlying array corresponds to one entity (vector).
    """

    def __init__(self, db: NumpyDB):
        self._db = db

    def add(self, obj: EmbeddingDBO) -> None:
        existing = self._db.get_by_id(obj.id)
        if existing is not None:
            raise VectorExistsError(f"Vector with id={obj.id} already exists")

        self._db.set_by_id(obj.id, obj.embedding)

    def update(self, obj: EmbeddingDBO) -> None:
        existing = self._db.get_by_id(obj.id)
        if existing is None:
            raise VectorNotFoundError(f"Vector with id={obj.id} not found")
        
        self._db.set_by_id(obj.id, obj.embedding)

    def get(self, obj_id: str, is_strict: bool=True) -> Optional[EmbeddingDBO]:
        embedding = self._db.get_by_id(obj_id)
        if is_strict and embedding is None:
            raise VectorNotFoundError(f"Vector with id={obj_id} not found")
        return EmbeddingDBO(obj_id, embedding)

    def list_all(self) -> list[EmbeddingDBO]:
        index = self._db._load_index()
        data = self._db._load_data()
        result: list[EmbeddingDBO] = []
        for obj_id, row in index.items():
            result.append(EmbeddingDBO(id=obj_id, embedding=data[row]))
        return result

    def remove(self, obj_id: str) -> None:
        index = self._db._load_index()
        data = self._db._load_data()

        if obj_id not in index:
            raise VectorNotFoundError(f"Vector with id={obj_id} not found")

        row_to_remove = index[obj_id]

        new_data = np.delete(data, row_to_remove, axis=0)

        new_index = {
            k: (v if v < row_to_remove else v - 1)
            for k, v in index.items()
            if k != obj_id
        }

        self._db._save_data(new_data)
        self._db._save_index(new_index)