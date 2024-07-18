class Message:
    def __init__(
        self,
        id,
        role,
        content,
        user_id,
        files=None,
        source_documents=None,
        created_at=None,
        updated_at=None,
    ):
        self.id = id
        self.role = role
        self.content = content
        self.user_id = user_id
        self.files = files or []
        self.source_documents = source_documents or []
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return self.__dict__
