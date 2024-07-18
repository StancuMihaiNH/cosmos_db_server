from app.services.base_service import BaseService


class MessageService(BaseService):
    def __init__(self):
        super().__init__(container_id="Message")
