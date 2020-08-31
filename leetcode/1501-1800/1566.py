# -*- coding: utf-8 -*-
# ======================================
# @File    : 1566.py
# @Time    : 2020/8/31 23:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1566. 重复至少 K 次且长度为 M 的模式](https://leetcode-cn.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/)
    """
    @timeit
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        if m * k > n: return False
        for i in range(n-m*k+1):
            for j in range(i, i+m):
                p, t = j, 0
                while p < n and arr[p] == arr[j] and t < k:
                    p += m
                    t += 1
                if t != k: break
            else:
                return True
        return False

if __name__ == '__main__':
    a = Solution()
    a.containsPattern(arr = [1,2,4,4,4,4], m = 1, k = 3)
    a.containsPattern(arr = [1,2,1,2,1,1,1,3], m = 2, k = 2)
    a.containsPattern(arr = [1,2,1,2,1,3], m = 2, k = 3)
    a.containsPattern(arr = [1,2,3,1,2], m = 2, k = 2)
    a.containsPattern(arr = [2,2,2,2], m = 2, k = 3)
    a.containsPattern([2,2],1,2)
    a.containsPattern([1,2],1,2)