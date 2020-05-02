# -*- coding: utf-8 -*-
# ======================================
# @File    : 1114.py
# @Time    : 2020/5/2 15:26
# @Author  : Rivarrl
# ======================================
# [1114. 按序打印](https://leetcode-cn.com/problems/print-in-order/)
from algorithm_utils import *
import threading
class Foo:
    """
    使用锁机制
    """
    def __init__(self):
        self.first_fin = threading.Lock()
        self.second_fin = threading.Lock()
        self.first_fin.acquire()
        self.second_fin.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_fin.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.first_fin:
            printSecond()
            self.second_fin.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.second_fin:
            printThird()


def f1(): print('one', end='')
def f2(): print('two', end='')
def f3(): print('three', end='')

if __name__ == '__main__':
    a = Foo()
    callable_list = [a.first, a.second, a.third]
    callable_args = [f1, f2, f3]
    x = [2,1,3]
    tr = []
    for e in x:
        tr.append(threading.Thread(target=callable_list[e-1], args=(callable_args[e-1],)))
    for t in tr:
        t.start()