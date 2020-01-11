# -*- coding: utf-8 -*-
# ======================================
# @File    : 5143
# @Time    : 2020/1/11 22:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5143. 解压缩编码列表]()
    """
    @timeit
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(0, n, 2):
            res += [nums[i+1]] * nums[i]
        return res


if __name__ == '__main__':
    a = Solution()
    a.decompressRLElist(nums = [1,2,3,4])