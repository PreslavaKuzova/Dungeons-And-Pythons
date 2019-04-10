import unittest
from Hero import Hero
class HeroTests(unittest.TestCase):
    #create test object
    h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
    def test_known_as(self):
        expected = 'Bron the Dragonslayer'
        returned = h.known_as
        self.assertEquals(returned, expected)

    def test_get_health(self):
        self.assertEquals(h.get_health, 100)

    def test_get_mana(self):
        self.assertEquals(h.get_mana, 100)