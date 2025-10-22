import numpy as np
from typing import List

from src.infrastructure.repository.user_repository import UserRepository
from src.infrastructure.repository.author_repository import AuthorRepository
from src.infrastructure.repository.article_repository import ArticleRepository
from src.infrastructure.repository.embedding_repository import EmbeddingRepository
from src.services.embedding_computer_service import EmbeddingComputerService
from src.services.dto.dtos import ArticleDTO, AuthorDTO, UserDTO
from src.infrastructure.dbo.dbos import ArticleDBO, AuthorDBO, UserDBO


class RecommenderService:
    def __init__(
        self,
        user_repository: UserRepository,
        author_repository: AuthorRepository,
        article_repository: ArticleRepository,
        user_embedding_repository: EmbeddingRepository,
        article_embedding_repository: EmbeddingRepository,
        embedding_service: EmbeddingComputerService,
    ):
        self._user_repository = user_repository
        self._author_repository = author_repository
        self._article_repository = article_repository
        self._user_embedding_repository = user_embedding_repository
        self._article_embedding_repository = article_embedding_repository
        self._embedding_service = embedding_service

    def create_user(self, user_obj: UserDTO) -> None:
        self._user_repository.add(UserDBO.from_dict(user_obj.to_dict()))
        self._embedding_service.ensure_user_embedding(user_obj.id)

    def list_users(self) -> list[UserDTO]:
        return self._user_repository.list_all()

    def create_author(self, author_obj: AuthorDTO) -> None:
        self._author_repository.add(AuthorDBO.from_dict(author_obj.to_dict()))

    def create_article(self, article_obj: ArticleDTO) -> None:
        self._article_repository.add(ArticleDBO.from_dict(article_obj.to_dict()))
        self._embedding_service.ensure_article_embedding(article_obj.id)

    def list_articles(self) -> list[ArticleDTO]:
        return self._article_repository.list_all()

    def recompute_user_embedding(self, user_id: str) -> np.ndarray:
        return self._embedding_service.update_user_embedding(user_id)

    def recompute_article_embedding(self, article_id: str) -> np.ndarray:
        return self._embedding_service.update_article_embedding(article_id)

    def recommend_for_user(self, user_id: str, top_k: int = 5) -> List[dict]:
        """Recommend top-k articles for a given user by cosine similarity."""

        user_emb = self._embedding_service.ensure_user_embedding(user_id)

        articles = self._article_repository.list_all()
        results = []

        for article in articles:
            article_id = article.id
            article_emb = self._embedding_service.ensure_article_embedding(article_id)

            sim = self._cosine_similarity(user_emb, article_emb)
            results.append((sim, article))

        results.sort(key=lambda x: x[0], reverse=True)
        return [article for _, article in results[:top_k]]

    @staticmethod
    def _cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
        if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
            return 0.0
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
