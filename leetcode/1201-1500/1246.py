# -*- coding: utf-8 -*-
# ======================================
# @File    : 1246.py
# @Time    : 2021/1/15 21:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1246. 删除回文子数组](https://leetcode-cn.com/problems/palindrome-removal/)
    """
    def minimumMoves(self, arr: List[int]) -> int:
        def fdp(i, j):
            if i > j: return 0
            if i == j: return 1
            if i + 1 == j:
                if arr[i] == arr[j]:
                    return 1
                else:
                    return 2
            if dp[i][j] != -1:
                return dp[i][j]
            res = n
            for k in range(i, j+1):
                if arr[i] != arr[k]: continue
                left = fdp(i+1, k-1)
                if left == 0: left = 1
                res = min(res, left + fdp(k+1, j))
            dp[i][j] = res
            return res
        n = len(arr)
        dp = [[-1] * n for _ in range(n)]
        res = fdp(0, n-1)
        return res

if __name__ == '__main__':
    a = Solution()
    a.minimumMoves(arr = [1,2])
    a.minimumMoves(arr = [1,3,4,1,5])