# -*- coding: utf-8 -*-
# ======================================
# @File    : 659.py
# @Time    : 2020/12/4 9:43 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [659. 分割数组为连续子序列](https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/)
    """
    @timeit
    def isPossible(self, nums: List[int]) -> bool:
        # hashmap + minheap O(nlogn) & O(n)
        import heapq
        d = {}
        for x in nums:
            if x not in d:
                d[x] = []
            cur = 1 if x-1 not in d or len(d[x-1]) == 0 else heapq.heappop(d[x-1])+1
            heapq.heappush(d[x], cur)
        for k, vs in d.items():
            while vs:
                if heapq.heappop(vs) < 3:
                    return False
        return True

    @timeit
    def isPossible2(self, nums: List[int]) -> bool:
        # hashmap * 2 O(n) & O(n)
        # 元素x的出现次数 = 连接x-1的次数 + 以x开头的次数
        from collections import defaultdict
        d1, d2 = defaultdict(), defaultdict()
        for x in nums:
            d1[x] += 1
        for x in sorted(d1.keys()):
            d1[x] -= d2[x-1]
            d2[x] += d2[x-1]


    @timeit
    def isPossible3(self, nums: List[int]) -> bool:


if __name__ == '__main__':
    a = Solution()
    a.isPossible([1,2,3,3,4,5])
    a.isPossible([1,2,3,3,4,4,5,5])
    a.isPossible([1,2,3,4,4,5])