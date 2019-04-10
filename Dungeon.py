import os
import tempfile
from Hero import Hero

class Dungeon:
    def __init__(self, map_directory):
        self.map_directory = map_directory
        self.tmp_map = []
        self.hero_position = []
        self.fill_tmp_map()

    def fill_tmp_map(self):
        with open(self.map_directory, 'r') as f:
            for line in f:
                line = line.replace('\n', "")
                self.tmp_map.append([x for x in line])

    def print_map(self):
        for line in self.tmp_map:
            print(''.join(line))

    def spawn(self, hero: Hero):
        for x, line in enumerate(self.tmp_map):
            for y, symbol in enumerate(line):
                if symbol == 'S':
                    self.tmp_map[x][y] = 'H'
                    self.hero_position = [x, y]
                    return True
        return False
