# -*- coding: utf-8 -*-
# ======================================
# @File    : 5295.py
# @Time    : 2019/12/29 13:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5295. 和为零的N个唯一整数](https://leetcode-cn.com/problems/find-n-unique-integers-sum-up-to-zero/)
    """
    @timeit
    def sumZero(self, n: int) -> List[int]:
        return [i - (n // 2) for i in range(n)] if n & 1 else [i - (n // 2) for i in range(n+1) if not i == n // 2]


if __name__ == '__main__':
    a = Solution()
    a.sumZero(5)
    a.sumZero(4)
    a.sumZero(3)
    a.sumZero(1)