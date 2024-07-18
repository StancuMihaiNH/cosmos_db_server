from app.services.base_service import BaseService


class TopicService(BaseService):
    def __init__(self):
        super().__init__(container_id="Topic")
