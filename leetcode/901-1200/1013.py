# -*- coding: utf-8 -*-
# ======================================
# @File    : 1013.py
# @Time    : 2019/12/25 13:22
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1013. 将数组分成和相等的三个部分](https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/)
    """
    @timeit
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 > 0: return False
        n = len(A)
        e = s // 3
        def dfs(i, p):
            if p == 3:
                return sum(A[i:]) == e
            c = 0
            for j in range(i, n):
                c += A[j]
                if c == e and dfs(j+1, p+1): return True
            return False
        return dfs(0, 1)


if __name__ == '__main__':
    a = Solution()
    a.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1])
    a.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1])
    a.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4])