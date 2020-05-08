# -*- coding: utf-8 -*-
# ======================================
# @File    : 341.py
# @Time    : 2020/5/8 16:26
# @Author  : Rivarrl
# ======================================
# [341. 扁平化嵌套列表迭代器](https://leetcode-cn.com/problems/flatten-nested-list-iterator/)
from algorithm_utils import *

class NestedInteger:
    def __init__(self, val):
        self.val = val

    def isInteger(self) -> bool:
        return isinstance(self.val, int)

    def getInteger(self) -> int:
        return self.val if self.isInteger() else None

    def getList(self) -> ['NestedInteger']:
        return self.val if not self.isInteger() else None

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stk = nestedList[::-1]

    def next(self) -> int:
        return self.stk.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stk and not self.stk[-1].isInteger():
            self.stk.extend(self.stk.pop().getList()[::-1])
        return len(self.stk) > 0

if __name__ == '__main__':
    nl = [NestedInteger([NestedInteger(1),NestedInteger(1)]), NestedInteger(2), NestedInteger([NestedInteger(1),NestedInteger(1)])]
    it = NestedIterator(nl)
    res = []
    while it.hasNext():
        res.append(it.next())
    print(res)
    nl = [NestedInteger([NestedInteger(1), NestedInteger([NestedInteger(4), NestedInteger([NestedInteger(6)])])])]
    it = NestedIterator(nl)
    res = []
    while it.hasNext():
        res.append(it.next())
    print(res)