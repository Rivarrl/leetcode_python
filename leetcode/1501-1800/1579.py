# -*- coding: utf-8 -*-
# ======================================
# @File    : 1579.py
# @Time    : 2021/1/27 16:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1579. 保证图可完全遍历](https://leetcode-cn.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/)
    """
    @timeit
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        

if __name__ == '__main__':
    a = Solution()
    a.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]])
    a.maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]])
    a.maxNumEdgesToRemove(n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]])