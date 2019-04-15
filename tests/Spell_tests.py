import unittest
import sys
sys.path.insert(0, '../')
from Spell import *

class TestSpell(unittest.TestCase):
    def test_spell_initialization_data_name(self):
        s = Spell("Riddikulus", 25, 30, 2)
        expected = "Riddikulus"
        self.assertEqual(s.name, expected)
    
    def test_spell_initialization_data_damage(self):
        s = Spell("Riddikulus", 25, 30, 2)
        expected = 25
        self.assertEqual(s.damage, expected)

    def test_spell_initialization_data_mana_cost(self):
        s = Spell("Riddikulus", 25, 30, 2)
        expected = 30
        self.assertEqual(s.mana_cost, expected)

    def test_spell_initialization_data_cast_range(self):
        s = Spell("Riddikulus", 25, 30, 2)
        expected = 2
        self.assertEqual(s.cast_range, expected)
        

if __name__ =='__main__':
    unittest.main()