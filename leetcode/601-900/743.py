# -*- coding: utf-8 -*-
# ======================================
# @File    : 743.py
# @Time    : 2021/3/2 22:23
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [743. 网络延迟时间](https://leetcode-cn.com/problems/network-delay-time/)
    """
    @timeit
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:


if __name__ == '__main__':
    a = Solution()
    a.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)
    a.networkDelayTime(times = [[1,2,1]], n = 2, k = 1)
    a.networkDelayTime(times = [[1,2,1]], n = 2, k = 2)