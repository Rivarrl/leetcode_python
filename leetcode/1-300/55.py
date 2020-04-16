# -*- coding: utf-8 -*-
# ======================================
# @File    : 55.py
# @Time    : 2020/4/17 0:06
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/)
    """
    @timeit
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        r = 0
        for i in range(n):
            if i > r: return False
            r = max(r, i + nums[i])
        return True


if __name__ == '__main__':
    a = Solution()
    a.canJump([2,3,1,1,4])
    a.canJump([3,2,1,0,4])