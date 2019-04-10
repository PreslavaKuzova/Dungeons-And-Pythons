from Weapon import Weapon
from Spell import Spell

class Enemy:
    def __init__(self, health, mana, damage):
        self.__max_health = health
        self.__max_mana = mana
        self.health = health #modifiable value, current health
        self.mana = mana #current mana
        self.damage = damage
        self.equiped = None
        self.spell = None


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


    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def take_healing(self, healing_points):
        self.health+=healing_points
        if self.health > self.__max_health:
            self.health = self.__max_health

    def take_damage(self, dmg_points):
        self.health-=dmg_points
        if self.health < 0:
            self.health = 0

    def equip(self, weapon):
        if not isinstance(weapon, Weapon):
            raise TypeError('the weapon given is not of class Weapon!')

        self.equiped = weapon

    def learn(self, spell):
        if not isinstance(spell, Spell):
            raise TypeError('the spell given is not of class Spell!')

        self.spell = spell

    def attack(self, by=None):
        if by == 'weapon':
            if self.weapon != None:
                return self.equiped.damage

        if by == 'magic':
            if self.spell != None:
                #check if we have enough mana
                if self.mana >= self.spell.mana_cost:
                    self.mana -= self.spell.mana_cost
                    return self.spell.damage

        return 0




