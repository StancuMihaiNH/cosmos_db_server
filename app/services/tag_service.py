from app.services.base_service import BaseService

class TagService(BaseService):
    def __init__(self):
        super().__init__(container_id="Tag")