from fastapi import APIRouter
from app.services.prompt_service import PromptService

router = APIRouter()
prompt_service = PromptService()

@router.get("/prompts", tags=["prompts"])
def get_all_prompts():
    return prompt_service.query_items(query="SELECT * FROM c")