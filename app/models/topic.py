class Topic:
    def __init__(
        self,
        id,
        name,
        description,
        user_id,
        tags=None,
        pinned=False,
        pinned_at=None,
        created_at=None,
        updated_at=None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.user_id = user_id
        self.tags = tags or []
        self.pinned = pinned
        self.pinned_at = pinned_at
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return self.__dict__
