# -*- coding: utf-8 -*-
# ======================================
# @File    : 1696.py
# @Time    : 2020/12/20 12:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1696. 跳跃游戏 VI](https://leetcode-cn.com/problems/jump-game-vi/)
    """
    @timeit
    def maxResult(self, nums: List[int], k: int) -> int:
        res = nums[0]
        l = r = 1
        m, mi = -10005, -1
        n = len(nums)
        while r < n:
            if r == n - 1:
                res += nums[r]
                break
            if nums[r] >= 0:
                res += nums[r]
                m, mi = -10005, -1
                l = r + 1
            else:
                if nums[r] >= m:
                    m = nums[r]
                    mi = r
            if r - l + 1 >= k:
                l = mi + 1
                res += m
                m, mi = -10005, -1
            r += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.maxResult(nums = [1,-1,-2,4,-7,3], k = 2)
    a.maxResult(nums = [10,-5,-2,4,0,3], k = 3)
    a.maxResult(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2)