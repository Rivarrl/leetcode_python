# -*- coding: utf-8 -*-
# ======================================
# @File    : 1043.py
# @Time    : 2019/11/11 15:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        """
        [1043. 分隔数组以得到最大和](https://leetcode-cn.com/problems/partition-array-for-maximum-sum/submissions/)
        思路：动态规划，dp[i]表示前i个数的最大和，dp[i] = max(dp[j] + max(A[j:i]) * (i-j))
        """
        n = len(A)
        dp = [0] * (n+1)
        for i in range(1, n+1):
            j = i - 1
            cur_max = float('-inf')
            while i - j <= K and j >= 0:
                cur_max = max(cur_max, A[j])
                dp[i] = max(dp[i], dp[j] + cur_max * (i-j))
                j -= 1
        return dp[n]
