from fastapi import APIRouter
from app.services.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.get("/users/{user_id}", tags=["users"])
def get_user(user_id: str):
    return user_service.read_item(item_id=user_id)

@router.get("/users", tags=["users"])
def get_all_users():
    return user_service.query_items(query="SELECT * FROM c")

@router.post("/users", tags=["users"])
def create_user(user: dict):
    user_service.create_item(item=user)

@router.put("/users/{user_id}", tags=["users"])
def update_user(user_id: str, user: dict):
    user_service.update_item(item_id=user_id, updated_item=user)

@router.delete("/users/{user_id}", tags=["users"])
def delete_user(user_id: str):
    user_service.delete_item(item_id=user_id)
