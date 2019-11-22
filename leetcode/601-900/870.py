# -*- coding: utf-8 -*-
# ======================================
# @File    : 870.py
# @Time    : 2019/11/23 0:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [870. 优势洗牌](https://leetcode-cn.com/problems/advantage-shuffle/)
    """
    @timeit
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        """
        思路：田忌赛马的原理，贪心算法，如果A最大值比B最大值大，那么把A最大的安排到B最大的位置，否则把A最小值安排到B最大的位置。
        """
        import heapq
        n = len(A)
        res = [0] * n
        pqb = []
        for i in range(n):
            heapq.heappush(pqb, (-B[i], i))
        A.sort()
        l, r = 0, n-1
        while pqb:
            b, i = heapq.heappop(pqb)
            if A[r] > -b:
                res[i] = A[r]
                r -= 1
            else:
                res[i] = A[l]
                l += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.advantageCount([2,7,11,15], [1,10,4,11])
    a.advantageCount([12,24,8,32], [13,25,32,11])