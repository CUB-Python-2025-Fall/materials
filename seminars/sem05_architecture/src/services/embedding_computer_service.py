from src.infrastructure.repository.embedding_repository import EmbeddingRepository
from src.services.dto.dtos import UserEmbeddingDTO, ArticleEmbeddingDTO
import numpy as np

class EmbeddingComputerService:
    def __init__(
        self,
        user_embedding_repository: EmbeddingRepository,
        article_embedding_repository: EmbeddingRepository,
        embedding_dim: int = 128,
    ):
        self._user_repository = user_embedding_repository
        self._article_repository = article_embedding_repository
        self._embedding_dim = embedding_dim

    def _compute_random_embedding(self) -> np.ndarray:
        """Generate a random embedding vector."""
        return np.random.rand(self._embedding_dim).astype(np.float32)

    def _modify_embedding(self, embedding: np.ndarray) -> np.ndarray:
        """Modify an existing embedding (random noise as placeholder)."""
        noise = np.random.normal(0, 0.01, size=embedding.shape).astype(np.float32)
        return embedding + noise

    def ensure_user_embedding(self, user_id: str) -> UserEmbeddingDTO:
        emb = self._user_repository.find_by_id(user_id)
        if emb is None:
            emb = self._compute_random_embedding()
            self._user_repository.add({"id": user_id, "vector": emb})
        return UserEmbeddingDTO(user_id=user_id, embedding=emb)

    def update_user_embedding(self, user_id: str) -> UserEmbeddingDTO:
        emb = self._user_repository.find_by_id(user_id)
        if emb is None:
            return self.ensure_user_embedding(user_id)

        new_emb = self._modify_embedding(emb)
        self._user_repository.update({"id": user_id, "vector": new_emb})
        return UserEmbeddingDTO(user_id=user_id, embedding=new_emb)

    def ensure_article_embedding(self, article_id: str) -> ArticleEmbeddingDTO:
        emb = self._article_repository.find_by_id(article_id)
        if emb is None:
            emb = self._compute_random_embedding()
            self._article_repository.add({"id": article_id, "vector": emb})
        return ArticleEmbeddingDTO(article_id=article_id, embedding=emb)

    def update_article_embedding(self, article_id: str) -> ArticleEmbeddingDTO:
        emb = self._article_repository.find_by_id(article_id)
        if emb is None:
            return self.ensure_article_embedding(article_id)

        new_emb = self._modify_embedding(emb)
        self._article_repository.update({"id": article_id, "vector": new_emb})
        return ArticleEmbeddingDTO(article_id=article_id, embedding=new_emb)