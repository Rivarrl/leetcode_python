# -*- coding: utf-8 -*-
# ======================================
# @File    : 5364.py
# @Time    : 2020/3/22 10:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5364. 按既定顺序创建目标数组]()
    """
    @timeit
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            res.insert(index[i], nums[i])
        return res

if __name__ == '__main__':
    a = Solution()
    a.createTargetArray([0,1,2,3,4],[0,1,2,2,1])
    a.createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0])
    a.createTargetArray([1],[0])