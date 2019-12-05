# -*- coding: utf-8 -*-
# ======================================
# @File    : 493.py
# @Time    : 2019/12/5 11:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import requests

class Solution:
    """
    [493. 翻转对](https://leetcode-cn.com/problems/reverse-pairs/)
    """
    @timeit
    def reversePairs(self, nums: List[int]) -> int:
        """
        思路: 归并排序, 每次归并之前找符合要求的翻转对并计数
        得用内置的sort辅助归并排序,不然会超时
        """
        n = len(nums)
        if n < 2: return 0
        def merge_sort(left, right):
            if left >= right: return 0
            mid = left + right >> 1
            r1 = merge_sort(left, mid)
            r2 = merge_sort(mid+1, right)
            r3 = 0
            lo, hi = left, mid+1
            while lo <= mid and hi <= right:
                if nums[lo] > 2 * nums[hi]:
                    r3 += mid + 1 - lo
                    hi += 1
                else:
                    lo += 1
            nums[left:right+1] = sorted(nums[left:right+1])
            return r1 + r2 + r3
        return merge_sort(0, n-1)

if __name__ == '__main__':
    a = Solution()
    a.reversePairs([1,3,2,3,1])
    a.reversePairs([2,4,3,5,1])
    a.reversePairs([7,7,-7,-7,-7,7])
