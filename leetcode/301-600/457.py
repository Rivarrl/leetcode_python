# -*- coding: utf-8 -*-
# ======================================
# @File    : 457.py
# @Time    : 2020/12/2 1:23 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [457. 环形数组循环](https://leetcode-cn.com/problems/circular-array-loop/)
    """
    @timeit
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            j = i
            rec = [False] * n
            rnd = False
            d, tot = nums[i], 0
            while not rec[(j + nums[j] + n) % n]:
                j = (j + nums[j] + n) % n
                if d * nums[j] < 0: break
                if j + nums[j] < 0 or j + nums[j] >= n:
                    rnd = True
                tot += 1
                rec[j] = True
            else:
                if rnd and j == i and tot > 1:
                    return True
        return False


if __name__ == '__main__':
    a = Solution()
    a.circularArrayLoop([2,-1,1,2,2])
    a.circularArrayLoop([-1,2])
    a.circularArrayLoop([-2,1,-1,-2,-2])
    a.circularArrayLoop([1,1,2])
    a.circularArrayLoop([1,2,2,-1])