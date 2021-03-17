import collections
import Ships_info
import MakeShips
import msvcrt
from typing import List
import os
import numpy as np
import copy
import time
import EasyMode

def make_filed(ships : dict, info : List, size : int, computer : dict, cp_info : List) -> None:
    size_field = [["■" for _ in range(size)] for _ in range(size)]
    copy_ships = ships
    for k in range(0,len(ships)):
        if ships.get("Cruiser"):
            size_field = MakeShips.make_battlecruiser(ships,info,size,size_field)
            del ships["Cruiser"]
        if ships.get("Troyer"):
            size_field = MakeShips.make_Destroyer(ships,info,size,size_field)
            del ships["Troyer"]
        if ships.get("Ailor"):
            size_field = MakeShips.make_Ailor(ships,info,size,size_field)
            del ships["Ailor"]
        if ships.get("Carso"):
            size_field = MakeShips.make_Carso(ships,info,size,size_field)
            del ships["Carso"]
    computer_field = [["■" for _ in range(size)] for _ in range(size)]
    copy_ships = computer
    for k in range(0,len(computer)):
        if computer.get("Cruiser"):
            computer_field = MakeShips.make_battlecruiser(computer,cp_info,size,computer_field)
            del computer["Cruiser"]
        if computer.get("Troyer"):
            computer_field = MakeShips.make_Destroyer(computer,cp_info,size,computer_field)
            del computer["Troyer"]
            
    return size_field,computer_field



class_battle = Ships_info.BattelShip()

def choose_ship() -> (List,dict,int):
    info_list = []
    computer_list = []
    battle_ship = collections.defaultdict(lambda : {})
    computer_ship = collections.defaultdict(lambda : {})
    while True:
        os.system("cls")
        print("Minimum size of the field -> 12 x 12")
        print("Maximum size of the field -> 50 x 50")
        filed_size = int(input("Enter the size of the filed (? x ?) : "))
        if filed_size >= 12 and filed_size <= 50:
            break
    max_hp = (int(filed_size / 6) * 100)
    cpy_max = max_hp
    
    '''
        There are some errors with Destrotyer, Sailor and Carsona. Need to fix it.
        Choose battlecruiser only.
    '''

    while max_hp > 0:
        os.system("cls")
        print("1: Battlecruiser(Hp: 50)   2: Destroyer(Hp: 30)   3: Sailor(Hp: 10)   4: Carsona(Hp: 5)")
        print("The maximum hp you can choose -> [{}]".format(int(max_hp)))
        ship = int(input("Choose your battleship: "))
        if ship == 1 and max_hp >= 50:
            if not battle_ship.get("Cruiser"):
                battle_ship["Cruiser"] = class_battle.Battlecruiser()
            battle_ship["Cruiser"]["Battlecruiser"]["Count"] += 1
            max_hp = max_hp - battle_ship["Cruiser"]["Battlecruiser"]["Hp"]
            info_list.append(ship)
            os.system("pause")
        elif ship == 2 and max_hp >= 30:
            if not battle_ship.get("Troyer"):
                battle_ship["Troyer"] = class_battle.Destroy()
            battle_ship["Troyer"]["Destroyer"]["Count"] += 1
            max_hp = max_hp - battle_ship["Troyer"]["Destroyer"]["Hp"]
            info_list.append(ship)
            os.system("pause")
        elif ship == 3 and max_hp >= 10:
            if not battle_ship.get("Ailor"):
                battle_ship["Ailor"] = class_battle.Sailor()
            battle_ship["Ailor"]["Sailor"]["Count"] += 1
            max_hp = max_hp - battle_ship["Ailor"]["Sailor"]["Hp"]
            info_list.append(ship)
            os.system("pause")
        elif ship == 4 and max_hp >= 5:
            if not battle_ship.get("Carso"):
                battle_ship["Carso"] = class_battle.Carsona()
            battle_ship["Carso"]["Carsona"]["Count"] += 1
            max_hp = max_hp - battle_ship["Carso"]["Carsona"]["Hp"]
            info_list.append(ship)
            os.system("pause")
        else:
            continue
    max_hp = cpy_max
    print("*" * 5,"Computer choose the ships", "*" * 5)
    print()
    print()
    

    '''
        Computer only choose battlecruiser. 
        Other battleships have not been implemented yet. 
    '''
    while max_hp >= 0:
        os.system("cls")
        if not computer_ship.get("Cruiser"):
            computer_ship["Cruiser"] = class_battle.Battlecruiser()
        computer_ship["Cruiser"]["Battlecruiser"]["Count"] += 1
        max_hp = max_hp - computer_ship["Cruiser"]["Battlecruiser"]["Hp"]
        computer_list.append(1)
        print("*" * 5," Computer chose the Battlecruiser. ", "*" * 5)
        os.system("pause")
    return info_list, battle_ship, filed_size,cpy_max,computer_ship,computer_list


info_list, battle_ship, filed_size,max_hp,computer_ship,computer_list = choose_ship()
size_field,computer_field = make_filed(battle_ship,info_list,filed_size,computer_ship,computer_list)
EasyMode.play_game(battle_ship,size_field,filed_size,max_hp,computer_field)
