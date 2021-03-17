import collections


class BattelShip():
    def __init__(self):
        self._battle_ship = collections.defaultdict(lambda : {})

    def Battlecruiser(self) -> dict:
        self._battle_ship["Battlecruiser"] = {
            "Hp" : 50,
            "Armor" : "★★★★★",
            "Power" : "★★★★★",
            "Count" : 0
        }
        print("Ship:  Battlecruiser")
        print("Hp:    {}".format(self._battle_ship["Battlecruiser"]["Hp"]))
        print("Armor: {}".format(self._battle_ship["Battlecruiser"]["Armor"]))
        print("Power: {}".format(self._battle_ship["Battlecruiser"]["Power"]))
        return self._battle_ship
    
    def Destroy(self) -> dict:
        self._battle_ship["Destroyer"] = {
            "Hp" : 30,
            "Armor" : "★★",
            "Power" : "★★★",
            "Count" : 0
        }
        print("Ship:  Destroyer")
        print("Hp:    {}".format(self._battle_ship["Destroyer"]["Hp"]))
        print("Armor: {}".format(self._battle_ship["Destroyer"]["Armor"]))
        print("Power: {}".format(self._battle_ship["Destroyer"]["Power"]))
        return self._battle_ship
  
    def Sailor(self) -> dict:
        self._battle_ship["Sailor"] = {
            "Hp" : 10,
            "Armor" : "★★",
            "Power" : "★★",
            "Count" : 0
        }
        print("Ship:  Sailor")
        print("Hp:    {}".format(self._battle_ship["Sailor"]["Hp"]))
        print("Armor: {}".format(self._battle_ship["Sailor"]["Armor"]))
        print("Power: {}".format(self._battle_ship["Sailor"]["Power"]))
        return self._battle_ship
    
    def Carsona(self) -> dict:
        self._battle_ship["Carsona"] = {
            "Hp" : 5,
            "Armor" : "★",
            "Power" : "★",
            "Count" : 0
        }
        print("Ship:  Carsona")
        print("Hp:    {}".format(self._battle_ship["Carsona"]["Hp"]))
        print("Armor: {}".format(self._battle_ship["Carsona"]["Armor"]))
        print("Power: {}".format(self._battle_ship["Carsona"]["Power"]))
        return self._battle_ship

    
    
 


