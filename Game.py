from Dungeon import Dungeon
from Hero import Hero
from Weapon import Weapon
import os
from getch import getch
from print_logo import print_logo
from time import sleep

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def level_readers(path):
    print("----Welcome to Dungeons and Pythons!!!----")
    print("Move your hero with a, w, s, d.")
    print("Press X to exit.")
    name = input("Enter name for your hero: ")
    title = input("Enter your hero's nickname: ")
    h = Hero(name, title, health=100, mana=100, mana_regeneration_rate=2)
    w=Weapon(name='The Axe of Destiny', damage = 10)
    h.equip(w) #there is no hero without weapon. Start game with some
    levels = os.listdir(path)
    levels.sort()
    cls()
    print_logo()
    sleep(3) #wait for 3 seconds


    for idx, lvl in enumerate(levels):
        map = Dungeon(path + '/' + lvl, h, idx+1) 
        map.spawn()
        key = ''
        exited = False
        legit_keys={'a', 'w', 's', 'd', 'x'}
        while map.hero.is_alive(): #does every move
            print('level {}'.format(idx+1))
            map.print_map()
            print("||||HEALTH: {}||||".format(map.hero.get_health()))
            print("||||MANA:   {}||||\n".format(map.hero.get_mana()))
            key = getch()
            cls()
            key = key.lower()

            if key in legit_keys:
                if key == 'a':
                    map.move_hero('left')
                if key == 'd':
                    map.move_hero('right')
                if key == 's':
                    map.move_hero('down')
                if key == 'w':
                    map.move_hero('up')
                if key == 'x':
                    exited = True
                    break

            else:
                print("Invalid command")

            if map.endpoint == (map.hero_position_X, map.hero_position_Y):
                break #we're done here, go to next level
        if exited:
            break
    if map.hero.is_alive() and not exited:
        print("Congratulations! You win!")
    else:
        print("Bye!")

#path to folder, where our files with levels are listed
path = 'levels'
level_readers(path)