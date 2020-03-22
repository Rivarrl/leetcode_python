# -*- coding: utf-8 -*-
# ======================================
# @File    : 5348.py
# @Time    : 2020/3/21 22:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5348. 两个数组间的距离值](https://leetcode-cn.com/problems/find-the-distance-value-between-two-arrays/)
    """
    @timeit
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        ctr = 0
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    break
            else:
                ctr += 1
        return ctr


if __name__ == '__main__':
    a = Solution()
    a.findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2)
    a.findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3)
    a.findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6)
