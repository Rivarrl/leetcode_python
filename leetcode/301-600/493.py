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

    @timeit
    def reversePairs2(self, nums: List[int]) -> int:
        # 逆序遍历, 二分查找满足条件的最大值的下标, 再将x插入
        import bisect
        q = []
        res = 0
        for x in nums[::-1]:
            rk = bisect.bisect_right(q, (x-1)//2)
            res += rk
            bisect.insort(q, x)
        return res

class Segment:
    def __init__(self, l=None, r=None, v=None):
        self.l = l
        self.r = r
        self.v = v

    @timeit
    def reversePairs3(self, nums: List[int]) -> int:
        # 线段树, 保存rank值
        n = len(nums)
        st = [Segment() for _ in range(4*(n+1))]


if __name__ == '__main__':
    a = Solution()
    a.reversePairs2([1,3,2,3,1])
    a.reversePairs2([2,4,3,5,1])
    a.reversePairs2([7,7,-7,-7,-7,7])
