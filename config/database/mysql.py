from sqlalchemy import create_engine
from config.config import ConfigurationManager


class MysqlConnect:
    def __init__(self):
        self.config = ConfigurationManager()
        self.user_name = self.config.DB_USERNAME
        self.password = self.config.DB_PASSWORD
        self.host = self.config.DB_HOST
        self.port = self.config.DB_PORT
        self.db_name = self.config.DB_NAME

    def get_mysql_engine(self):
        DB_URL = f'mysql://{self.user_name}:{self.password}@{self.host}:{self.port}/{self.db_name}'

        engine = create_engine(DB_URL)

        return engine

