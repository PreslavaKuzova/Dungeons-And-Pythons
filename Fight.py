from Hero import Hero
from Enemy import Enemy
class Fight:
    def __init__(self, hero:Hero, enemy:Enemy):
        self.hero = hero
        self.enemy = enemy

    def fight(self):
        #fight till death
        while self.hero.is_alive() and self.enemy.is_alive():
            #hero attacks first
            curr_hero_damage_by_weapon = 0
            curr_hero_damage_by_magic = 0
            try:
                curr_hero_damage_by_weapon = self.hero.equiped.damage
            except:
                pass
            
            try:
                if self.hero.can_cast():
                    curr_hero_damage_by_magic = self.hero.spell.damage
            except:
                pass
           
           #use the attack that deals more damage
            if curr_hero_damage_by_magic >= curr_hero_damage_by_weapon:
                made_dmg = self.hero.attack(by='magic')
            else:
                made_dmg = self.hero.attack(by='weapon')

            self.enemy.take_healing(-made_dmg) #apply damage on the enemy

            #if enemy is still alive, he attacks
            if self.enemy.is_alive():
                curr_enemy_damage_by_weapon = 0
                curr_enemy_damage_by_magic = 0
                try:
                    curr_enemy_damage_by_weapon = self.enemy.equiped.damage
                except:
                    pass
            
                try:
                    if self.enemy.can_cast():
                        curr_enemy_damage_by_magic = self.enemy.spell.damage
                except:
                    pass
           
                #use the attack that deals more damage
                max_dmg = max(curr_enemy_damage_by_magic, curr_enemy_damage_by_weapon, self.enemy.damage)
                if curr_enemy_damage_by_magic == max_dmg:
                    made_dmg = self.enemy.attack(by='magic')
                elif curr_enemy_damage_by_weapon == max_dmg:
                    made_dmg = self.enemy.attack(by='weapon')
                else:
                    made_dmg = self.enemy.attack()

                self.hero.take_healing(-made_dmg) #apply damage on the hero


    def start_remote_battle(self, curr_x, curr_y):
        try:
            rng = self.hero.spell.cast_range
        except:
            rng = 0
        low_x = curr_x - rng if curr_x - rng > 0 else 0
        up_x = curr_x + rng if curr_x + rng <= self.X else self.X
        low_y = curr_y - rng if curr_y - rng > 0 else 0
        up_y = curr_y + rng if curr_y + rng <= self.Y else self.Y
        for x in range(low_x, up_x):
            for y in range(low_y, up_y):
                if self.tmp_map[x][y] == 'E':
                    enemy = Enemy(self.level*15, self.level*15, self.level*10)
                    #start a fight
                    