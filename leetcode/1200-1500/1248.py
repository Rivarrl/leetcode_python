# -*- coding: utf-8 -*-
# ======================================
# @File    : 1248.py
# @Time    : 2020/4/21 12:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1248. 统计「优美子数组」](https://leetcode-cn.com/problems/count-number-of-nice-subarrays/)
    """
    @timeit
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 前缀和+hash
        pre = [0]
        for e in nums:
            pre.append(pre[-1] + (e & 1))
        d = {}
        res = 0
        for e in pre:
            res += d.get(e-k, 0)
            d[e] = d.get(e, 0) + 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.numberOfSubarrays([1,1,2,1,1],3)
    a.numberOfSubarrays([2,4,6],1)
    a.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2)