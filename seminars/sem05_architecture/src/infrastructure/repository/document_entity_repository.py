from src.infrastructure.repository.interface.entity_repository_base import EntityRepositoryBase
from src.infrastructure.dbo.dbos import AbstractDBO
from src.infrastructure.exceptions.repository_exceptions import DocumentExistsError, DocumentNotFoundError
from src.infrastructure.db.json_db import JsonDB
from abc import ABC, abstractmethod
from typing import Optional, Any

class DocumentEntityRepository(EntityRepositoryBase, ABC):

    @property
    @abstractmethod
    def _entity_type(self) -> str:
        """Subclasses must specify the entity type."""

    @property
    @abstractmethod
    def _entity_dbo_type(self) -> type[AbstractDBO]:
        """Subclasses must specify the entity dbo type."""

    def __init__(self, db: JsonDB):
        self._db = db

    def add(self, obj: AbstractDBO) -> None:
        collection = self._db.get_collection(self._entity_type)
        if any(self._entity_dbo_type.from_dict(d).id == obj.id for d in collection):
            raise DocumentExistsError(f"Document with id={obj.id} already exists")
        collection.append(obj.to_dict())
        self._db.set_collection(self._entity_type, collection)

    def update(self, obj: AbstractDBO) -> None:
        collection = self._db.get_collection(self._entity_type)
        for i, d in enumerate(collection):
            db_obj = self._entity_dbo_type.from_dict(d)
            if db_obj.id == obj.id:
                collection[i] = obj.to_dict()
                self._db.set_collection(self._entity_type, collection)
                return
        raise DocumentNotFoundError(f"Document with id={obj.id} not found")

    def get(self, obj_id: str) -> AbstractDBO:
        collection = self._db.get_collection(self._entity_type)
        for d in collection:
            obj = self._entity_dbo_type.from_dict(d)
            if obj.id == obj_id:
                return obj
        raise DocumentNotFoundError(f"Document with id={obj_id} not found")

    def list_all(self) -> list[AbstractDBO]:
        return [self._entity_dbo_type.from_dict(d) for d in self._db.get_collection(self._entity_type)]

    def remove(self, obj_id: str) -> None:
        collection = self._db.get_collection(self._entity_type)
        new_collection = [d for d in collection if self._entity_dbo_type.from_dict(d).id != obj_id]
        if len(new_collection) == len(collection):
            raise DocumentNotFoundError(f"Document with id={obj_id} not found")
        self._db.set_collection(self._entity_type, new_collection)