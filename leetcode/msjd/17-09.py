# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-09.py
# @Time    : 2020/11/5 5:55 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.09. 第 k 个数](https://leetcode-cn.com/problems/get-kth-magic-number-lcci/)
    """
    @timeit
    def getKthMagicNumber(self, k: int) -> int:
        import heapq
        pq = [[1,(0,0,0)]]
        res = 1
        seen = set()
        for _ in range(k):
            res, (a, b, c) = heapq.heappop(pq)
            for da, db, dc in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
                x, y, z = a+da, b+db, c+dc
                if (x, y, z) not in seen:
                    seen.add((x, y, z))
                    heapq.heappush(pq, [3 ** x * 5 ** y * 7 ** z, (x, y, z)])
        return res

if __name__ == '__main__':
    a = Solution()
    # a.getKthMagicNumber(k = 5)
    a.getKthMagicNumber(k = 7)