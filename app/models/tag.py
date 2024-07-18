class Tag:
    def __init__(self, id, display_name, content, attachments=None):
        self.id = id
        self.display_name = display_name
        self.content = content
        self.attachments = attachments or []

    def to_dict(self):
        return self.__dict__
