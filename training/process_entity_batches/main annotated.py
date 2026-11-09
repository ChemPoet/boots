# input command structure:  {"action":   "create",      "entity":   Material("mat-1", "Steel", 12)}
#         entity = collection of info incl. class                     Class    ID      Name   Cond
#                           {"action":   "update",      "id":       "mac-2",                        "changes":    {"name": "CNC Lathe", "condition": 92}}
#                            USER REQ   METHOD CALLED   VARIABLE     VALUE                         ACTION TAKEN     VAR         VAL         VAR     VAL
        
        # self.id_set: set[str] = []
        # self.catalogue: dict[(str, str),] = [(self.entity_id, self.name),]
        # self.id_set.add(self.entity_id)
        # self.catalogue[self.entity_id] = [self.name]
        # self.inventory: dict[(str, int),] = [(self.name, self.__quant),]
        # self.status: dict[(str, int),] = [(self.name, self.__condit),]
        
class Entity:
    def __init__(self, entity_id, name):
        self.entity_id: str = entity_id
        self.name: str = name
        self.id_set: set[str] = []
        self.catalogue: dict[(str, str),] = [(self.entity_id, self.name),]
        
            
    #   each entity_id must be unique str
    #   name cannot be empty str

    def update(self, changes):      # !!!! changes.name  changes.entity_id !!!!!
        #Field updates
        if len(self.name) < 1:
            raise ValueError("invalid name")
        
        if self.entity_id in self.id_set:
            raise ValueError(f"duplicate entity: {self.entity_id}")
'''
        #Error Handling
        if changes != self.entity_id or self.name:
            raise ValueError(f"unknown field: {changes}")
'''        
        # self.id_set.add(self.entity_id)
        # self.catalogue[self.entity_id] = [self.name]
                
        
    #   ONLY entity name and type-specific field may be updated
    #   Reject unknow fields and invalid values (entity_id, name)


class Material(Entity):
    def __init__(self, entity_id, name, quantity):
        super().__init__(entity_id, name)
        self.__quant: int = quantity
        self.inventory: dict[(str, int),] = [(self.name, self.__quant),]
        if self.__quant < 0:
            raise ValueError("invalid quantity")
    # import entity class definitions and methods
    #   quantity must be int > 0

    def update(self, changes):
        super().update(changes)
        if changes == self.__quant:
            self.inventory[self.name] = [self.__quant]
        if changes ==
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
        super().__init__(Entity)
        self.id_set: set[str] = []
        self.catalogue: dict[(str, str),] = [(self.entity_id, self.name),]
        self.inventory: dict[(str, int),] = [(self.name, self.__quant),]
        self.status: dict[(str, int),] = [(self.name, self.__condit),]
    # import entity, material, and machine class definitions and methods needed in this section

    def create(self, entity):
        # entity = collection of info incl. class -> e.g., Machine("mac-2", "Lathe", 70)
        #                                                   Class    ID      Name   Cond
        
        if entity == Material:
            Entity.update(entity)
            self.id_set.add(self.entity_id)
            self.catalogue[self.entity_id] = [self.name]
            self.inventory[self.name] = [self.__quantity]
            
        elif entity == Machine:
            self.id_set.add(self.entity_id)
            self.catalogue[self.entity_id] = [self.name]
            self.status[self.name] = [self.__condit]
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
