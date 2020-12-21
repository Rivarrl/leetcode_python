# -*- coding: utf-8 -*-
# ======================================
# @File    : 641.py
# @Time    : 2020/12/21 10:00 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Node:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None

class MyCircularDeque:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = 0
        self.max_size = k
        self.head = self.tail = None

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull(): return False
        cur = Node(value)
        if self.isEmpty():
            self.head = self.tail = cur
            self.head.pre = self.tail
            self.tail.next = self.head
        else:
            self.head.pre, cur.next, self.tail.next, cur.pre = cur, self.head, cur, self.tail
            self.head = cur
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull(): return False
        cur = Node(value)
        if self.isEmpty():
            self.head = self.tail = cur
            self.head.next = self.tail
            self.tail.pre = self.head
        else:
            self.tail.next, cur.next, self.head.pre, cur.pre = cur, self.head, cur, self.tail
            self.tail = cur
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        if self.size == 1:
            self.head = self.tail = None
        else:
            last = self.head
            self.tail.next = last.next
            last.next.pre = self.tail
            self.head = last.next
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        if self.size == 1:
            self.head = self.tail = None
        else:
            last = self.tail
            self.head.pre = last.pre
            last.pre.next = self.head
            self.tail = last.pre
        self.size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty(): return -1
        return self.head.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty(): return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.max_size

if __name__ == '__main__':
    a = MyCircularDeque(3)
    print(a.insertLast(1))
    print(a.insertLast(2))
    print(a.insertFront(3))
    print(a.insertFront(4))
    print(a.getRear())
    print(a.isFull())
    print(a.deleteLast())
    print(a.insertFront(4))
    print(a.getFront())
