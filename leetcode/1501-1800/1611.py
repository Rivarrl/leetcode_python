# -*- coding: utf-8 -*-
# ======================================
# @File    : 1611.py
# @Time    : 2020/10/28 1:41 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1611. 使整数变为 0 的最少操作次数](https://leetcode-cn.com/problems/minimum-one-bit-operations-to-make-integers-zero/)
    """
    @timeit
    def minimumOneBitOperations(self, n: int) -> int:
        from collections import deque
        seen = {n}
        q = deque([[n, 0]])
        while q:
            n, step = q.popleft()
            if n == 0: return step
            s1 = n ^ 1
            s2 = n ^ ((n ^ (n-1)) + 1)
            for s in (s1, s2):
                if s not in seen:
                    seen.add(s)
                    q.append([s, step+1])
        return -1

if __name__ == '__main__':
    a = Solution()
    a.minimumOneBitOperations(n = 0)
    a.minimumOneBitOperations(n = 3)
    a.minimumOneBitOperations(n = 6)
    a.minimumOneBitOperations(n = 9)
    a.minimumOneBitOperations(n = 333)
    a.minimumOneBitOperations(n = 10**8 + 3256)