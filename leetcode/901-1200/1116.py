# -*- coding: utf-8 -*-
# ======================================
# @File    : 1116.py
# @Time    : 2020/5/2 16:37
# @Author  : Rivarrl
# ======================================
# [1116. 打印零与奇偶数](https://leetcode-cn.com/problems/print-zero-even-odd/)
from algorithm_utils import *
import threading
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.tot = 0
        self.zero_lock = threading.Lock()
        self.even_lock = threading.Lock()
        self.odd_lock = threading.Lock()
        self.even_lock.acquire()
        self.odd_lock.acquire()

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for x in range(self.n):
            self.zero_lock.acquire()
            printNumber(0)
            self.tot += 1
            if self.tot & 1:
                self.odd_lock.release()
            else:
                self.even_lock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for x in range(2, self.n+1, 2):
            self.even_lock.acquire()
            printNumber(self.tot)
            self.zero_lock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for x in range(1, self.n+1, 2):
            self.odd_lock.acquire()
            printNumber(self.tot)
            self.zero_lock.release()

def f1(x): print(x, end='')

if __name__ == '__main__':
    a = ZeroEvenOdd(2)
    A = threading.Thread(target=a.zero, args=(f1,))
    B = threading.Thread(target=a.even, args=(f1,))
    C = threading.Thread(target=a.odd, args=(f1,))
    A.start()
    B.start()
    C.start()