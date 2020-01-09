# -*- coding: utf-8 -*-
# ======================================
# @File    : 546
# @Time    : 2020/1/9 10:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [546. 移除盒子](https://leetcode-cn.com/problems/remove-boxes)
    """
    @timeit
    def removeBoxes(self, boxes: List[int]) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dfs(i, j, k):
            if i > j: return 0
            while i < j and boxes[i] == boxes[i+1]:
                i += 1
                k += 1
            res = k * k + dfs(i+1, j, 1)
            for p in range(i+1, j+1):
                if boxes[p] == boxes[i]:
                    res = max(res, dfs(i+1, p-1, 1) + dfs(p, j, k+1))
            return res
        return dfs(0, len(boxes)-1, 1)

if __name__ == '__main__':
    a = Solution()
    a.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1])
    a.removeBoxes([8, 1, 2, 10, 8, 5, 1, 10, 8, 4])