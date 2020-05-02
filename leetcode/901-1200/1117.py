# -*- coding: utf-8 -*-
# ======================================
# @File    : 1117.py
# @Time    : 2020/5/2 17:08
# @Author  : Rivarrl
# ======================================
# [1117. H2O 生成](https://leetcode-cn.com/problems/building-h2o/)
from algorithm_utils import *
import threading
class H2O:
    # 信号量
    def __init__(self):
        self.o = threading.Semaphore(0)
        self.h = threading.Semaphore(2)
        self.ctr_h = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.acquire()
        releaseHydrogen()
        if self.ctr_h == 0:
            self.ctr_h += 1
        else:
            self.o.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.acquire()
        releaseOxygen()
        self.ctr_h = 0
        self.h.release()
        self.h.release()

from collections import deque
class H2O_2:
    # 双向队列
    def __init__(self):
        self.h = deque()
        self.o = deque()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.append(releaseHydrogen)
        self.run()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.append(releaseOxygen)
        self.run()

    def run(self):
        if len(self.h) > 1 and len(self.o) > 0:
            self.h.popleft()()
            self.h.popleft()()
            self.o.popleft()()

def f1(): print('H', end='')
def f2(): print('O', end='')

def f3(s):
    for c in s:
        if c == 'H':
            x = threading.Thread(target=a.hydrogen, args=(f1,))
        else:
            x = threading.Thread(target=a.oxygen, args=(f2,))
        x.start()

if __name__ == '__main__':
    a = H2O_2()
    example = 'OOHHHH'
    X = threading.Thread(target=f3, args=(example,))
    X.start()
