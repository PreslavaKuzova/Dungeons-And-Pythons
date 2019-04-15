from Hero import Hero
from Enemy import Enemy
class Fight:
    def __init__(self, hero:Hero, enemy:Enemy, tmp_map, rows, cols):
        self.hero = hero
        self.enemy = enemy
        self.tmp_map = tmp_map
        self.X = rows
        self.Y = cols

    def fight(self):
        #fight till death
        print("A fight is started between our", str(self.hero),"and", str(self.enemy))
        while self.hero.is_alive() and self.enemy.is_alive():
            #hero attacks first
            curr_hero_damage_by_weapon = self.hero.equiped.damage
            if self.hero.can_cast():
                curr_hero_damage_by_magic = self.hero.spell.damage
            else:
                curr_hero_damage_by_magic = 0
           
           #use the attack that deals more damage
            if curr_hero_damage_by_magic >= curr_hero_damage_by_weapon and self.hero.spell.mana_cost <= self.hero.get_mana() :
                made_dmg = self.hero.attack(by='magic')
                print("Hero casts a {} for {} dmg.".format(self.hero.spell.name, made_dmg))
            else:
                made_dmg = self.hero.attack(by='weapon')
                print("Hero hits with {} for {} dmg.".format(self.hero.equiped.name, made_dmg))

            self.enemy.take_damage(made_dmg) #apply damage on the enemy
            print("Enemy health is {}".format(self.enemy.get_health()))

            #if enemy is still alive, he attacks
            if self.enemy.is_alive():
                made_dmg = self.enemy.attack()
                self.hero.take_damage(made_dmg) #apply damage on hero
                print("Enemy hits hero for {}dmg. Hero health is {}".format(made_dmg, self.hero.get_health()))
            else:
                print("Enemy is dead!")

    def remote_battle(self, curr_x, curr_y):
        rng = self.hero.spell.cast_range
        low_x = curr_x - rng if curr_x - rng > 0 else 0
        up_x = curr_x + rng if curr_x + rng <= self.X else self.X
        low_y = curr_y - rng if curr_y - rng > 0 else 0
        up_y = curr_y + rng if curr_y + rng <= self.Y else self.Y

        for x in range(low_x, curr_x): #for every position up of our hero
            if self.tmp_map[x][curr_y] == 'E' and self.hero.can_cast() and self.hero.mana >= self.hero.spell.mana_cost:
                enemy_dmg = self.hero.attack(by='magic')
                self.enemy.take_damage(enemy_dmg)
                print("Hero casts a {}, hits enemy for {}dmg. Enemy health is {}".format(self.hero.spell.name, enemy_dmg, self.enemy.get_health()))
                self.tmp_map[x][curr_y] = '.'
                if self.enemy.is_alive(): #if enemy is still not dead, move down to hero
                    if (x-1, curr_y)!=(curr_x, curr_y): #Hero and enemy are still not on same position
                        self.tmp_map[x][curr_y] = '.'
                        print("Enemy moves one square to the left to get to the hero. This is his move.")
                        if (x+1, curr_y)!=(curr_x, curr_y):
                            self.tmp_map[x+1][curr_y] = 'E'
                        else:
                            self.fight()
                        return
                    else:
                        self.fight()
                        return
                else:
                    self.tmp_map[x][curr_y] = '.'
                    print("Enemy is dead!")
                    return
                

        for x in range(curr_x, up_x): #for every position down of our hero
            if self.tmp_map[x][curr_y] == 'E' and self.hero.can_cast() and self.hero.mana >= self.hero.spell.mana_cost:
                enemy_dmg = self.hero.attack(by='magic')
                self.enemy.take_damage(enemy_dmg)
                print("Hero casts a {}, hits enemy for {}dmg. Enemy health is {}".format(self.hero.spell.name, enemy_dmg, self.enemy.get_health()))
                self.tmp_map[x][curr_y] = '.'
                if self.enemy.is_alive(): #if enemy is still not dead, it moves up to hero
                    if (x+1, curr_y)!=(curr_x, curr_y): #Hero and enemy are still not on same position
                        self.tmp_map[x][curr_y] = '.'
                        print("Enemy moves one square to the left to get to the hero. This is his move.")
                        if (x-1, curr_y)!=(curr_x, curr_y):
                            self.tmp_map[x-1][curr_y] = 'E'
                        else:
                            self.fight()
                        return
                    else:
                        self.fight()
                        return
                else:
                    self.tmp_map[x][curr_y] = '.'
                    print("Enemy is dead!")
                    return
        
        for y in range(low_y, curr_y): #for every position left of our hero
            if self.tmp_map[curr_x][y] == 'E' and self.hero.can_cast() and self.hero.mana >= self.hero.spell.mana_cost:
                enemy_dmg = self.hero.attack(by='magic')
                self.enemy.take_damage(enemy_dmg)
                print("Hero casts a {}, hits enemy for {}dmg. Enemy health is {}".format(self.hero.spell.name, enemy_dmg, self.enemy.get_health()))
                self.tmp_map[curr_x][y] = '.'
                if self.enemy.is_alive(): #if enemy is still not dead, move right to hero
                    if (curr_x, y+1)!=(curr_x, curr_y): #Hero and enemy are still not on same position
                        self.tmp_map[curr_x][y] = '.'
                        print("Enemy moves one square to the left to get to the hero. This is his move.")
                        if (curr_x, y+1)!=(curr_x, curr_y):
                            self.tmp_map[curr_x][y+1] = 'E'
                        else:
                            self.fight()
                        return
                    else:
                        self.fight()
                        return
                else:
                    self.tmp_map[curr_x][y] = '.'
                    print("Enemy is dead!")
                    return
                            
        for y in range(curr_y, up_y): #for every position righ of our hero
            if self.tmp_map[curr_x][y] == 'E' and self.hero.can_cast() and self.hero.mana >= self.hero.spell.mana_cost:
                enemy_dmg = self.hero.attack(by='magic')
                self.enemy.take_damage(enemy_dmg)
                print("Hero casts a {}, hits enemy for {}dmg. Enemy health is {}".format(self.hero.spell.name, enemy_dmg, self.enemy.get_health()))
                self.tmp_map[curr_x][y] = '.'
                if self.enemy.is_alive(): #if enemy is still not dead, move left to hero
                    if (curr_x, y-1)!=(curr_x, curr_y): #Hero and enemy are still not on same position
                        self.tmp_map[curr_x][y] = '.'
                        print("Enemy moves one square to the left to get to the hero. This is his move.")
                        if (curr_x, y-1)!=(curr_x, curr_y):
                            self.tmp_map[curr_x][y-1] = 'E'
                        else:
                            self.fight()
                        return
                    else:
                        self.fight()
                        return
                else:
                    self.tmp_map[curr_x][y] = '.'
                    print("Enemy is dead!")
                    return