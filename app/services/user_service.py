from app.services.base_service import BaseService

class UserService(BaseService):
    def __init__(self):
        super().__init__(container_id="User")