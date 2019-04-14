from Character import *

class Enemy(Character):
    def __init__(self, health, damage):
        Character.__init__(self, health)
        self.damage = damage

    def __str__(self):
        return "Enemy(health={}, damage={})".format(self.health, self.damage)

    def attack(self):
        return self.damage




