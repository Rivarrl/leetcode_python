# -*- coding: utf-8 -*-
# ======================================
# @File    : 324.py
# @Time    : 2019/12/19 1:19
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [324. 摆动排序 II](https://leetcode-cn.com/problems/wiggle-sort-ii/)
    """
    def wiggleSort(self, nums: List[int]) -> None:
        """
        nlogn，先排序再按位置分配，分配的时候注意先小后大，如果按序分配，假如是123334，就变成了132334，而答案应该是341323，观察可得倒序分配可避免此问题.
        """
        nums.sort()
        n = len(nums[::2])
        nums[::2], nums[1::2] = nums[:n][::-1], nums[n:][::-1]

    def wiggleSort2(self, nums: List[int]) -> None:
        """
        类似三路快速排序(荷兰国旗算法)的方法，先找中位数，按中位数上下浮动去找中位数附近点分别放在2i和2i+1位置
        """


if __name__ == "__main__":
    a = Solution()
    a.wiggleSort()