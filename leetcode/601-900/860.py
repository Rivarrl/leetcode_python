# -*- coding: utf-8 -*-
# ======================================
# @File    : 860.py
# @Time    : 2020/5/9 0:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [860. 柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/)
    """
    @timeit
    def lemonadeChange(self, bills: List[int]) -> bool:
        d5 = d10 = 0
        for x in bills:
            if x == 5:
                d5 += 1
            elif x == 10:
                if d5 == 0: return False
                d5 -= 1
                d10 += 1
            else:
                if d5 == 0: return False
                if d10 > 0:
                    d10 -= 1
                    d5 -= 1
                elif d5 < 3: return False
                else: d5 -= 3
        return True

if __name__ == '__main__':
    a = Solution()
    a.lemonadeChange([5,5,5,10,20])
    a.lemonadeChange([5,5,10])
    a.lemonadeChange([10,10])
    a.lemonadeChange([5,5,10,10,20])
    a.lemonadeChange([5,5,5,10,5,5,10,20,20,20])