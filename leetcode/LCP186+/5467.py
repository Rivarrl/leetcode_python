# -*- coding: utf-8 -*-
# ======================================
# @File    : 5467.py
# @Time    : 2020/7/19 11:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1521. 找到最接近目标值的函数值](https://leetcode-cn.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/)
    """
    @timeit
    def closestToTarget(self, arr: List[int], target: int) -> int:
        s = set()
        res = abs(arr[0] - target)
        for x in arr:
            tmp = {x, }
            for pre in s:
                tmp.add(pre & x)
            for y in tmp:
                res = min(res, abs(y - target))
            s = tmp
        return res

if __name__ == '__main__':
    a = Solution()
    a.closestToTarget(arr = [9,12,3,7,15], target = 5)
    a.closestToTarget(arr = [1000000,1000000,1000000], target = 1)
    a.closestToTarget(arr = [1,2,4,8,16], target = 0)
    a.closestToTarget([5,89,79,44,45,79],965)