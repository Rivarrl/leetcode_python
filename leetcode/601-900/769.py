# -*- coding: utf-8 -*-
# ======================================
# @File    : 769.py
# @Time    : 2021/1/7 20:25
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [769. 最多能完成排序的块](https://leetcode-cn.com/problems/max-chunks-to-make-sorted/)
    """
    @timeit
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        right = 0
        res = 0
        for left in range(n):
            if arr[left] > right:
                right = arr[left]
            elif left == right:
                res += 1
                right += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxChunksToSorted(arr = [4,3,2,1,0])
    a.maxChunksToSorted(arr = [1,0,2,3,4])