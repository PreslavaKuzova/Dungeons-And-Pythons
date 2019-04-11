from Dungeon import Dungeon
from Hero import Hero
import os
from getch import getch
from print_logo import print_logo
from time import sleep

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def level_readers(path):
    print("----Welcome to Dungeons and Pythons!!!----")
    print("Move your hero with arrow keys.")
    print("Press X to exit.")
    name = input("Enter name for your hero: ")
    title = input("Enter your hero's nickname: ")
    h = Hero(name, title, health=100, mana=100, mana_regeneration_rate=2)
    levels = os.listdir(path)
    levels.sort()
    cls()
    print_logo()
    sleep(3) #wait for 3 seconds


    for idx, lvl in enumerate(levels):
        #start every level with full health and mana
        map = Dungeon(path + '/' + lvl, h) 
        map.spawn()
        key = ''
        exited = False
        legit_keys={'a', 'w', 's', 'd'}
        while map.hero.is_alive(): #does every move
            print('level {}'.format(idx+1))
            map.print_map()
            print("||||HEALTH: {}||||".format(map.hero.get_health()))
            print("||||MANA:   {}||||\n".format(map.hero.get_mana()))
            key = getch()
            cls()
            key = key.lower()
            if key == 'x':
                exited = True
                break

            if key in legit_keys:
                if key == 'a':
                    map.move_hero('left')
                if key == 'd':
                    map.move_hero('right')
                if key == 's':
                    map.move_hero('down')
                if key == 'w':
                    map.move_hero('up')

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