# -*- coding: utf-8 -*-
# ======================================
# @File    : 39.py
# @Time    : 2019/11/16 0:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [39. 组合总和](https://leetcode-cn.com/problems/combination-sum/)
    """
    @timeit
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        思路：可无限次取，不需要记录是否被选过
        """
        candidates.sort()
        def dfs(candidates, target):
            if target == 0: return [[]]
            if not candidates or min(candidates) > target: return []
            res = []
            for x in candidates:
                for y in dfs([e for e in candidates if e <= x], target - x):
                    res += [[x] + y]
            return res
        return dfs(candidates, target)


if __name__ == '__main__':
    a = Solution()
    a.combinationSum([2,3,6,7], 7)