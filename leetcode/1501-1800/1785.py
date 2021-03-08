# -*- coding: utf-8 -*-
# ======================================
# @File    : 1785
# @Time    : 2021/3/8 12:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1785. 构成特定和需要添加的最少元素](https://leetcode-cn.com/problems/minimum-elements-to-add-to-form-a-given-sum/)
    """
    @timeit
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return (abs(sum(nums) - goal) + limit - 1) // limit

if __name__ == '__main__':
    a = Solution()
    a.minElements(nums = [1,-1,1], limit = 3, goal = -4)
    a.minElements(nums = [1,-10,9,1], limit = 100, goal = 0)