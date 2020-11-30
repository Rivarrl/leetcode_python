# -*- coding: utf-8 -*-
# ======================================
# @File    : 1603.py
# @Time    : 2020/10/31 11:58
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class ParkingSystem:
    """
    [1603. 设计停车系统](https://leetcode-cn.com/problems/design-parking-system/)
    """
    def __init__(self, big: int, medium: int, small: int):
        self.arr = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.arr[carType-1] == 0: return False
        self.arr[carType-1] -= 1
        return True


if __name__ == '__main__':
    a = ParkingSystem(1,1,0)
    a.addCar(1)
    a.addCar(2)
    a.addCar(3)
    a.addCar(1)
