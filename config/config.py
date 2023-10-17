import os


# Singleton Pattern - ConfigurationManager
class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance.load_config()
        return cls._instance

    def load_config(self):
        self.DB_USERNAME = os.getenv('DB_USERNAME', 'root')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD', 'toor')
        self.DB_HOST = os.getenv('DB_HOST', 'localhost')
        self.DB_PORT = os.getenv('DB_PORT', '3306')
        self.DB_NAME = os.getenv('DB_NAME', 'ports_and_adapters')
