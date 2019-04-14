import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Hero import Hero
from Weapon import Weapon
from Spell import Spell
class HeroTests(unittest.TestCase):
    def test_known_as(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        expected = 'Bron the Dragonslayer'
        returned = h.known_as()
        self.assertEqual(returned, expected)

    def test_get_health(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.assertEqual(h.get_health(), 100)

    def test_get_mana(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.assertEqual(h.get_mana(), 100)

    def test_is_alive_if_alive(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.assertTrue(h.is_alive())

    def test_is_alive_if_not_alive(self):
        h = Hero(name="Bron", title="Dragonslayer", health=0, mana=100, mana_regeneration_rate=2)
        self.assertFalse(h.is_alive())

    def test_can_cast_if_possible(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        spell = Spell('abra kadabra', 30, 20, 2)
        h.learn(spell)
        self.assertTrue(h.can_cast())

    def test_can_cast_if_no_enough_mana(self):
            h = Hero(name="Bron", title="Dragonslayer", health=100, mana=0, mana_regeneration_rate=2)
            self.assertFalse(h.can_cast())

    def test_take_damage_and_not_dead(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        h.take_damage(50)
        self.assertEqual(h.health, 50)

    def test_take_damage_and_die(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        h.take_damage(120)
        self.assertEqual(h.health, 0)

    def test_take_healing_but_not_reach_max(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        h.health = 10
        h.take_healing(70)
        self.assertEqual(h.health, 80)

    def test_take_healing_and_overflow_max(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        h.take_healing(50)
        self.assertEqual(h.health, 100)

    def test_take_mana_but_not_reach_max(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        h.mana = 10
        h.take_mana(70)
        self.assertEqual(h.mana, 80)

    def test_take_mana_and_overflow_max(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        h.take_mana(50)
        self.assertEqual(h.mana, 100)


    def test_equip_weapon(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        wpn = Weapon('sword', 20)
        h.equip(wpn)
        self.assertEqual(h.equiped, wpn)

    def test_learn_spell(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        spell = Spell('abra kadabra', 30, 20, 2)
        h.learn(spell)
        self.assertEqual(h.spell, spell)

    def test_attack_without_weapon_or_spell(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        damage = h.attack()
        self.assertEqual(damage, 0)


    def test_attack_with_weapon_if_hero_has_weapon(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        wpn = Weapon('sword', 20)
        h.equip(wpn)
        damage = h.attack(by='weapon')
        self.assertEqual(damage, 20)

    def test_attack_with_weapon_if_hero_doesnt_have_weapon(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        damage = h.attack(by='weapon')
        self.assertEqual(damage, 0)

    def test_attack_with_spell_if_hero__doesnt_know_spell(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        self.assertEqual(h.attack(by='magic'), 0)

    def test_attack_with_spell_if_hero_knows_spell_and_has_enough_mana(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        spell = Spell('abra kadabra', 30, 20, 2)
        h.learn(spell)
        damage = h.attack(by='magic')
        self.assertEqual(damage, 30)


    def test_attack_with_spell_if_hero_knows_spell_and_doesnt_have_enough_mana(self):
        h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
        spell = Spell('abra kadabra', 30, 120, 2)
        h.learn(spell)
        damage = h.attack(by='magic')
        self.assertEqual(damage, 0)



if __name__ =='__main__':
    unittest.main()