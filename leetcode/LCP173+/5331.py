# -*- coding: utf-8 -*-
# ======================================
# @File    : 5331.py
# @Time    : 2020/2/2 10:57
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1344. 跳跃游戏 V](https://leetcode-cn.com/problems/jump-game-v/)
    """
    @timeit
    def maxJumps(self, arr: List[int], d: int) -> int:
        from functools import lru_cache
        n = len(arr)
        @lru_cache(None)
        def dfs(i):
            res = 1
            bl = br = 1
            for k in range(1, d+1):
                if bl == br == 0: break
                l, r = i - k, i + k
                if l >= 0 and bl:
                    if arr[l] >= arr[i]:
                        bl = 0
                    else:
                        res = max(res, dfs(l) + 1)
                if r < n and br:
                    if arr[r] >= arr[i]:
                        br = 0
                    else:
                        res = max(res, dfs(r) + 1)
            return res
        res = 1
        for i in range(n):
            res = max(res, dfs(i))
        return res


if __name__ == '__main__':
    a = Solution()
    a.maxJumps(arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2)
    a.maxJumps(arr = [3,3,3,3,3], d = 3)
    a.maxJumps(arr = [7,6,5,4,3,2,1], d = 1)
    a.maxJumps(arr = [7,1,7,1,7,1], d = 2)
    a.maxJumps(arr = [66], d = 1)