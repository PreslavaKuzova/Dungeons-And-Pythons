import json
import random
from Hero import Hero
from Spell import Spell
from Weapon import Weapon

class Dungeon:
    def __init__(self, map_directory, hero: Hero):
        self.map_directory = map_directory
        self.Hero = hero
        self.tmp_map = []
        self.hero_position_X = None
        self.hero_position_Y = None
        self.X = 0
        self.Y = 0
        self.fill_tmp_map()

    def fill_tmp_map(self):
        with open(self.map_directory, 'r') as f:
            for line in f:
                line = line.replace('\n', "")
                self.tmp_map.append([x for x in line])
                self.X += 1
                self.Y = len(line)

    def print_map(self):
        for line in self.tmp_map:
            print(''.join(line))
        
        print('\n')

    def spawn(self):
        for x, line in enumerate(self.tmp_map):
            for y, symbol in enumerate(line):
                if symbol == 'S':
                    self.tmp_map[x][y] = 'H'
                    self.hero_position_X = x
                    self.hero_position_Y = y
                    return True
        return False

    def _update_tmp_map(self, x, y):
        self.tmp_map[x][y] = 'H'
        self.tmp_map[self.hero_position_X][self.hero_position_Y] = '.'
        self.hero_position_X = x
        self.hero_position_Y = y

    def move_hero(self, direction):
        direction = direction.lower()
        
        x = self.hero_position_X
        y = self.hero_position_Y

        if direction == 'up':
            x -= 1
        if direction == 'down':
            x += 1
        if direction == 'left':
            y -= 1
        if direction == 'right':
            y += 1
        
        if (x in range(0, self.X) and y in range(0, self.Y)):
            if self.tmp_map[x][y] != '#':
                if  self.tmp_map[x][y] != 'T':
                    pass
                self._update_tmp_map(x, y)
                return True
        else:
            print('Invalid. Your move was out of the map!')

        return False
    
    def return_tresure(self):
        tresure = random.choice(["weapon", "spell", "mana", "health"])
        return tresure

    @classmethod
    def from_json(cls, json_string):
        dic = json.loads(json_string)
        return cls(**dic[cls.__name__])

h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
map = Dungeon("levels/level1.txt", h)
map.print_map()
print(map.return_tresure())
