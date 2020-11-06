# -*- coding: utf-8 -*-
# ======================================
# @File    : 1636.py
# @Time    : 2020/11/6 12:53 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1636. 按照频率将数组升序排序]()
    """
    @timeit
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        d = Counter(nums)
        nums.sort(key=lambda x: (d[x], -x))
        return nums

if __name__ == '__main__':
    a = Solution()
    a.frequencySort(nums = [1,1,2,2,2,3])
    a.frequencySort(nums = [2,3,1,3,2])
    a.frequencySort(nums = [-1,1,-6,4,5,-6,1,4,1])