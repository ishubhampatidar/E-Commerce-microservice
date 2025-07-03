from fastapi import APIRouter
from app.grpc_clients.user_client import get_user_by_id

router = APIRouter()

@router.get("/user/{user_id}")
def read_user(user_id: int):
    user = get_user_by_id(user_id)
    return {
        "id": user.id,
        "email": user.email,
        "fullname": user.full_name
    }