# -*- coding: utf-8 -*-
# ======================================
# @File    : 5123.py
# @Time    : 2019/12/14 22:49
# @Author  : Rivarrl
# ======================================
from itertools import combinations

class CombinationIterator:
    """
    [5123. 字母组合迭代器](https://leetcode-cn.com/problems/iterator-for-combination/)
    """
    def __init__(self, characters: str, combinationLength: int):
        self.arr = list(combinations(characters, combinationLength))
        self.size = len(self.arr)
        self.cur = 0

    def next(self) -> str:
        ret = ''.join(self.arr[self.cur])
        self.cur += 1
        return ret

    def hasNext(self) -> bool:
        return self.cur < self.size

if __name__ == '__main__':
    # Your CombinationIterator object will be instantiated and called as such:
    obj = CombinationIterator("abc", 2)
    while obj.hasNext():
        print(obj.next())
