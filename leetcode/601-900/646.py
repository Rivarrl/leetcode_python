# -*- coding: utf-8 -*-
# ======================================
# @File    : 646.py
# @Time    : 2020/12/18 9:42 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [646. 最长数对链](https://leetcode-cn.com/problems/maximum-length-of-pair-chain/)
    """
    @timeit
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        s = pairs[0][1]
        res = 1
        for x, y in pairs[1:]:
            if x > s:
                res += 1
                s = y
        return res

    @timeit
    def findLongestChain2(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort()
        dp = [0] * n
        dp[0] = 1
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return dp[-1]

if __name__ == '__main__':
    a = Solution()
    a.findLongestChain([[1,2], [2,3], [3,4]])
    a.findLongestChain([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]])
    a.findLongestChain([[9,10],[-4,9],[-5,6],[-5,9],[8,9]])