# -*- coding: utf-8 -*-
# ======================================
# @File    : 992.py
# @Time    : 2019/12/23 20:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [992. K 个不同整数的子数组](https://leetcode-cn.com/problems/subarrays-with-k-different-integers/)
    滑动窗口
    """
    @timeit
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        count = [0] * (max(A) + 1)
        res = window = left = 0
        for right in range(len(A)):
            if count[A[right]] == 0: window += 1
            count[A[right]] += 1
            while window > K:
                count[A[left]] -= 1
                if count[A[left]] == 0: window -= 1
                left += 1
            if window == K:
                j = left
                while window == K:
                    count[A[j]] -= 1
                    if count[A[j]] == 0: window -= 1
                    j += 1
                    res += 1
                for i in range(left, j):
                    if count[A[i]] == 0: window += 1
                    count[A[i]] += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.subarraysWithKDistinct(A = [1,2,1,2,3], K = 2)
    a.subarraysWithKDistinct(A = [1,2,1,3,4], K = 3)
    a.subarraysWithKDistinct([1,2], 1)
    a.subarraysWithKDistinct([2,1,1,1,2], 1)