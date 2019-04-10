from Hero import Hero

class Dungeon:
    def __init__(self, map_directory):
        self.map_directory = map_directory
        self._hero_position = []

    def print_map(self):
        with open(self.map_directory, 'r') as f:
            print(f.read())
    
    def spawn(self, hero: Hero):
        with open(self.map_directory, 'r') as f:
            for x, line in enumerate(f):
                for y, symbol in enumerate(line):
                    if symbol == 'S':
                        symbol = 'H'
                        self._hero_position = [x, y]
                        return True
        return False