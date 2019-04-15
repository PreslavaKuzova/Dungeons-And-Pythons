import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Character import *

class HeroTests(unittest.TestCase):
    def test_init_value(self):
        c = Character(20)
        self.assertEqual(c.get_health(), 20)

    def test_when_damage_is_taken_and_substract_that_much_from_the_health(self):
        c = Character(100)
        c.take_damage(20)
        self.assertEqual(c.get_health(), 80)

    def test_when_damage_taken_is_more_that_the_health_then_health_equals_zero(self):
        c = Character(50)
        c.take_damage(60)
        self.assertEqual(c.get_health(), 0)
    
    def test_when_damage_taken_is_more_that_the_health_then_character_is_dead(self):
        c = Character(50)
        c.take_damage(60)
        self.assertFalse(c.is_alive())

    def test_when_damage_taken_is_less_that_the_health_then_character_is_dead(self):
        c = Character(60)
        c.take_damage(50)
        self.assertTrue(c.is_alive())
    
    def test_when_starting_with_no_health_and_test_whether_it_is_alive(self):
        c = Character(0)
        self.assertFalse(c.is_alive())
    

if __name__ =='__main__':
    unittest.main()