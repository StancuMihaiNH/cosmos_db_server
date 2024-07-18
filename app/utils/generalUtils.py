from typing import OrderedDict
from uuid import uuid4


def generate_unique_id(service, field_name="id"):
    while True:
        new_id = str(uuid4())
        query = f"SELECT * FROM c WHERE c.{field_name}='{new_id}'"
        existing_item = service.query_items(query=query)
        if not existing_item:
            return new_id
