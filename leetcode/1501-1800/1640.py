# -*- coding: utf-8 -*-
# ======================================
# @File    : 1640.py
# @Time    : 2020/11/23 23:38
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1640. 能否连接形成数组](https://leetcode-cn.com/problems/check-array-formation-through-concatenation/)
    """
    @timeit
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(pieces)
        m = len(arr)
        ids = [0] * n
        i = 0
        while i < m:
            last = i
            j = 0
            while j < n:
                while ids[j] < len(pieces[j]) and pieces[j][ids[j]] == arr[i]:
                    ids[j] += 1
                    i += 1
                if i != last: break
                j += 1
            if last == i or ids[j] != len(pieces[j]): return False
        return all(ids[i] == len(pieces[i]) for i in range(n))



if __name__ == '__main__':
    a = Solution()
    a.canFormArray(arr = [85], pieces = [[85]])
    a.canFormArray(arr = [15,88], pieces = [[88],[15]])
    a.canFormArray(arr = [49,18,16], pieces = [[16,18,49]])
    a.canFormArray(arr = [91,4,64,78], pieces = [[78],[4,64],[91]])
    a.canFormArray(arr = [1,3,5,7], pieces = [[2,4,6,8]])
    a.canFormArray([1,2,3], [[2],[1,3]])