# -*- coding: utf-8 -*-
# ======================================
# @File    : 1095.py
# @Time    : 2020/4/29 0:37
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)

class Solution:
    """
    [1095. 山脉数组中查找目标值](https://leetcode-cn.com/problems/find-in-mountain-array/)
    """
    @timeit
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        lo, hi = 0, n
        maxi, midm = 0, 0
        while lo < hi:
            mi = lo + (hi - lo) // 2
            x = mountain_arr.get(mi)
            ix = mountain_arr.get(mi-1)
            if ix > x:
                hi = mi
            else:
                xi = mountain_arr.get(mi+1)
                if xi < x:
                    maxi, midm = mi, x
                    break
                else:
                    lo = mi + 1
        lo, hi = 0, maxi + 1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            x = mountain_arr.get(mi)
            if x == target:
                return mi
            elif x < target:
                lo = mi + 1
            else:
                hi = mi
        lo, hi = maxi, n
        while lo < hi:
            mi = lo + (hi - lo) // 2
            x = mountain_arr.get(mi)
            if x == target:
                return mi
            elif x < target:
                hi = mi
            else:
                lo = mi + 1
        return -1

if __name__ == '__main__':
    a = Solution()
    ma = MountainArray([1,2,3,4,5,3,1])
    a.findInMountainArray(3, ma)
    ma = MountainArray([0,1,2,4,2,1])
    a.findInMountainArray(3, ma)