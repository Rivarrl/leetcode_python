# -*- coding: utf-8 -*-
# ======================================
# @File    : 547.py
# @Time    : 2020/5/9 1:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [547. 朋友圈](https://leetcode-cn.com/problems/friend-circles/)
    """
    @timeit
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        arr = [i for i in range(n)]
        def find(p):
            if p == arr[p]:
                return p
            else:
                arr[p] = find(arr[p])
            return arr[p]
        def union(p, q):
            x, y = find(p), find(q)
            if x == y: return
            arr[y] = x

        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1: union(i, j)
        for i in range(n): find(i)
        return len(set(arr))

if __name__ == '__main__':
    a = Solution()
    a.findCircleNum([[1,1,0],
                     [1,1,0],
                     [0,0,1]])
    a.findCircleNum([[1,1,0],
                     [1,1,1],
                     [0,1,1]])
    a.findCircleNum([[1,0,0,1],
                     [0,1,1,0],
                     [0,1,1,1],
                     [1,0,1,1]])