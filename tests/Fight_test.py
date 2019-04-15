import unittest
import sys
sys.path.insert(0, '../')
from Fight import *
from Hero import *
from Enemy import *
from Weapon import *


class FightTest(unittest.TestCase):
    def test_fight_lowers_health(self):
        h = Hero("Bron", "Dragonslayer", 100, 100, 1)
        e = Enemy(100, 10)
        f = Fight(h, e, [], 3, 3)
        f.fight()



if __name__ =='__main__':
    unittest.main()