# -*- coding: utf-8 -*-
# ======================================
# @File    : 474.py
# @Time    : 2020/5/13 23:28
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 01背包多重背包问题
        # dp[k][i][j] 表示前k个物品时用i个0和j个1的最大收益
        # k只与k-1的状态相关，dp数组压缩的方法是倒序遍历，使得每次dp取到的dp[i-c0][j-c1]都是上一轮的结果
        dp = [[0] * (n+1) for _ in range(m+1)]
        for x in strs:
            c0 = x.count('0')
            c1 = len(x) - c0
            for i in range(m, c0-1, -1):
                for j in range(n, c1-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-c0][j-c1] + 1)
        return dp[m][n]

if __name__ == '__main__':
    a = Solution()
    a.findMaxForm(["10","0001","111001","1","0"], 5, 3)
    a.findMaxForm(["10", "0", "1"], 1, 1)