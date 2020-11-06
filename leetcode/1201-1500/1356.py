# -*- coding: utf-8 -*-
# ======================================
# @File    : 1356.py
# @Time    : 2020/11/6 2:50 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1356. 根据数字二进制下 1 的数目排序](https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/)
    """
    @timeit
    def sortByBits(self, arr: List[int]) -> List[int]:
        from functools import cmp_to_key
        def my_cmp(x, y):
            sx, sy = bin(x), bin(y)
            cx, cy = sx.count('1'), sy.count('1')
            if cx == cy:
                return 1 if x > y else -1
            else:
                return 1 if cx > cy else -1

        arr.sort(key=cmp_to_key(my_cmp))
        return arr

    @timeit
    def sortByBits2(self, arr: List[int]) -> List[int]:
        def count1(x):
            res = 0
            while x:
                x &= (x-1)
                res += 1
            return res
        arr.sort(key= lambda x: (count1(x), x))
        return arr

if __name__ == '__main__':
    a = Solution()
    a.sortByBits(arr = [0,1,2,3,4,5,6,7,8])
    a.sortByBits(arr = [1024,512,256,128,64,32,16,8,4,2,1])
    a.sortByBits(arr = [10000,10000])
    a.sortByBits(arr = [2,3,5,7,11,13,17,19])
    a.sortByBits(arr = [10,100,1000,10000])