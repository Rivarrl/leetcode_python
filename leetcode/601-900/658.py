# -*- coding: utf-8 -*-
# ======================================
# @File    : 658.py
# @Time    : 2020/12/21 1:16 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [658. 找到 K 个最接近的元素](https://leetcode-cn.com/problems/find-k-closest-elements/)
    """
    @timeit
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l + 1 > k:
            if x - arr[l] > arr[r] - x:
                l += 1
            else:
                r -= 1
        return arr[l:r+1]


if __name__ == '__main__':
    a = Solution()
    a.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3)
    a.findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1)
    a.findClosestElements([1,2], 1, 1)
    a.findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 4)