# Dungeons-And-Pythons
This is a  a simple, 2D turn-based console game. 

## Character class
As our Hero and our Enemies have similar traits, we decided to create a parent class which will be inherited by both. 
Character class takes the health and manages it.

* **get_health()** returns the health of the hero/enemy 

* **is_alive()** returns True or False depending on the current health points

* **take_damage()** reduces the health points of the hero/enemy. If we inflict more damage than we have health, health will always be equal to zero and we cannot get below that!


## Hero
Every hero starts with the given health and mana points.
Those health and mana points are the maximum health and mana for the hero!
When a hero reaches 0 health he is considered dead.
When a hero reaches 0 mana, he cannot cast any spells

* **known_as()** which returns a string, formatted in the following way: "{hero_name} the {hero_title}"

* **is_alive()** returns True, if our hero is still alive. Otherwise - False.

* **get_health()** returns the current health

* **get_mana()** which returns the current mana

* **can_cast()** which returns True, if our hero can cast the magic he has been given. Otherwise - False

* **take_healing(healing_points)** heals our hero. Our hero can also be healed! If our hero is dead, the method should return False. It's too late to heal our hero
We cannot heal our hero above the maximum health, which is given by health. If healing is successful (our hero is not dead), the method should return True.

* **take_mana(mana_points)** increces the mana by mana_points

Our hero can also increase his mana in two ways:
Each time he makes a move, his mana is increased by **mana_regeneration_rate** amount.
He can drink a mana potion, which will increse his mana by the amount of mana points the potion have.
Hero's mana cannot go above the start mana given to him, neither he can go down below 0 mana.

* **equip(weapon)** and **learn(spell)**

Our hero can equip one weapon and one spell in order to have damage. Our hero can learn only 1 spell and be equapped with only 1 weapon at a time.
If you learn a given spell, and after this learn another one, the hero can use only the latest.

* **attack()** returns the demage done either from the weapon or from the spell. 

If the hero has not been equiped with weapon or he has no spells, his attack points are 0.
attack(by="weapon") - returns the damage of the weapon if equiped or 0 otherwise
attack(by="magic") - returns the damage of the spell, if quiped or 0 otherwise\

# Enemy
Enemies have starting damage, which is different from a weapon or a spell. 
They cannot equip weapons or learn spells but it is not required for them in order to deal damage, as it is for our hero.
* **attack()** returns the demage done by the enemy

# Weapons and Spells
These two classes have been implemented with the help of .json files that contain the information for the weapons' and spells' attributes. In order for our hero to have proper damage, he must be equiped with either a weapon or a spell. One hero can carry at max 1 weapon and 1 spell.

# Dungeon
This is where the map of the game is loaded. We decided that we want more than one level in our game and this is why we created a folder that contains the txt files with the maps.

* **move_hero(direction)** where direction is either "up", "down", "left" and "right"

This should move our hero in the desired direction.
Return True if he can move into that direction or Fasle otherwise.

* **fill_tmp_map()** creates a list with the characters given in the map. 

We load the maps from a txt file.

* **spawn()** spawns our hero on the first S that is given on the map
* **treasure_found()**

Once we step on a 'T' on our map this means we have found a treasue. It can either be mana, health, weapon or a spell. A random functions decides and automatically adds it to the attributes.

* **hero_attack()** returns True if the damage done by the hero is more than 0 and False in the other cases
* **get_end_point()** returns a tuple with the coordinates of the endpoint 'G' 

# Fight
Our hero must fight his enemies in order to reach the exit of the dungeon.Our hero walks into the same position as the enemy - then the fights start automatically. Our hero is within some range of the enemy and triggers hero_attack method call. Then we can attack our enemy, but our enemy must walk to our place in order to start attacking us. This is really helpful with spells!

* **fight()** starts a fight when our hero is on the same cell of the map
* **remote_fight()** starts the fight from distance when our hero casts a spell and there is an enemy in it's range

The fight follows this algorithm:
* Our hero always attacks first
* We always use the attack that uses more damage
* If our weapon and our spell deals the same amount of damage, the hero uses the spell first.
* When then hero runs out of mana, he uses the weapon (if he has any)

