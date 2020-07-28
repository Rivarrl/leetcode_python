# -*- coding: utf-8 -*-
# ======================================
# @File    : 381.py
# @Time    : 2020/7/28 3:20 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import random
from collections import defaultdict

class RandomizedCollection:
    """
    [381. O(1) 时间插入、删除和获取随机元素 - 允许重复](https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed/)
    """
    def __init__(self):
        self.arr = []
        self.d = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.d[val].add(len(self.arr))
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not self.d[val]: return False
        i, j = self.d[val].pop(), len(self.arr)-1
        if i != j:
            self.d[self.arr[j]].add(i)
            self.d[self.arr[j]].remove(j)
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


if __name__ == '__main__':
    rc = RandomizedCollection()
    rc.insert(1)
    rc.remove(1)
    rc.insert(1)
    rc.insert(2)
    rc.getRandom()
    rc.remove(1)
    rc.getRandom()