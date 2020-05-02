# -*- coding: utf-8 -*-
# ======================================
# @File    : 1115.py
# @Time    : 2020/5/2 16:21
# @Author  : Rivarrl
# ======================================
# [1115. 交替打印FooBar](https://leetcode-cn.com/problems/print-foobar-alternately/)
from algorithm_utils import *
import threading

class FooBar:
    # 锁机制
    def __init__(self, n):
        self.n = n
        self.foo_lock = threading.Lock()
        self.bar_lock = threading.Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()

def f1(): print('foo', end='')
def f2(): print('bar', end='')

if __name__ == '__main__':
    a = FooBar(2)
    foo = threading.Thread(target=a.foo, args=(f1,))
    bar = threading.Thread(target=a.bar, args=(f2,))
    foo.start()
    bar.start()