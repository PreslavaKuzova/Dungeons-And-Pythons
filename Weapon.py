class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = int(damage)

    def __eq__(self, other):
        for k in self.__dict__.keys():
            if self.__dict__[k] != other.__dict__[k]:
                return False
        return True