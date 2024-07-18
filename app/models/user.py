class User:
    def __init__(self, id, email, name, avatar=None, created_at=None, updated_at=None):
        self.id = id
        self.email = email
        self.name = name
        self.avatar = avatar
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return self.__dict__
