from adapters.outbound.database.person_mysql_persistence import PersonMysqlPersistence
from business_logic.services.person_crud_service import PersonCrudService


class PersonCrudPort:
    def __init__(self):
        repository = PersonMysqlPersistence()
        self.service = PersonCrudService(repository=repository)

    def create_person(self, person_data: dict):
        return self.service.create_person(person_data)

    def show_tables(self):
        return self.service.get_database_tables()