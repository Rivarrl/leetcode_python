# -*- coding: utf-8 -*-
# ======================================
# @File    : 1144.py
# @Time    : 2019/12/2 23:37
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import sys

sys.setrecursionlimit(3000)
class Solution:
    """
    [1144. 递减元素使数组呈锯齿状](https://leetcode-cn.com/problems/decrease-elements-to-make-array-zigzag/)
    """
    @timeit
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        """
        从中间向两边加数
        """
        n = len(nums)
        # u, d记录升序/降序需要累计的代价
        # last_d记录前一个位置需要减的代价，只有升序变降序时需要记录
        u = d = last_d = 0
        for i in range(1, n):
            last_d, u, d = max(0, nums[i] - nums[i-1] + 1), max(0, nums[i-1] - last_d - nums[i] + 1) + d, max(0, nums[i] - nums[i-1] + 1) + u
        return min(u, d)

if __name__ == '__main__':
    import random
    a = Solution()
    # a.movesToMakeZigzag([1,2,3])
    a.movesToMakeZigzag([9,6,1,6,2])
    # a.movesToMakeZigzag([2,7,10,9,8,9])
    # x = [i for i in range(1, 1001)]
    # for i in range(999):
    #     j = random.randint(i+1, 999)
    #     x[i], x[j] = x[j], x[i]
    # a.movesToMakeZigzag(x)