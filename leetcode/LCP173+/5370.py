# -*- coding: utf-8 -*-
# ======================================
# @File    : 5370.py
# @Time    : 2020/3/29 10:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class UndergroundSystem:

    def __init__(self):
        self.d = {}
        self.c1 = {}
        self.c2 = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.d[id] = stationName, t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        s1, t1 = self.d[id]
        self.d.pop(id)
        k = (s1, stationName)
        self.c1[k] = self.c1.get(k, 0) + t - t1
        self.c2[k] = self.c2.get(k, 0) + 1

    @timeit
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        k = (startStation, endStation)
        if not k in self.c2: return -1.0
        return self.c1[k] / self.c2[k]


if __name__ == '__main__':
    undergroundSystem = UndergroundSystem()
    undergroundSystem.checkIn(45, "Leyton", 3)
    undergroundSystem.checkIn(32, "Paradise", 8)
    undergroundSystem.checkIn(27, "Leyton", 10)
    undergroundSystem.checkOut(45, "Waterloo", 15)
    undergroundSystem.checkOut(27, "Waterloo", 20)
    undergroundSystem.checkOut(32, "Cambridge", 22)
    undergroundSystem.getAverageTime("Paradise", "Cambridge")
    undergroundSystem.getAverageTime("Leyton", "Waterloo")
    undergroundSystem.checkIn(10, "Leyton", 24)
    undergroundSystem.getAverageTime("Leyton", "Waterloo")
    undergroundSystem.checkOut(10, "Waterloo", 38)
    undergroundSystem.getAverageTime("Leyton", "Waterloo")

