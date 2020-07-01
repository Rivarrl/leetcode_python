# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-15.py
# @Time    : 2020/7/2 0:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.15. 珠玑妙算](https://leetcode-cn.com/problems/master-mind-lcci/)
    """
    @timeit
    def masterMind(self, solution: str, guess: str) -> List[int]:
        s = {}
        g = {}
        res = [0, 0]
        for i in range(4):
            if solution[i] == guess[i]:
                res[0] += 1
            else:
                s[solution[i]] = s.get(solution[i], 0) + 1
                g[guess[i]] = g.get(guess[i], 0) + 1
        for k, v in s.items():
            if k in g:
                res[1] += min(g[k], v)
        return res

if __name__ == '__main__':
    a = Solution()
    a.masterMind("RGBY", "GGRR")