# -*- coding: utf-8 -*-
# ======================================
# @File    : 354
# @Time    : 2021/3/4 13:13
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [354. 俄罗斯套娃信封问题](https://leetcode-cn.com/problems/russian-doll-envelopes/)
    """
    @timeit
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        import bisect
        if not envelopes:
            return 0
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        f = [envelopes[0][1]]
        for i in range(1, n):
            num = envelopes[i][1]
            if num > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num

        return len(f)

if __name__ == '__main__':
    a = Solution()
    a.maxEnvelopes(envelopes = [[5,4],[6,4],[6,7],[2,3]])
