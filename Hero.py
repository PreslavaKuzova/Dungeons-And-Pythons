class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.__max_health = health
        self.__max_mana = mana
        self.health = health #modifiable value, current health
        self.mana = mana #current mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.equiped = {} #set for weapons equiped
        self.spells = {} #set for known spells

    def known_as():
        return "{} the {}".format(self.name, self.title)

    def get_health():
        return self.health

    def get_mana():
        return self.mana

    def is_alive():
        if self.health > 0:
            return True
        else:
            return False

    def can_cast():
        if self.mana > 0:
            return True
        else:
            return False

    def take_damage(dmg_points):
        pass

    def take_healing(healing_points):
        pass

    def take_mana(mana_points):
        pass

    def equip(weapon):
        #should validate weapon to be instance of weapon class
        pass

    def learn(spell):
        #should validate spell to be instance of Spell class
        pass

    def attack(by=None):
        pass


