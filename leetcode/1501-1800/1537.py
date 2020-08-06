# -*- coding: utf-8 -*-
# ======================================
# @File    : 1537.py
# @Time    : 2020/8/4 19:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1537. 最大得分](https://leetcode-cn.com/problems/get-the-maximum-score/)
    """
    @timeit
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10 ** 9 + 7
        n, m = len(nums1), len(nums2)
        i = j = 0
        r1 = r2 = 0
        while i < n or j < m:
            if i == n:
                while j < m:
                    r2 += nums2[j]
                    j += 1
            elif j == m:
                while i < n:
                    r1 += nums1[i]
                    i += 1
            elif nums1[i] < nums2[j]:
                r1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                r2 += nums2[j]
                j += 1
            else:
                r1 = r2 = max(r1, r2) + nums1[i]
                i += 1
                j += 1
        return max(r1, r2) % mod

if __name__ == '__main__':
    a = Solution()
    a.maxSum(nums1 = [2,4,5,8,10], nums2 = [4,6,8,9])
    a.maxSum(nums1 = [1,3,5,7,9], nums2 = [3,5,100])
    a.maxSum(nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10])
    a.maxSum(nums1 = [1,4,5,8,9,11,19], nums2 = [2,3,4,11,12])
    a.maxSum([8,18,38,58,69,83,95,96,99,104,107,126,145,162,172,176,195,196,198,213,228,231,251,253,256,260,265,266,269,272,273,277,279,282,285,290,300,310],
[7,22,25,27,30,40,57,61,66,78,83,87,91,104,115,132,135,140,144,163,182,187,201,203,206,209,219,224,241,254,259,261,266,283,295,296,300,315,318,322,334,346,357,377,382,383,401,405,410])