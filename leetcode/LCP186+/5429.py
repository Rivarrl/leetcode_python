# -*- coding: utf-8 -*-
# ======================================
# @File    : 5429.py
# @Time    : 2020/6/7 10:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5429. 数组中的 k 个最强值](https://leetcode-cn.com/problems/the-k-strongest-values-in-an-array)
    """
    @timeit
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m = arr[(n-1)//2]
        i, j = 0, n - 1
        res = []
        while k > 0:
            left, right = abs(arr[i] - m), abs(arr[j] - m)
            if left > right:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j -= 1
            k -= 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.getStrongest(arr = [1,2,3,4,5], k = 2)
    a.getStrongest(arr = [1,1,3,5,5], k = 2)
    a.getStrongest(arr = [6,7,11,7,6,8], k = 5)
    a.getStrongest(arr = [6,-3,7,2,11], k = 3)
    a.getStrongest(arr = [-7,22,17,3], k = 2)