import os
import tempfile
from Hero import Hero

class Dungeon:
    def __init__(self, map_directory):
        self.map_directory = map_directory
        self.tmp_map = []
        self.hero_position_X = None
        self.hero_position_Y = None
        self.fill_tmp_map()

    def fill_tmp_map(self):
        with open(self.map_directory, 'r') as f:
            for line in f:
                line = line.replace('\n', "")
                self.tmp_map.append([x for x in line])

    def print_map(self):
        for line in self.tmp_map:
            print(''.join(line))
        
        print('\n')

    def spawn(self, hero: Hero):
        for x, line in enumerate(self.tmp_map):
            for y, symbol in enumerate(line):
                if symbol == 'S':
                    self.tmp_map[x][y] = 'H'
                    self.hero_position_X = x
                    self.hero_position_Y = y
                    return True
        return False

    def update_tmp_map(self, x, y):
        self.tmp_map[x][y] = 'H'
        self.tmp_map[self.hero_position_X][self.hero_position_Y] = '.'
        self.hero_position_X = x
        self.hero_position_Y = y

    def move_hero(self, direction):
        direction = direction.lower()
        if direction == 'up':
            if self.tmp_map[self.hero_position_X - 1][self.hero_position_Y] != '#':
                self.update_tmp_map(self.hero_position_X - 1, self.hero_position_Y)
                return True
            return False

        if direction == 'down':
            if self.tmp_map[self.hero_position_X + 1][self.hero_position_Y] != '#':
                self.update_tmp_map(self.hero_position_X + 1, self.hero_position_Y)
                return True
            return False
        
        if direction == 'left':
            if self.tmp_map[self.hero_position_X] [self.hero_position_Y - 1]!= '#':
                self.update_tmp_map(self.hero_position_X, self.hero_position_Y - 1)
                return True
            return False

        if direction == 'right':
            if self.tmp_map[self.hero_position_X][self.hero_position_Y + 1] != '#':
                self.update_tmp_map(self.hero_position_X, self.hero_position_Y + 1)
                return True
            return False
            