import os
from Hero import Hero

class Dungeon:
    def __init__(self, map_directory):
        self.map_directory = map_directory
        self.temp_map_directory = self._create_temp_map_directory()
        self._fill_temp_map()
    
    def _create_temp_map_directory(self):
        lst = self.map_directory.split('/')
        lst = [x for x in lst if x != '' and x != '.']
        lst[len(lst) - 1] = 'temp_' + lst[len(lst) - 1]
        self.temp_map_directory = '/'.join(lst)
        return self.temp_map_directory
    
    def _fill_temp_map(self):
        with open(self.map_directory) as f:
            with open(self.temp_map_directory, "w") as f1:
                for line in f:
                    f1.write(line)

    def print_map(self):
        with open(self.temp_map_directory, 'r') as f:
            print(f.read())

    def spawn(self, hero: Hero):
        pass
        # is_able_to_spawn = False
        # tmp_file = open(self.create_temp_map_directory)
        # with open(self.map_directory, 'r') as f:
        #     for line in f:
        #         for symbol in line:
        #             if symbol == 'S':
        #                 tmp_file.write('H')
        #                 is_able_to_spawn = True
        #             tmp_file.write(symbol)
        #         tmp_file.write('\n')
        # tmp_file.close()
        # return is_able_to_spawn