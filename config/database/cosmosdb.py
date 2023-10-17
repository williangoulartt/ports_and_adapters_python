from azure.core.exceptions import ResourceNotFoundError
from azure.cosmos import CosmosClient
# If proxy
#from azure.cosmos import ProxyConfiguration

from config.config import ConfigurationManager


class CosmoDBConnect:
    def __init__(self):
        self.config = ConfigurationManager()
        url = self.config.COSMOS_ENDPOINT
        key = self.config.COSMOS_KEY

        # If proxy
        # proxy = ProxyConfiguration()
        # proxy.Port = self.config.PROXY_PORT
        # proxy.Hostname = self.config.PROXY_HOSTNAME
        #
        # self.client = CosmosClient(url, key, proxy_config=proxy)

        # Without proxy
        self.client = CosmosClient(url, key)

    def get_cosmos_container(self, container_name):
        try:
            database = self.client.get_database_client(self.config.DATABASE)
            container = database.get_container_client(container_name)

            return container

        except ResourceNotFoundError as e:
            raise ResourceNotFoundError(f"Container '{container_name}' not found in Cosmos DB.") from e
        except Exception as e:
            raise Exception() from e