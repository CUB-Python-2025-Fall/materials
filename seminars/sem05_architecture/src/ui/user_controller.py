from src.services.dto.dtos import UserDTO
from src.services.recommender_service import RecommenderService
class UserController:
    def __init__(self, svc: RecommenderService):
        self._svc = svc

    def create_user(self, payload: dict):
        self._svc.create_user(UserDTO(**payload))
        return {"status": "ok"}

    def list_users(self):
        return {"users": [u.to_dict() for u in self._svc.list_users()]}
