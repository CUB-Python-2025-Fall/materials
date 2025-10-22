from src.services.recommender_service import RecommenderService
from typing import Any

class AuthorController:
    def __init__(self, recommender_service: RecommenderService):
        self._svc = recommender_service

    def create_author(self, payload: dict[str, Any]) -> dict[str, Any]:
        self._svc.create_author(payload)
        return {"status": "ok", "author_id": payload["id"]}
