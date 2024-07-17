from app.services.base_service import BaseService

class PromptService(BaseService):
    def __init__(self):
        super().__init__(container_id="Prompt")