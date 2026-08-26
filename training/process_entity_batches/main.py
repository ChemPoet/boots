class Entity:
    def __init__(self, entity_id, name):
        pass
    #   each entity_id must be unique str
    #   name cannot be empty str

    def update(self, changes):
        pass
    #   ONLY entity name and type-specific field may be updated
    #   Reject unknow fields and invalid values (entity_id, name)


class Material(Entity):
    def __init__(self, entity_id, name, quantity):
        pass
    # import entity class definitions and methods
    #   quantity must be int > 0

    def update(self, changes):
        pass
    #   ONLY entity name and type-specific field may be updated (e.g., __quant)
    #   Reject unknow fields and invalid values (quantity)


class Machine(Entity):
    def __init__(self, entity_id, name, condition):
        pass
    # import entity class definitions and methods
    #   condition must be integer in range 0 - 100

    def update(self, changes):
        pass
    #   ONLY entity name and type-specific field may be updated (e.g., __condit)
    #   Reject unknow fields and invalid values (condition)


class EntityCollection:
    def __init__(self):
        pass
    # import entity, material, and machine class definitions and methods needed in this section

    def create(self, entity):
        pass
    #   add entity
    #   reject duplicate IDs

    def get(self, entity_id):
        pass
    #   returns entity
    #   reject missing IDs

    def update(self, entity_id, changes):
        pass
    #   updates matching entity

    def remove(self, entity_id):
        pass
    #   remove and returns matching entity

    def summary(self):
        pass
    #   returns 
    #       total: total number of entitie
    #       materials: total number of materials entities
    #       machines: total number of machines entities
    #       material_units: sum of all materials entities' quantities
    #       avgerage_machine_condition: int avg of all machines entities (int devision aka //), else 0 if there are no machines.


class BatchProcessor:
    def __init__(self, collection):
        pass
    # import Entitycollection -> methods of operations that can be performed

    def process(self, operations):
        pass
    #   accepts list of operation (dict) as input.
    #   supported actions: create, update, remove, summary
    #   return result:dict for each operation in the same order as they were performed
    #   NB! Failed operation mustn't change collection; batch processing MUST continue.
