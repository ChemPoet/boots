class Entity:
    def __init__(self, entity_id, name):
        pass

    def update(self, changes):
        pass


class Material(Entity):
    def __init__(self, entity_id, name, quantity):
        pass

    def update(self, changes):
        pass


class Machine(Entity):
    def __init__(self, entity_id, name, condition):
        pass

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
