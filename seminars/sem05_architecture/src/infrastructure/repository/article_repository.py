from src.infrastructure.repository.document_entity_repository import DocumentEntityRepository
from src.infrastructure.dbo.dbos import ArticleDBO

class ArticleRepository(DocumentEntityRepository):
    
    @property
    def _entity_type(self) -> str:
        return "articles"
    
    @property
    def _entity_dbo_type(self) -> type[ArticleDBO]:
        """Subclasses must specify the entity dbo type."""
        return ArticleDBO

    def list_by_author(self, author_id: str) -> list[ArticleDBO]:
        """Return all articles written by a given author_id."""
        collection = self.list_all()
        return [doc for doc in collection if doc.author_id == author_id]

    def find_by_title(self, title: str) -> list[ArticleDBO]:
        """Return all articles whose title matches (case-insensitive substring search)."""
        collection = self.list_all()
        title_lower = title.lower()
        return [doc for doc in collection if title_lower in str(doc.title or "").lower()]
    