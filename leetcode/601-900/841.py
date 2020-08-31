# -*- coding: utf-8 -*-
# ======================================
# @File    : 841.py
# @Time    : 2020/8/31 1:39 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [841. 钥匙和房间](https://leetcode-cn.com/problems/keys-and-rooms)
    """
    @timeit
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        def dfs(i, k=1):
            if k == (1 << n) - 1: return k
            for j in rooms[i]:
                if k & (1 << j): continue
                k |= dfs(j, k | (1 << j))
                if k == (1 << n) - 1: return k
            return k
        return dfs(0) == (1 << n) - 1

if __name__ == '__main__':
    a = Solution()
    a.canVisitAllRooms([[1],[2],[3],[]])
    a.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
    a.canVisitAllRooms([[2,3],[],[2],[1,3,1]])