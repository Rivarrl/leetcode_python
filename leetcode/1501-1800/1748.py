# -*- coding: utf-8 -*-
# ======================================
# @File    : 1748.py
# @Time    : 2021/2/17 19:26
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1748. 唯一元素的和](https://leetcode-cn.com/problems/sum-of-unique-elements/)
    """
    @timeit
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums)
        res = 0
        for k, v in cnt.items():
            if v == 1:
                res += k
        return res

if __name__ == '__main__':
    a = Solution()
    a.sumOfUnique(nums = [1,2,3,2])
    a.sumOfUnique(nums = [1,1,1,1,1])
    a.sumOfUnique(nums = [1,2,3,4,5])