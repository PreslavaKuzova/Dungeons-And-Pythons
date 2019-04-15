import unittest
import sys
sys.path.insert(0, '../')
from Weapon import *

class TestWeapon(unittest.TestCase):
    def test_weapon_initialization_data_name(self):
        w = Weapon('The Axe of Destiny', 10)
        expected = 'The Axe of Destiny'
        self.assertEqual(w.name, expected)

    def test_weapon_initialization_data_damage(self):
        w = Weapon('The Axe of Destiny', 10)
        expected = 10
        self.assertEqual(w.damage, expected)


if __name__ =='__main__':
    unittest.main()