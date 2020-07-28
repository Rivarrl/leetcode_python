# -*- coding: utf-8 -*-
# ======================================
# @File    : 380.py
# @Time    : 2020/7/28 1:32 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import random

class RandomizedSet:
    """
    [380. 常数时间插入、删除和获取随机元素](https://leetcode-cn.com/problems/insert-delete-getrandom-o1/)
    """
    def __init__(self):
        self.rs = []
        self.d = {}

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.rs)
        self.rs.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.d:
            self.rs[self.d[val]] = self.rs[-1]
            self.d[self.rs[self.d[val]]] = self.d[val]
            self.rs.pop()
            del self.d[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.rs)


if __name__ == '__main__':
    rs = RandomizedSet()
    rs.insert(0)
    rs.insert(1)
    rs.remove(0)
    rs.insert(2)
    rs.remove(1)
    rs.getRandom()
