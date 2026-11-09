class Entity:
    def __init__(self, entity_id, name):
        self.entity_id: str = entity_id
        self.name: str = name
        self.id_set: set[str] = []
        self.catalogue: dict[(str, str),] = [(self.entity_id, self.name),]

    def update(self, changes):
        pass


class Material(Entity):
    def __init__(self, entity_id, name, quantity):
        super().__init__(entity_id, name)
        self.__quant: int = quantity
        self.inventory: dict[(str, int),] = [(self.name, self.__quant),]

    def update(self, changes):
        pass


class Machine(Entity):
    def __init__(self, entity_id, name, condition):
        super().__init__(entity_id, name)
        self.__condit: int = condition
        self.status: dict[(str, int),] = [(self.name, self.__condit),]

    def update(self, changes):
        pass


class EntityCollection:
    def __init__(self):
        pass

    def create(self, entity):
        pass

    def get(self, entity_id):
        pass

    def update(self, entity_id, changes):
        pass

    def remove(self, entity_id):
        pass

    def summary(self):
        pass


class BatchProcessor:
    def __init__(self, collection):
        pass

    def process(self, operations):
        pass
