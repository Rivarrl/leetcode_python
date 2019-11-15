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
        import bisect
        import heapq
        def dfs(candidates, target):
            if target == 0: return [[]]
            if not candidates or min(candidates) > target: return []
            res = []
            while candidates:
                x = heapq.heappop(candidates)
                for y in dfs([e for e in candidates if e <= target - x], target-x):
                    bisect.insort(y, x)
                    if y not in res:
                        res += [y]
            return res
        return dfs(candidates, target)


if __name__ == '__main__':
    a = Solution()
    a.combinationSum2([3,1,3,5,1,5,2,3,2,5,4],1)
    a.combinationSum2([10,1,2,7,6,1,5], 8)