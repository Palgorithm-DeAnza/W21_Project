import numpy as np
from typing import List


'''
    There are some errors with making battleships in field. Need to fix it.
'''



def make_battlecruiser(ships : dict, info : List, size : int, size_field : List) -> List:
    s = []
    count = 0
    while count < ships["Cruiser"]["Battlecruiser"]["Count"]:
        rand1 = list(np.random.choice(range(0,size),1,replace=False))
        if rand1[0] not in s:
            a = np.random.choice(range(1, 3), 1, replace=False)
            if rand1[0] + 4 < len(size_field) and a[0] == 1:
                rand2 = np.random.choice(range(1, size), 1)
                for j in range(rand1[0], rand1[0] + 5):
                    if size_field[j][rand2[0]] == "▣" or size_field[j][rand2[0]] == "◎" or size_field[j][rand2[0]] == "◐" or size_field[j][rand2[0]] == "◑":
                        rand2[0] = -1
                        break
                if rand2[0] == -1:
                    rand1.pop()
                    continue
                else:
                    for k in range(rand1[0], rand1[0] + 5):
                        size_field[k][rand2[0]] = "◎"
                count += 1
            elif rand1[0] + 4 < len(size_field) and a[0] == 2:
                rand2 = np.random.choice(range(1, size), 1)
                for j in range(rand1[0], rand1[0] + 5):
                    if size_field[rand1[0]][j] == "▣" or size_field[rand1[0]][j] == "◎" or size_field[rand1[0]][j] == "◐" or size_field[rand1[0]][j] == "◑":
                        rand2[0] = -1
                        break
                if rand2[0] == -1:
                    rand1.pop()
                    continue
                else:
                    for k in range(rand1[0], rand1[0] + 5):
                        size_field[k][rand2[0]] = "◎"
                count += 1
            else:
                rand1.pop()
                continue
        else:
            del rand1[0]
            continue
        s.append(rand1[0])
        rand1.pop()
    return size_field



def make_Destroyer(ships : dict, info : List, size : int, size_field : List) -> List:
    s = []
    count = 0
    while count < ships["Troyer"]["Destroyer"]["Count"]:
        rand1 = list(np.random.choice(range(0,size),1,replace=False))
        if rand1[0] not in s:
            a = np.random.choice(range(1, 3), 1, replace=False)
            if rand1[0] + 2 < len(size_field) and a[0] == 1:
                rand2 = np.random.choice(range(1, size), 1)
                for j in range(rand1[0], rand1[0] + 3):
                    if size_field[j][rand2[0]] == "▣" or size_field[j][rand2[0]] == "◎" or size_field[j][rand2[0]] == "◐" or size_field[j][rand2[0]] == "◑":
                        rand2[0] = -1
                        break
                if rand2[0] == -1:
                    rand1.pop()
                    continue
                else:
                    for j in range(rand1[0], rand1[0] + 3):
                        size_field[j][rand2[0]] = "▣"
                count += 1
            elif rand1[0] + 2 < len(size_field) and a[0] == 2:
                rand2 = np.random.choice(range(1, size), 1)
                for j in range(rand1[0], rand1[0] + 3):
                    if size_field[rand1[0]][j] == "▣" or size_field[rand1[0]][j] == "◎" or size_field[rand1[0]][j] == "◐" or size_field[rand1[0]][j] == "◑":
                        rand2[0] = -1
                        break
                    size_field[rand1[0]][j] = "▣"
                if rand2[0] == -1:
                    rand1.pop()
                    continue
                else:
                    for j in range(rand1[0], rand1[0] + 3):
                        size_field[rand1[0]][j] = "▣"
                count += 1
            else:
                rand1.pop()
                continue
        else:
            del rand1[0]
            continue
        s.append(rand1[0])
        rand1.pop()
    return size_field


def make_Ailor(ships : dict, info : List, size : int, size_field : List) -> List:
    s = []
    count = 0
    while count < ships["Ailor"]["Sailor"]["Count"]:
        rand1 = list(np.random.choice(range(0,size),1,replace=False))
        if rand1[0] not in s:
            a = np.random.choice(range(1, 3), 1, replace=False)
            if rand1[0] + 1 < len(size_field) and a[0] == 1:
                rand2 = np.random.choice(range(1, size), 1)
                for j in range(rand1[0], rand1[0] + 2):
                    if size_field[j][rand2[0]] == "◐" or size_field[j][rand2[0]] == "▣" or size_field[j][rand2[0]] == "◎" or size_field[j][rand2[0]] == "◑":
                        rand2[0] = -1
                        break
                if rand2[0] == -1:
                    rand1.pop()
                    continue
                else:
                    for j in range(rand1[0], rand1[0] + 2):
                        size_field[j][rand2[0]] = "◐"
                count += 1
            elif rand1[0] + 2 < len(size_field) and a[0] == 2:
                rand2 = np.random.choice(range(1, size), 1)
                for j in range(rand1[0], rand1[0] + 2):
                    if size_field[rand1[0]][j] == "◐" or size_field[rand1[0]][j] == "▣" or size_field[rand1[0]][j] == "◎" or size_field[rand1[0]][j] == "◑":
                        rand2[0] = -1
                        break
                if rand2[0] == -1:
                    rand1.pop()
                    continue
                else:
                    for j in range(rand1[0], rand1[0] + 2):
                        size_field[rand1[0]][j] = "◐"
                count += 1
            else:
                rand1.pop()
                continue
        else:
            del rand1[0]
            continue
        s.append(rand1[0])
        rand1.pop()
    return size_field


def make_Carso(ships : dict, info : List, size : int, size_field : List) -> List:
    s = []
    count = 0
    while count < ships["Carso"]["Carsona"]["Count"]:
        rand1 = list(np.random.choice(range(0,size),1,replace=False))
        if rand1[0] not in s:
            a = np.random.choice(range(1, 3), 1, replace=False)
            if rand1[0] < len(size_field) and a[0] == 1:
                rand2 = np.random.choice(range(1, size), 1)
                for j in range(rand1[0], rand1[0] + 1):
                    if size_field[j][rand2[0]] == "◑" or size_field[j][rand2[0]] == "▣" or size_field[j][rand2[0]] == "◎" or size_field[j][rand2[0]] == "◐":
                        rand2[0] = -1
                        break
                if rand2[0] == -1:
                    rand1.pop()
                    continue
                else:
                    for j in range(rand1[0], rand1[0] + 1):
                        size_field[j][rand2[0]] = "◑"
                count += 1
            elif rand1[0] + 2 < len(size_field) and a[0] == 2:
                rand2 = np.random.choice(range(1, size), 1)
                for j in range(rand1[0], rand1[0] + 1):
                    if size_field[rand1[0]][j] == "◑" or size_field[rand1[0]][j] == "▣" or size_field[rand1[0]][j] == "◎" or size_field[rand1[0]][j] == "◐":
                        rand2[0] = -1
                        break
                if rand2[0] == -1:
                    rand1.pop()
                    continue
                else:
                    for j in range(rand1[0], rand1[0] + 1):
                        size_field[rand1[0]][j] = "◑"
                count += 1
            else:
                rand1.pop()
                continue
        else:
            del rand1[0]
            continue
        s.append(rand1[0])
        rand1.pop()
    return size_field

