# -*- coding: utf-8 -*-
# ======================================
# @File    : 1671.py
# @Time    : 2020/12/2 0:45
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1671. 得到山形数组的最少删除次数]()
    """
    @timeit
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        import bisect
        def f(arr):
            h = []
            res = []
            for x in arr:
                p = bisect.bisect_left(h, x)
                res.append(p)
                if p == len(h):
                    h.append(x)
                else:
                    h[p] = x
            return res

        left = f(nums)
        right = f(reversed(nums))
        right.reverse()
        return len(nums) - max(i + j for i, j in zip(left[1:-1], right[1:-1])) - 1


if __name__ == '__main__':
    a = Solution()
    # a.minimumMountainRemovals(nums = [1,3,1])
    # a.minimumMountainRemovals(nums = [2,1,1,5,6,2,3,1])
    # a.minimumMountainRemovals(nums = [4,3,2,1,1,2,3,1])
    # a.minimumMountainRemovals(nums = [1,2,3,4,4,3,2,1])
    a.minimumMountainRemovals([23,47,63,72,81,99,88,55,21,33,32])