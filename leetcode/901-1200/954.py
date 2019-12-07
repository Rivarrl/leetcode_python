# -*- coding: utf-8 -*-
# ======================================
# @File    : 954.py
# @Time    : 2019/12/6 13:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [954. 二倍数对数组](https://leetcode-cn.com/problems/array-of-doubled-pairs/)
    """
    @timeit
    def canReorderDoubled(self, A: List[int]) -> bool:
        """
        思路: 分正负数和0
        """
        from collections import Counter
        if A.count(0) & 1: return False
        A = [abs(a) for a in A]
        ctr = Counter(A)
        sa = sorted(set(A))
        for a in sa:
            if ctr[a] == 0: continue
            if a * 2 not in ctr: break
            if ctr.get(a, 0) > ctr.get(a*2, 0): return False
            ctr[a*2] = ctr.get(a*2, 0) - ctr.get(a, 0)
            ctr[a] = 0
        return sum(v for v in ctr.values()) == 0


if __name__ == '__main__':
    a = Solution()
    # a.canReorderDoubled([2,1,2,6])
    # a.canReorderDoubled([3,1,3,6])
    # a.canReorderDoubled([4,-2,2,-4])
    # a.canReorderDoubled([1,2,4,8,16,4])
    a.canReorderDoubled([36,-34,-78,18,-17,30,-15,40,29,-38,15,-30,-3,-39,58,-76,20,-34,-6,-17])