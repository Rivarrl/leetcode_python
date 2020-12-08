# -*- coding: utf-8 -*-
# ======================================
# @File    : 5619.py
# @Time    : 2020/12/6 11:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5619. 最小不兼容性]()
    """
    @timeit
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        from functools import lru_cache
        from collections import Counter
        if max(Counter(nums).values()) > k: return -1
        n = len(nums)
        kn = n // k
        nums = sorted(nums)
        inf =(nums[-1] - nums[0]) * k + 1

        @lru_cache(None)
        def solve(st, pre):
            nonlocal kn
            rest = [i for i in range(n) if (1 << i) & st == 0]
            m = len(rest)
            if m == 0: return 0
            if pre >= n: return inf
            # 为新子集分配数字
            if m % kn == 0: return solve(st | (1 << rest[0]), rest[0])
            if m % kn > 1:
                rest = rest[:-(m % kn - 1)]
            res = inf
            for t in rest:
                if nums[t] <= nums[pre]:
                    continue
                res = min(res, nums[t] - nums[pre] + solve(st | (1 << t), t))
            return res
        ret = solve(0, -1)
        if ret >= inf:
            return -1
        return ret


if __name__ == '__main__':
    a = Solution()
    a.minimumIncompatibility(nums = [1,2,1,4], k = 2)
    a.minimumIncompatibility(nums = [6,3,8,1,3,1,2,2], k = 4)
    a.minimumIncompatibility(nums = [5,3,3,6,3,3], k = 3)