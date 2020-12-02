# -*- coding: utf-8 -*-
# ======================================
# @File    : 1673.py
# @Time    : 2020/12/2 2:06 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1673. 找出最具竞争力的子序列](https://leetcode-cn.com/problems/find-the-most-competitive-subsequence/)
    """
    @timeit
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stk = []
        q = len(nums) - k
        for x in nums:
            while q > 0 and stk and stk[-1] > x:
                q -= 1
                stk.pop()
            stk.append(x)
        return stk[:k]

if __name__ == '__main__':
    a = Solution()
    a.mostCompetitive(nums = [3,5,2,6], k = 2)
    a.mostCompetitive(nums = [2,4,3,3,5,4,9,6], k = 4)
    a.mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2], 3)