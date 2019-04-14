import json
import random
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
        
        if (x in range(0, self.X) and y in range(0, self.Y)):
            if self.tmp_map[x][y] != '#':
                if  self.tmp_map[x][y] == 'T':
                    self.treasure_found()
                if  self.tmp_map[x][y] == 'E':
                    enemy = Enemy(self.level*15, self.level*10)
                    fight = Fight(self.hero, enemy)
                    fight.fight()
                self.start_remote_battle(x, y)
                self._update_tmp_map(x, y)
                self.hero.take_mana()
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

    def start_remote_battle(self, curr_x, curr_y):
        pass
        #can't work like that because we have to move during the fight
        #TODO: when loading the map, count enemies and create set with them
        #when the enemy is dead, pop from set => hash for the enemies class
    #     try:
    #         rng = self.hero.spell.cast_range
    #     except:
    #         rng = 0
    #     low_x = curr_x - rng if curr_x - rng > 0 else 0
    #     up_x = curr_x + rng if curr_x + rng <= self.X else self.X
    #     low_y = curr_y - rng if curr_y - rng > 0 else 0
    #     up_y = curr_y + rng if curr_y + rng <= self.Y else self.Y
    #     for x in range(low_x, up_x):
    #         for y in range(low_y, up_y):
    #             if self.tmp_map[x][y] == 'E':
    #                 enemy = Enemy(self.level*15, self.level*15, self.level*10)
    #                 fight = Fight(self.hero, enemy)
                    


    @staticmethod
    def read_json(argument):
        with open (argument, 'r') as f:
            data = json.load(f)
        return data
