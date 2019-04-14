import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Enemy import *
from Hero import *

class TestEnemy(unittest.TestCase):

    def test_correct_enemy_initialization_of_health(self):
        e = Enemy(100, 20)
        self.assertEqual(e.get_health(), 100)
    
    def test_correct_enemy_initialization_of_attack(self):
        e = Enemy(100, 20)
        self.assertEqual(e.attack(), 20)
        
        
if __name__ =='__main__':
    unittest.main()