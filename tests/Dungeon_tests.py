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
        expected_map = [['.', '.', '#'],['S', 'T', '.'],['#', '.', 'G']]
        self.assertEqual(d.tmp_map, expected_map)
    
    def test_getting_the_dimentions_of_the_current_map_when_map_is_empty(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/empty.txt', h, 2)
        expected = (0, 0)
        self.assertEqual((d.X, d.Y), expected)

    def test_getting_the_dimentions_of_the_current_map(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/test.txt', h, 2)
        expected = (3, 3)
        self.assertEqual((d.X, d.Y), expected)
    
    def test_getting_the_spawning_coordinates_of_the_hero_on_the_S_location_on_map(self):
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

    def test_when_spawning_the_hero_is_successful_then_resturn_true(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/test.txt', h, 2)
        self.assertTrue(d.spawn())

    def test_when_spawning_the_hero_is_unsuccessful_then_resturn_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/empty.txt', h, 2)
        self.assertFalse(d.spawn())

    def test_when_spawning_the_hero_then_change_S_to_H(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/test.txt', h, 2)
        d.spawn()
        letter_on_the_map = d.tmp_map[d.hero_position_X][d.hero_position_Y]
        self.assertEqual('H', letter_on_the_map)

    def test_moving_the_hero_left_when_there_are_no_obstacles_then_return_true(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/no_obstacles.txt', h, 2)
        d.spawn()
        self.assertTrue(d.move_hero('left'))

    def test_moving_the_hero_left_when_there_are_no_obstacles_then_compare_the_updated_coordinates(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/no_obstacles.txt', h, 2)
        d.spawn()
        old_coordinates_after_update = (d.hero_position_X, d.hero_position_Y - 1)
        d.move_hero('left')
        new_coordinates = (d.hero_position_X, d.hero_position_Y)
        self.assertEqual(old_coordinates_after_update, new_coordinates)

    def test_moving_the_hero_right_when_there_are_no_obstacles_then_return_true(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/no_obstacles.txt', h, 2)
        d.spawn()
        self.assertTrue(d.move_hero('right'))
    
    def test_moving_the_hero_right_when_there_are_no_obstacles_then_compare_the_updated_coordinates(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/no_obstacles.txt', h, 2)
        d.spawn()
        old_coordinates_after_update = (d.hero_position_X, d.hero_position_Y + 1)
        d.move_hero('right')
        new_coordinates = (d.hero_position_X, d.hero_position_Y)
        self.assertEqual(old_coordinates_after_update, new_coordinates)

    def test_moving_the_hero_up_when_there_are_no_obstacles_then_return_true(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/no_obstacles.txt', h, 2)
        d.spawn()
        self.assertTrue(d.move_hero('up'))
    
    def test_moving_the_hero_up_when_there_are_no_obstacles_then_compare_the_updated_coordinates(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/no_obstacles.txt', h, 2)
        d.spawn()
        old_coordinates_after_update = (d.hero_position_X - 1, d.hero_position_Y)
        d.move_hero('up')
        new_coordinates = (d.hero_position_X, d.hero_position_Y)
        self.assertEqual(old_coordinates_after_update, new_coordinates)

    def test_moving_the_hero_down_when_there_are_no_obstacles_then_return_true(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/no_obstacles.txt', h, 2)
        d.spawn()
        self.assertTrue(d.move_hero('down'))
    
    def test_moving_the_hero_down_when_there_are_no_obstacles_then_compare_the_updated_coordinates(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/no_obstacles.txt', h, 2)
        d.spawn()
        old_coordinates_after_update = (d.hero_position_X + 1, d.hero_position_Y)
        d.move_hero('down')
        new_coordinates = (d.hero_position_X, d.hero_position_Y)
        self.assertEqual(old_coordinates_after_update, new_coordinates)

    def test_moving_the_hero_to_an_obstacle_then_return_false(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/test.txt', h, 2)
        d.spawn()
        self.assertFalse(d.move_hero('down'))

    def test_moving_the_hero_out_of_boundaries_of_the_map_then_return_false_and_print_message(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        d = Dungeon('test_maps/test.txt', h, 2)
        d.spawn()
        self.assertFalse(d.move_hero('left'))

    # def test_moving_hero_to_a_treasure_then_return_true_and_print_the_treasure_found(self):
    #     h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
    #     d = Dungeon('test_maps/test.txt', h, 2)
    #     d.spawn()
    #     self.assertTrue(d.move_hero('right'))


if __name__ =='__main__':
    unittest.main()