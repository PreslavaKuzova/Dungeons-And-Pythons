from Dungeon import Dungeon
from Hero import Hero
from os import listdir

def level_readers(path):
    print("------Welcome to Pythons and Dungeons!!!------")
    print("Move your hero with arrow keys.")
    print("If you'd like to exit game, press esc.")
    name = input("Enter name for your hero: ")
    title = input("Enter your hero's nickname: ")
    h = Hero(name, title, health=100, mana=100, mana_regeneration_rate=2)
    levels = listdir(path)
    levels.sort()

    for lvl in levels:
        #start every level with full health and mana
        map = Dungeon(path + '/' + lvl, h) 
        map.spawn()
        key = ''
        legit_keys={'a', 'w', 's', 'd'}
        while map.hero.is_alive(): #does every move
            map.print_map()
            key = input()
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

            if map.endpoint == (map.hero_position_X, map.hero_position_Y):
                break #we're done here, go to next level

#path to folder, where our files with levels are listed
path = 'levels'
level_readers(path)