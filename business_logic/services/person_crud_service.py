import uuid
from ports.outbound.person_persistence_port import PersonPersistencePort


class PersonCrudService:
    def __init__(self, repository):
        self.repository: PersonPersistencePort = repository

    def create_person(self, person_data: dict) -> dict:

        unique_id = str(uuid.uuid4())

        data = person_data
        data['id'] = unique_id

        result: dict = self.repository.save(**data)

        return result

    def get_database_tables(self):
        result: list = self.repository.find_all_tables()

        return result
