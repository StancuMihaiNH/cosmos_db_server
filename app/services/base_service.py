from azure.cosmos import CosmosClient, PartitionKey
from app.utils.key_vault_manager import KeyVaultManager
from app.utils.constants import Constants
from app.utils.generalUtils import generate_unique_id


class BaseService:
    def __init__(self, container_id):
        key_vault_manager = KeyVaultManager.getInstance()

        self.key = key_vault_manager.get_secret(Constants.COSMOS_KEY_SECRET_NAME)
        self.endpoint = key_vault_manager.get_secret(Constants.COSMOS_ENDPOINT_SECRET_NAME)

        self.database_name = Constants.DATABASE_NAME
        self.container_id = container_id
        self.client = CosmosClient(self.endpoint, self.key)
        self.database = self.client.create_database_if_not_exists(id=self.database_name)
        self.container = self.database.create_container_if_not_exists(
            id=self.container_id,
            partition_key=PartitionKey(path="/PK"),
            offer_throughput=Constants.OFFER_THROUGHPUT,
        )

    def create_item(self, item):
        if "id" not in item:
            item["id"] = generate_unique_id(self)
        if "PK" not in item:
            item["PK"] = f'{self.container_id}#{item["id"]}'
        self.container.create_item(body=item)

    def read_item(self, item_id):
        partition_key = f"{self.container_id}#{item_id}"
        return self.container.read_item(item=item_id, partition_key=partition_key)

    def update_item(self, item_id, updated_item):
        partition_key = f"{self.container_id}#{item_id}"
        self.container.upsert_item(body=updated_item, partition_key=partition_key)

    def delete_item(self, item_id):
        partition_key = f"{self.container_id}#{item_id}"
        self.container.delete_item(item=item_id, partition_key=partition_key)

    def query_items(self, query):
        return list(
            self.container.query_items(query=query, enable_cross_partition_query=True)
        )
