import unittest
import sys
sys.path.insert(0, '../')
from Fight import *
from Hero import *
from Enemy import *
from Weapon import *


class TestFight(unittest.TestCase):

    def test_normal_fight_lowers_health(self):
        w = Weapon('The Axe of Destiny', 10)
        h = Hero("Bron", "Dragonslayer", 100, 100, 1)
        h.equip(w)
        e = Enemy(100, 10)
        f = Fight(h, e, [], 3, 3)
        f.fight()

        test_passes = False
        if e.is_alive() is not True or h.is_alive() is not True:
            test_passes = True
        self.assertEqual(test_passes, True)


if __name__ =='__main__':
    unittest.main()