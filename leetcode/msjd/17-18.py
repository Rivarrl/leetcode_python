# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-18.py
# @Time    : 2020/9/28 12:53 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.18. 最短超串](https://leetcode-cn.com/problems/shortest-supersequence-lcci/)
    """
    @timeit
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        # 滑动窗口
        res = []
        if len(small) > len(set(big)): return []
        n, m = len(big), len(small)
        d = set(small)
        seen = {}
        l, r = 0, 0
        while r < n:

        return res

    @timeit
    def shortestSeq2(self, big: List[int], small: List[int]) -> List[int]:
        # 记录位置, 因为small中的元素不重复
        # 所以只要在small全部出现后计算最大位置和最小位置差，然后取全局最小的作为结果
        res = []
        if len(small) > len(set(big)): return []
        d = set(small)
        seen = {}
        n = len(big)
        for i, x in enumerate(big):
            if x in d: seen[x] = i
            if len(seen) == len(d):
                l, r = min(seen.values()), max(seen.values())
                if r - l < n:
                    n = r - l
                    res = [l, r]
        return res

if __name__ == '__main__':
    a = Solution()
    big = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
    small = [1, 5, 9]
    a.shortestSeq2(big, small)
    a.shortestSeq2([1, 2, 1, 2, 1, 2], [1, 2])
    a.shortestSeq2([1], [1,2])