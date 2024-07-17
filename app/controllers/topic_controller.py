from fastapi import APIRouter
from app.services.topic_service import TopicService

router = APIRouter()
topic_service = TopicService()

@router.get("/topics", tags=["topics"])
def get_all_topics():
    return topic_service.query_items(query="SELECT * FROM c")