from Weapon import Weapon
from Spell import Spell
from Character import *

class Hero(Character):
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        Character.__init__(self, health)
        self.name = name
        self.title = title
        self.__max_mana = mana
        self.mana = mana #current mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.equiped = None
        self.spell = None

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_mana(self):
        return self.mana

    def can_cast(self):
        return True if self.spell is not None and self.mana > 0 else False

    def take_healing(self, healing_points):
        self.health+=healing_points
        if self.health > self._max_health:
            self.health = self._max_health

    #in every move, mana will be regenerated by rate
    #if hero takes mana potion, he will regenerate as much mana as the potion is giving
    def take_mana(self, mana_points=None):
        if mana_points is None:
             mana_points = self.mana_regeneration_rate

        self.mana += mana_points
        if self.mana > self.__max_mana:
            self.mana = self.__max_mana

    def equip(self, weapon:Weapon):
        self.equiped = weapon

    def learn(self, spell:Spell):
        self.spell = spell

    def attack(self, by=None):
        if by == 'weapon':
            if self.equiped is not None:
                return self.equiped.damage

        if by == 'magic':
            if self.spell is not None:
                #check if we have enough mana
                if self.mana >= self.spell.mana_cost:
                    self.mana -= self.spell.mana_cost
                    return self.spell.damage

        return 0

