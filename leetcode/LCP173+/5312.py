# -*- coding: utf-8 -*-
# ======================================
# @File    : 5312.py
# @Time    : 2/8/20 10:36 PM
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5312. 大小为 K 且平均值大于等于阈值的子数组数目](https://leetcode-cn.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)
    """
    @timeit
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        t = k * threshold
        n = len(arr)
        ctr = 0
        s = sum(arr[:k])
        if s >= t: ctr += 1
        for i in range(n-k):
            j = i + k
            s += arr[j] - arr[i]
            if s >= t: ctr += 1
        return ctr


if __name__ == '__main__':
    a = Solution()
    a.numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4)
    a.numOfSubarrays(arr = [1,1,1,1,1], k = 1, threshold = 0)
    a.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5)
    a.numOfSubarrays(arr = [7,7,7,7,7,7,7], k = 7, threshold = 7)
    a.numOfSubarrays(arr = [4,4,4,4], k = 4, threshold = 1)