from fastapi import APIRouter

from app.services.message_service import MessageService

router = APIRouter()
message_service = MessageService()


@router.get("/messages", tags=["messages"])
def get_all_messages():
    return message_service.query_items(query="SELECT * FROM c")
