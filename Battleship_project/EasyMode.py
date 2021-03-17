import numpy as np
from typing import List
import os
import copy
import time
import msvcrt



def play_game(ships : dict, size_field : List, size : int, hp : int, computer_field : List) -> None:
    
    xpos,ypos = 0,0
    cp_xpos, cp_ypos = 0,0
    cp_hp = hp 
    original = size_field[ypos][xpos]
    cp_original = computer_field[cp_xpos][cp_ypos]
    copy_list = copy.deepcopy(size_field)
    computer_list = copy.deepcopy(computer_field)
    size_field[ypos][xpos] = "☆"
    while True:
        count = 0
        while True:
            os.system("cls")
            print("*" * 10,"Your Ships","*" * 10)
            for i in range(size):
                for j in range(size):
                    if copy_list[i][j] == "※" or copy_list[i][j] == "Ｏ":
                        print(copy_list[i][j],end=" ")
                    elif size_field[i][j] == "☆":
                        print(size_field[i][j],end=" ")
                    else:
                        print("■",end=" ")
                print()
            if count == 1:
                break
            print("A: Left     D: Right     W: Up      S: Down     M: Attack")
            key = str(msvcrt.getch()).lower()
            if key[2] == "d":
                if xpos + 1 < size:
                    temp = size_field[ypos][xpos+1]
                    size_field[ypos][xpos+1] = "☆"
                    size_field[ypos][xpos] = original
                    original = temp
                    xpos += 1
            
            if key[2] == "a":
                if xpos - 1 >= 0 :
                    temp = size_field[ypos][xpos-1]
                    size_field[ypos][xpos-1] = "☆"
                    size_field[ypos][xpos] = original
                    original = temp
                    xpos -= 1

            if key[2] == 'w':
                if ypos - 1 >= 0 :
                    temp = size_field[ypos -1][xpos]
                    size_field[ypos -1][xpos] = "☆"
                    size_field[ypos][xpos] = original
                    original = temp
                    ypos -= 1
            
            if key[2] == 's':
                if ypos + 1 < size :
                    temp = size_field[ypos +1][xpos]
                    size_field[ypos +1][xpos] = "☆"
                    size_field[ypos][xpos] = original
                    original = temp
                    ypos += 1

            if key[2] == 'm':
                if copy_list[ypos][xpos] == "■":
                    copy_list[ypos][xpos] = "■"
                    count = 1
                elif copy_list[ypos][xpos] == "◎" or  copy_list[ypos][xpos] == "▣":
                    copy_list[ypos][xpos] = "※"
                    print("You hit the ship! its still your turn")
                    hp -= 10
                    os.system("pause")
                elif copy_list[ypos][xpos] == "◐" or copy_list[ypos][xpos] == "◑":
                    copy_list[ypos][xpos] = "※"
                    print("You hit the ship! its still your turn")
                    hp -= 10
                    os.system("pause")
                    hp -= 5      
        print("-"* 30)
        print()
        print("Current Hp:  {}".format(hp))
        print()
        print("You missed the ship!")
        if hp <= 0:
            print("You won!!!")
            break
        os.system("pause")
        cp_list = []
        count = 0
        while True:
            os.system("cls")
            print("Now computer turn. Please wait untill computer choose the point")
            time.sleep(2)
            print("*" * 10,"Computer Ships","*" * 10)
            cp_key = np.random.choice(range(1, 5), 1, replace=False)
            ran_num = np.random.choice(range(1, 5), 1, replace=False)
            if cp_key[0] == 1:
                if cp_xpos + ran_num[0] < size:
                    temp = computer_field[cp_ypos][cp_xpos+ran_num[0]]
                    computer_field[cp_ypos][cp_xpos] = cp_original
                    cp_original = temp
                    cp_xpos += ran_num[0]
                    if computer_list[cp_ypos][cp_xpos] == "■":
                        computer_list[cp_ypos][cp_xpos] = "■"
                        if [cp_ypos,cp_xpos] not in cp_list:
                            count = 1
                        cp_list.append([cp_ypos,cp_xpos])
                    elif computer_list[cp_ypos][cp_xpos] == "◎" or  computer_list[cp_ypos][cp_xpos] == "▣":
                        computer_list[cp_ypos][cp_xpos] = "※"
                        if [cp_ypos,cp_xpos] not in cp_list:
                            print("Computer hit the ship. Computer turn again")
                            os.system("pause")
                            cp_hp -= 10
                        cp_list.append([cp_ypos,cp_xpos])
            
            if cp_key[0] == 2:
                if cp_xpos - ran_num[0] >= 0 :
                    temp = computer_field[cp_ypos][cp_xpos-ran_num[0]]
                    computer_field[cp_ypos][cp_xpos] = cp_original
                    cp_original = temp
                    cp_xpos -= ran_num[0]
                    if computer_list[cp_ypos][cp_xpos] == "■":
                        computer_list[cp_ypos][cp_xpos] = "■"
                        if [cp_ypos,cp_xpos] not in cp_list:
                            count = 1
                        cp_list.append([cp_ypos,cp_xpos])
                    elif computer_list[cp_ypos][cp_xpos] == "◎" or  computer_list[cp_ypos][cp_xpos] == "▣":
                        computer_list[cp_ypos][cp_xpos] = "※"
                        if [cp_ypos,cp_xpos] not in cp_list:
                            print("Computer hit the ship. Computer turn again")
                            os.system("pause")
                            cp_hp -= 10
                        cp_list.append([cp_ypos,cp_xpos])

            if cp_key[0] == 3:
                if cp_ypos - ran_num[0] >= 0 :
                    temp = computer_field[cp_ypos -ran_num[0]][cp_xpos]
                    computer_field[cp_ypos][cp_xpos] = cp_original
                    cp_original = temp
                    cp_ypos -= ran_num[0]
                    if computer_list[cp_ypos][cp_xpos] == "■":
                        computer_list[cp_ypos][cp_xpos] = "■"
                        if [cp_ypos,cp_xpos] not in cp_list:
                            count = 1
                        cp_list.append([cp_ypos,cp_xpos])
                    elif computer_list[cp_ypos][cp_xpos] == "◎" or  computer_list[cp_ypos][cp_xpos] == "▣":
                        computer_list[cp_ypos][cp_xpos] = "※"
                        if [cp_ypos,cp_xpos] not in cp_list:
                            print("Computer hit the ship. Computer turn again")
                            os.system("pause")
                            cp_hp -= 10
                        cp_list.append([cp_ypos,cp_xpos])
            
            if cp_key[0] == 4:
                if cp_ypos + ran_num[0] < size :
                    temp = computer_field[cp_ypos +ran_num[0]][cp_xpos]
                    computer_field[cp_ypos][cp_xpos] = cp_original
                    cp_original = temp
                    cp_ypos += ran_num[0]
                    if computer_list[cp_ypos][cp_xpos] == "■":
                        computer_list[cp_ypos][cp_xpos] = "■"
                        if [cp_ypos,cp_xpos] not in cp_list:
                            count = 1
                        cp_list.append([cp_ypos,cp_xpos])
                    elif computer_list[cp_ypos][cp_xpos] == "◎" or  computer_list[cp_ypos][cp_xpos] == "▣":
                        computer_list[cp_ypos][cp_xpos] = "※"
                        if [cp_ypos,cp_xpos] not in cp_list:
                            print("Computer hit the ship. Computer turn again")
                            os.system("pause")
                            cp_hp -= 10
                        cp_list.append([cp_ypos,cp_xpos])
            for i in range(size):
                for j in range(size):
                    if computer_list[i][j] == "※" or computer_list[i][j] == "Ｏ":
                        print(computer_list[i][j],end=" ")
                    else:
                        print("■",end=" ")
                print()
            if count == 1:
                break
        print()
        print("Current Computer Hp:  {}".format(cp_hp))
        print()
        print("Computer missed the ship. Now its your turn")

        if cp_hp <= 0:
            print("Computer won!!!")
            break
        os.system("pause")