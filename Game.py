from Dungeon import Dungeon
from Hero import Hero

h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
map = Dungeon('levels/level1.txt')
map.print_map()
map.spawn(h)
map.print_map()