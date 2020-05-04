# -*- coding: utf-8 -*-
# ======================================
# @File    : 5403.py
# @Time    : 2020/5/3 10:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5403. 有序矩阵中的第 k 个最小数组和]()
    """
    @timeit
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        import heapq
        n, m = len(mat), len(mat[0])
        ptr = [0] * n
        c = 0
        for i in range(n):
            c += mat[i][ptr[i]]
        stk = []
        heapq.heappush(stk, (c, ptr))
        vis = set()
        vis.add(tuple(ptr))
        for t in range(1, k):
            c, ptr = heapq.heappop(stk)
            for i in range(n):
                if ptr[i] == m - 1: continue
                ptr[i] += 1
                if not tuple(ptr) in vis:
                    cq = c + mat[i][ptr[i]] - mat[i][ptr[i]-1]
                    heapq.heappush(stk, (cq, ptr[:]))
                    vis.add(tuple(ptr))
                ptr[i] -= 1
        return stk[0][0]

if __name__ == '__main__':
    a = Solution()
    a.kthSmallest(mat = [[1,3,11],[2,4,6]], k = 5)
    a.kthSmallest(mat = [[1,3,11],[2,4,6]], k = 9)
    a.kthSmallest(mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7)
    a.kthSmallest(mat = [[1,1,10],[2,2,9]], k = 7)