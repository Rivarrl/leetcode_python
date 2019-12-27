# -*- coding: utf-8 -*-
# ======================================
# @File    : 5292.py
# @Time    : 2019/12/22 10:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5292. 划分数组为连续数字的集合](https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers)
    """
    @timeit
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        from collections import Counter
        n = len(nums)
        if n % k != 0: return False
        ctrs = Counter(nums)
        st = list(sorted(set(nums)))
        for i in range(len(st)):
            if ctrs[st[i]] == 0: continue
            need = ctrs[st[i]]
            for j in range(k):
                if not st[i] + j in ctrs or ctrs[st[i] + j] == 0: return False
                ctrs[st[i] + j] -= need
        return True

if __name__ == '__main__':
    a = Solution()
    a.isPossibleDivide(nums = [1,2,3,3,4,4,5,6], k = 4)
    a.isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3)
    a.isPossibleDivide(nums = [3,3,2,2,1,1], k = 3)
    a.isPossibleDivide(nums = [1,2,3,4], k = 3)