from src.infrastructure.repository.document_entity_repository import DocumentEntityRepository
from src.infrastructure.dbo.dbos import UserDBO

class UserRepository(DocumentEntityRepository):
    @property
    def _entity_type(self) -> str:
        return "users"
    
    @property
    def _entity_dbo_type(self) -> type[UserDBO]:
        """Subclasses must specify the entity dbo type."""
        return UserDBO
    
    def list_by_name(self, obj_name: str) -> list[UserDBO]:
        collection = self.list_all()
        return [user for user in collection if user.name == obj_name]

