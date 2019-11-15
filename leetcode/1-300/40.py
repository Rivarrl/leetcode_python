# -*- coding: utf-8 -*-
# ======================================
# @File    : 40.py
# @Time    : 2019/11/15 22:58
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [40. 组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii/)
    """
    @timeit
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        思路：回溯，建立一个来控制candidates中的元素是否被访问过的数组
        用一个数二进制可以代替数组
        """
        candidates.sort()
        n = len(candidates)
        a = 0
        def dfs(i, j, t):
            nonlocal a, res
            if candidates[i] > t: return []
            if candidates[i] == t: return [[candidates[i]]]
            for j in range(n):
                if a & (1 << j): continue
                if candidates[j]
            a |= (1 << i)
            dfs(i+1, t - candidates[i])





if __name__ == '__main__':
    a = Solution()
    a.combinationSum2([10,1,2,7,6,1,5], 8)