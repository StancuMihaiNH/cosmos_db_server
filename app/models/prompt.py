class Prompt:
    def __init__(self, id, title, description, created_at=None, updated_at=None):
        self.id = id
        self.title = title
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return self.__dict__