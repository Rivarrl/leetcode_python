# -*- coding: utf-8 -*-
# ======================================
# @File    : 284.py
# @Time    : 2019/11/13 10:29
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

# Below is the interface for Iterator, which is already defined for you.

class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.pointer = 0
        self.size = len(nums)

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.pointer < self.size

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        if self.hasNext():
            element = self.nums[self.pointer]
            self.pointer += 1
            return element
        else:
            raise Exception("没了")

class PeekingIterator:
    """
    [284. 顶端迭代器](https://leetcode-cn.com/problems/peeking-iterator/)
    思路：Iterator只有next能看元素，peek的方法只看不删的话，就把next删掉的先缓存一下
    """
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.cache = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.cache != None:
            return self.cache
        elif self.hasNext():
            self.cache = self.next()
            return self.cache

    def next(self):
        """
        :rtype: int
        """
        if self.cache != None:
            c = self.cache
            self.cache = None
            return c
        elif self.hasNext():
            return self.iterator.next()
        else:
            raise Exception("没了")

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cache != None or self.iterator.hasNext()

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    iter = PeekingIterator(Iterator(nums))
    while iter.hasNext():
        val = iter.peek()
        print(val)
        iter.next()