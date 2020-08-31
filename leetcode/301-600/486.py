# -*- coding: utf-8 -*-
# ======================================
# @File    : 486.py
# @Time    : 2020/9/1 0:14
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [486. 预测赢家](https://leetcode-cn.com/problems/predict-the-winner/)
    """
    @timeit
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if (n >> 1) == 0: return True
        dp = [[nums[i] if i == j else 0 for j in range(n)] for i in range(n)]
        for k in range(1, n):
            for j in range(k, n):
                i = j - k
                dp[i][j] = max(nums[j] - dp[i][j-1], nums[i] - dp[i+1][j])
        return dp[0][-1] >= 0

if __name__ == '__main__':
    a = Solution()
    a.PredictTheWinner([1, 5, 2])
    a.PredictTheWinner([1, 5, 233, 7])