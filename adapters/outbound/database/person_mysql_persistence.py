from config.config import ConfigurationManager
from config.database.mysql import MysqlConnect
from ports.outbound.person_persistence_port import PersonPersistencePort
from sqlalchemy.orm import sessionmaker


class PersonMysqlPersistence(PersonPersistencePort):
    def __init__(self):
        self.mysql_connector = MysqlConnect()
        self.config = ConfigurationManager()

    def save(self, person_data: dict):
        """Not used"""
        pass

    def delete(self, person: dict):
        """Not used"""
        pass

    def update(self, person: dict):
        """Not used"""
        pass

    def find_by_id(self, person_id: str) -> dict:
        """Not used"""
        pass

    def find_all_tables(self):
        try:
            mysql_engine = self.mysql_connector.get_mysql_engine()

            result = mysql_engine.execute("SHOW TABLES")
            tables = result.fetchall()
            my_tables = []
            for table in tables:
                my_tables.append(table)

            Session = sessionmaker(bind=mysql_engine)
            session = Session()
            session.close()

            return my_tables
        except Exception as e:
            raise e


