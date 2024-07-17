from fastapi import APIRouter
from app.services.tag_service import TagService

router = APIRouter()
tag_service = TagService()

@router.get("/tags", tags=["tags"])
def get_all_tags():
    return tag_service.query_items(query="SELECT * FROM c")