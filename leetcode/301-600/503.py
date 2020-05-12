# -*- coding: utf-8 -*-
# ======================================
# @File    : 503.py
# @Time    : 2020/5/11 23:45
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [503. 下一个更大元素 II](https://leetcode-cn.com/problems/next-greater-element-ii/)
    """
    @timeit
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stk = []
        c = 0
        for i in range(n*2):
            while stk and nums[stk[-1]] < nums[i%n]:
                j = stk.pop()
                if res[j] == -1: c += 1
                res[j] = nums[i%n]
            if c == n: break
            stk.append(i%n)
        return res

if __name__ == '__main__':
    a = Solution()
    a.nextGreaterElements([1,2,1])
    a.nextGreaterElements([1,2,3,4,3])