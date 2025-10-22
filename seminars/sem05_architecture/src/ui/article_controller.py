from src.services.recommender_service import RecommenderService
from typing import Any

class ArticleController:
    def __init__(self, recommender_service: RecommenderService):
        self._svc = recommender_service

    def create_article(self, payload: dict[str, Any]) -> dict[str, Any]:
        self._svc.create_article(payload)
        return {"status": "ok", "article_id": payload["id"]}

    def list_articles(self) -> dict[str, Any]:
        articles = self._svc.list_articles()
        return {"articles": [a.to_dict() for a in articles]}
