class Spell:
    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range

    def __eq__(self, other):
        for k in self.__dict__.keys():
            if self.__dict__[k] != other.__dict__[k]:
                return False
        return True