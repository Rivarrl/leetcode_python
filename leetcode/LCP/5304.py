# -*- coding: utf-8 -*-
# ======================================
# @File    : 5304
# @Time    : 2020/1/5 15:07
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    5304. 子数组异或查询
    """
    @timeit
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = [0]
        for e in arr:
            pre += [pre[-1] ^ e]
        return [pre[y+1] ^ pre[x] for x, y in queries]


if __name__ == '__main__':
    a = Solution()
    a.xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]])
    a.xorQueries(arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]])