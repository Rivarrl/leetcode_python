# -*- coding: utf-8 -*-
# ======================================
# @File    : 385.py
# @Time    : 2020/7/28 4:33 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """
       pass

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """
       pass

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """
       pass

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """
       pass

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """
       pass

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
       pass


class Solution:
    """
    [385. 迷你语法分析器](https://leetcode-cn.com/problems/mini-parser/)
    """
    def deserialize(self, s: str) -> NestedInteger:
        if s=='': return NestedInteger()
        if s[0]!='[': return NestedInteger(int(s))
        if len(s)<=2: return NestedInteger()
        left, lv = 1, 0
        res = NestedInteger()
        for right in range(1, len(s)):
            if lv == 0 and (s[right] == ',' or right == len(s)-1):
                res.add(self.deserialize(s[left:right]))
                left = right + 1
            elif s[right] == '[':
                lv += 1
            elif s[right] == ']':
                lv -= 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.deserialize("[123,[456,[789]]]")
