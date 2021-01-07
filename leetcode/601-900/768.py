# -*- coding: utf-8 -*-
# ======================================
# @File    : 768.py
# @Time    : 2021/1/7 22:25
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [768. 最多能完成排序的块 II](https://leetcode-cn.com/problems/max-chunks-to-make-sorted-ii/)
    """
    @timeit
    def maxChunksToSorted(self, arr: List[int]) -> int:
        from collections import defaultdict
        n = len(arr)
        arr2 = sorted(arr)
        d = defaultdict(list)
        for i in range(n):
            d[arr2[i]].append(i)
        for k in d: d[k].reverse()
        res = right = 0
        for left in range(n):
            t = d[arr[left]].pop()
            if t > right:
                right = t
            elif left == right:
                right += 1
                res += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxChunksToSorted(arr = [5,4,3,2,1])
    a.maxChunksToSorted(arr = [2,1,3,4,4])