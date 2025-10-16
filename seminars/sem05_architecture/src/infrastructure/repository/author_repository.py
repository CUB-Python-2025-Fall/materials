from src.infrastructure.repository.document_entity_repository import DocumentEntityRepository
from src.infrastructure.dbo.dbos import AuthorDBO

class AuthorRepository(DocumentEntityRepository):
    @property
    def _entity_type(self) -> str:
        return "authors"
    
    @property
    def _entity_dbo_type(self) -> type[AuthorDBO]:
        """Subclasses must specify the entity dbo type."""
        return AuthorDBO
    
    def list_by_name(self, obj_name: str) -> list[AuthorDBO]:
        collection = self.list_all()
        return [author for author in collection if author.name == obj_name]
