class Spell:
    def __init__(self, name, mana_cost):
        self.name: str = name
        self.mana_cost: int = mana_cost

    def cast(self, base_power):
        self.base_power = base_power
        raise NotImplementedError


class FireSpell(Spell):
    def __init__(self, name, mana_cost):
        super().__init__(name, mana_cost)

    def cast(self, base_power):
        self.damage = base_power + 10
#        print(f"Fire spell '{self.name}' hits for {self.damage} damage!")
        return f"Fire spell '{self.name}' hits for {self.damage} damage!"


class IceSpell(Spell):
    def __init__(self, name, mana_cost):
        super().__init__(name, mana_cost)
        
    def cast(self, base_power):
        self.damage = base_power + 5
#        print(f"Ice spell '{self.name}' hits for {self.damage} damage!")
        return f"Ice spell '{self.name}' hits for {self.damage} damage!"


def cast_all(spells, base_power):
    results = []
    for spell in spells:
        results.append(spell.cast(base_power))
    return results
