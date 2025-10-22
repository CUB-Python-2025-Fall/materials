from typing import Any
from src.services.recommender_service import RecommenderService
import numpy as np

def _np_to_list(x: np.ndarray):
    return x.astype(float).tolist()

class RecommenderController:
    def __init__(self, recommender_service: RecommenderService):
        self._svc = recommender_service

    def recommend(self, payload: dict[str, Any]) -> dict[str, Any]:
        user_id = payload["user_id"]
        top_k = int(payload.get("top_k", 5))

        articles = self._svc.recommend_for_user(user_id, top_k)
        return {
            "user_id": user_id,
            "top_k": top_k,
            "recommendations": [a.to_dict() for a in articles],
        }

    def recompute_user(self, payload: dict[str, Any]) -> dict[str, Any]:
        user_id = payload["user_id"]
        emb_dto = self._svc.recompute_user_embedding(user_id)
        return {
            "user_id": user_id,
            "embedding": _np_to_list(emb_dto.embedding),
            "dim": int(len(emb_dto.embedding)),
        }

    def recompute_item(self, payload: dict[str, Any]) -> dict[str, Any]:
        article_id = payload["article_id"]
        emb_dto = self._svc.recompute_article_embedding(article_id)
        return {
            "article_id": article_id,
            "embedding": _np_to_list(emb_dto.embedding),
            "dim": int(len(emb_dto.embedding)),
        }