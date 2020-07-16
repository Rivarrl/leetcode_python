# -*- coding: utf-8 -*-
# ======================================
# @File    : 96.py
# @Time    : 2020/7/15 1:17 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [96. 不同的二叉搜索树](https://leetcode-cn.com/problems/unique-binary-search-trees/)
    """
    @timeit
    def numTrees(self, n: int) -> int:
        # 卡塔兰数
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


if __name__ == '__main__':
    a = Solution()
    a.numTrees(3)