# -*- coding: utf-8 -*-
# ======================================
# @File    : 5298.py
# @Time    : 2019/12/29 17:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5298. 口算难题](https://leetcode-cn.com/problems/verbal-arithmetic-puzzle/)
    """
    def isSolvable(self, words: List[str], result: str) -> bool:
        n = len(words)
        vis = {}
        def dfs(k):
            res = 0
            for i in range(n):
                if k < len(words[i]):
                    j = len(words) - 1 - k
                    if not words[i][j] in vis:
                        for i in range(10):
                            vis[words[i][j]] = i

                    res += words[i][j] * (10 ** k)
        dfs(0)

if __name__ == '__main__':
    a = Solution()
    a.isSolvable(words = ["SEND","MORE"], result = "MONEY")
    a.isSolvable(words = ["SIX","SEVEN","SEVEN"], result = "TWENTY")
    a.isSolvable(words = ["THIS","IS","TOO"], result = "FUNNY")
    a.isSolvable(words = ["LEET","CODE"], result = "POINT")