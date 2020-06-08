# -*- coding: utf-8 -*-
# ======================================
# @File    : 5428.py
# @Time    : 2020/6/7 10:56
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5428. 重新排列数组](https://leetcode-cn.com/problems/shuffle-the-array/)
    """
    @timeit
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res

if __name__ == '__main__':
    a = Solution()
    a.shuffle([2,5,1,3,4,7], 3)
    a.shuffle([1,2,3,4,4,3,2,1], 4)
    a.shuffle([1,1,2,2], 2)