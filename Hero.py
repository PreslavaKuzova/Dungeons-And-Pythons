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

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def can_cast(self):
        if self.mana > 0:
            return True
        else:
            return False

    def take_damage(self, dmg_points):
        pass

    def take_healing(self, healing_points):
        pass

    def take_mana(self, mana_points):
        pass

    def equip(self, weapon):
        #should validate weapon to be instance of weapon class
        pass

    def learn(self, spell):
        #should validate spell to be instance of Spell class
        pass

    def attack(self, by=None):
        pass


