# -*- coding: utf-8 -*-
# ======================================
# @File    : 03-06.py
# @Time    : 2020/9/18 0:23
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from collections import deque

class AnimalShelf:
    """
    [面试题 03.06. 动物收容所](https://leetcode-cn.com/problems/animal-shelter-lcci/)
    """
    def __init__(self):
        self.tot = 0
        self.arr_cat = deque()
        self.arr_dog = deque()

    def enqueue(self, animal: List[int]) -> None:
        p = self.arr_dog if animal[1] else self.arr_cat
        p.append((animal[0],self.tot))
        self.tot += 1

    def dequeueAny(self) -> List[int]:
        c = (-1,self.tot) if not self.arr_cat else self.arr_cat[0]
        d = (-1,self.tot) if not self.arr_dog else self.arr_dog[0]
        if c[1] == d[1]:
            return [-1, -1]
        elif c[1] < d[1]:
            return [self.arr_cat.popleft()[0], 0]
        else:
            return [self.arr_dog.popleft()[0], 1]

    def dequeueDog(self) -> List[int]:
        if not self.arr_dog: return [-1, -1]
        return [self.arr_dog.popleft()[0], 1]

    def dequeueCat(self) -> List[int]:
        if not self.arr_cat: return [-1, -1]
        return [self.arr_cat.popleft()[0], 0]


if __name__ == '__main__':
    a = AnimalShelf()
    a.enqueue([0, 0])
    a.enqueue([1, 0])
    a.dequeueCat()
    a.dequeueDog()
    a.dequeueAny()