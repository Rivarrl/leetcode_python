# -*- coding: utf-8 -*-
# ======================================
# @File    : 565.py
# @Time    : 2020/5/8 21:21
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [565. 数组嵌套](https://leetcode-cn.com/problems/array-nesting/submissions/)
    """
    @timeit
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        vis = [False] * n
        def dfs(i):
            if i == nums[i]: return 1
            if vis[i]: return 0
            vis[i] = True
            res = dfs(nums[i]) + 1
            return res
        res = 0
        for i in range(n):
            if not vis[i]:
                res = max(res, dfs(i))
        return res


if __name__ == '__main__':
    a = Solution()
    a.arrayNesting([5,4,0,3,1,6,2])