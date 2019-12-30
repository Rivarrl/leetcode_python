# -*- coding: utf-8 -*-
# ======================================
# @File    : 5297.py
# @Time    : 2019/12/29 17:21
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5297. 跳跃游戏 III](https://leetcode-cn.com/problems/jump-game-iii/)
    """
    @timeit
    def canReach(self, arr: List[int], start: int) -> bool:
        stk = [start]
        n = len(arr)
        vis = [0] * n
        vis[start] = 1
        while stk:
            i = stk.pop()
            if arr[i] == 0: return True
            for j in [-1, 1]:
                x = i +  j * arr[i]
                if 0 <= x < n and vis[x] == 0:
                    vis[x] = 1
                    stk.insert(0, x)
        return False

if __name__ == '__main__':
    a = Solution()
    a.canReach(arr = [4,2,3,0,3,1,2], start = 5)
    a.canReach(arr = [4,2,3,0,3,1,2], start = 0)
    a.canReach(arr = [3,0,2,1,2], start = 2)