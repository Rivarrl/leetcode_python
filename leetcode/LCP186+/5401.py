# -*- coding: utf-8 -*-
# ======================================
# @File    : 5401.py
# @Time    : 2020/5/3 10:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5401. 是否所有 1 都至少相隔 k 个元素]()
    """
    @timeit
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        j = -k-1
        for i in range(n):
            if nums[i] == 1:
                if i - j - 1 < k:
                    return False
                j = i
        return True


if __name__ == '__main__':
    a = Solution()
    a.kLengthApart(nums = [1,0,0,0,1,0,0,1], k = 2)
    a.kLengthApart(nums = [1,0,0,1,0,1], k = 2)
    a.kLengthApart(nums = [1,1,1,1,1], k = 0)
    a.kLengthApart(nums = [0,1,0,1], k = 1)