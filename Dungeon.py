import json
import random
import os
from Hero import Hero
from Enemy import Enemy
from Spell import Spell
from Weapon import Weapon
from Fight import Fight

class Dungeon:
    def __init__(self, map_directory, hero: Hero, level):
        self.map_directory = map_directory
        self.hero = hero
        self.level = level #the power of enemies will depend on level
        self.tmp_map = []
        self.hero_position_X = None
        self.hero_position_Y = None
        self.X = 0
        self.Y = 0
        self.fill_tmp_map()
        self.get_end_point()

    def get_end_point(self):
        for x, line in enumerate(self.tmp_map):
            for y, symbol in enumerate(line):
                if symbol == 'G':
                    self.endpoint = (x, y)

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
        
        if x in range(0, self.X) and y in range(0, self.Y):
            enemy = Enemy(self.level*15, self.level*10)
            fight = Fight(self.hero, enemy, self.tmp_map, self.X, self.Y)
            if self.tmp_map[x][y] != '#':
                self.hero.take_mana()
                if  self.tmp_map[x][y] == 'T':
                    self.treasure_found()
                if  self.tmp_map[x][y] == 'E':
                    enemy = Enemy(self.level*15, self.level*10)
                    fight.fight()
                self._update_tmp_map(x, y)
                if self.hero.can_cast():
                    fight.remote_battle(x,y)
                return True
        else:
            print('Invalid. Your move was out of the map!')

        return False
    
    def treasure_found(self):
        treasure = random.choice(["weapon", "spell", "mana", "health"])
        print('You win {}!'.format(treasure))
        if treasure == "health":
            self.hero.take_healing(random.randint(10, 50))
            return self.hero.health
        
        if treasure == "mana":
            self.hero.take_mana(random.randint(10, 50))
            return self.hero.mana
        
        if treasure == "spell":
            random_key = str(random.randint(1, 7))
            spells = self.read_json("items/spells.json")
            spell_dic = spells.get(random_key)
            spell = Spell(**spell_dic)
            self.hero.learn(spell)
            return spell.name

        if treasure == "weapon":
            random_key = str(random.randint(1, 4))
            weapons = self.read_json("items/weapons.json")
            weapon_dic = weapons.get(random_key)
            weapon = Weapon(**weapon_dic)
            self.hero.equip(weapon)
            return weapon.name

    def hero_attack(self, by=None):
        dmg = self.hero.attack(by=by)
        if dmg > 0:
            return True
        return False
 
    @staticmethod
    def read_json(argument):
        with open (argument, 'r') as f:
            data = json.load(f)
        return data
