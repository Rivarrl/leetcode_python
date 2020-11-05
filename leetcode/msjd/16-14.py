# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-14.py
# @Time    : 2020/11/5 11:14 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.14. 最佳直线](https://leetcode-cn.com/problems/best-line-lcci/)
    """
    @timeit
    def bestLine(self, points: List[List[int]]) -> List[int]:
        ans = []
        N, max_cnt = len(points), 0
        for i, p1 in enumerate(points):
            slope = {}
            for j, p2 in enumerate(islice(points, i+1, N), i+1):
                if p1[0] == p2[0]:
                    k = None
                else:
                    k = (p2[1]-p1[1]) / (p2[0]-p1[0])
                slope.setdefault(k, [i])
                slope[k].append(j)
            for idx in slope.values():
                if len(idx) > max_cnt:
                    max_cnt = len(idx)
                    ans = idx[:2]
        return ans
if __name__ == '__main__':
    a = Solution()
    a.bestLine([[0,0],[1,1],[1,0],[2,0]])