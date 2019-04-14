class Character: 
    def __init__(self, health):
        self.__max_health = health
        self.health = health #modifiable value, current health

    def get_health(self):
        return self.health

    def is_alive(self):
        return True if (self.health > 0) else False

    def take_damage(self, dmg_points):
        self.health -= dmg_points
        if self.health < 0:
            self.health = 0