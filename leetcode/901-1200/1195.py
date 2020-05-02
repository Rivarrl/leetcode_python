# -*- coding: utf-8 -*-
# ======================================
# @File    : 1195.py
# @Time    : 2020/5/2 17:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

import threading
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n + 1
        self.fz = threading.Semaphore(0)
        self.bz = threading.Semaphore(0)
        self.fzbz = threading.Semaphore(0)
        self.nm = threading.Semaphore(1)

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n):
            if i % 3 == 0 and i % 5 != 0:
                self.fz.acquire()
                printFizz()
                self.nm.release()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n):
            if i % 3 != 0 and i % 5 == 0:
                self.bz.acquire()
                printBuzz()
                self.nm.release()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n):
            if i % 3 == 0 and i % 5 == 0:
                self.fzbz.acquire()
                printFizzBuzz()
                self.nm.release()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n):
            self.nm.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.fzbz.release()
            elif i % 3 == 0:
                self.fz.release()
            elif i % 5 == 0:
                self.bz.release()
            else:
                printNumber(i)
                self.nm.release()


def f1(): print('fizz', end=',')
def f2(): print('buzz', end=',')
def f3(): print('fizzbuzz', end=',')
def f4(x): print(x, end=',')

if __name__ == '__main__':
    a = FizzBuzz(9)
    A = threading.Thread(target=a.fizz, args=(f1,))
    B = threading.Thread(target=a.buzz, args=(f2,))
    C = threading.Thread(target=a.fizzbuzz, args=(f3,))
    D = threading.Thread(target=a.number, args=(f4, ))
    A.start()
    B.start()
    C.start()
    D.start()