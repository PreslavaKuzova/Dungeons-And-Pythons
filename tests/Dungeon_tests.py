import unittest
import os, sys
sys.path.insert(0, '../')
from Dungeon import *
from Hero import *


class TestDungeon(unittest.TestCase):
    def test_dungeon_initialization_when_empty_map(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/empty.txt', h, 2)
        self.assertEqual(d.tmp_map, [])
    
    def test_dungeon_initialization_when_map_is_correct(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/test.txt', h, 2)
        expected_map = [['.', '.', '#'],['S', '.', '.'],['#', '.', 'G']]
        self.assertEqual(d.tmp_map, expected_map)
    
    def test_spawning_the_hero_on_the_S_location_on_map(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/test.txt', h, 2)
        d.spawn()
        result = [d.hero_position_X, d.hero_position_Y]
        expected = [1, 0]
        self.assertEqual(result, expected)
    
    def test_getting_the_end_point_of_the_map_then_return_its_coordinates(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/test.txt', h, 2)
        result = d.endpoint
        expected = (2, 2)
        self.assertEqual(result, expected)

    

if __name__ =='__main__':
    unittest.main()