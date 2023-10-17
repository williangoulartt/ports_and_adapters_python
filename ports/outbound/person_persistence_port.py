from abc import abstractmethod


class PersonPersistencePort:
    @abstractmethod
    def save(self, person: dict):
        pass

    @abstractmethod
    def delete(self, person: dict):
        pass

    @abstractmethod
    def update(self, person: dict):
        pass

    @abstractmethod
    def find_by_id(self, person: str):
        pass

    @abstractmethod
    def find_all_tables(self):
        pass
