from Dungeon import Dungeon
from Hero import Hero

from os import listdir

def level_readers(path):
    levels = listdir(path)
    levels.sort()
    h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
    for lvl in levels:
        map = Dungeon(path + '/' + lvl)
        map.print_map()
        map.spawn(h)
        map.print_map()
        map.move_hero('Right')
        map.print_map()

path = 'levels'
level_readers(path)