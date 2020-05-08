# -*- coding: utf-8 -*-
# ======================================
# @File    : 554.py
# @Time    : 2020/5/9 1:19
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [554. 砖墙](https://leetcode-cn.com/problems/brick-wall/)
    """
    @timeit
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)
        d = {}
        for i in range(n):
            pre = 0
            for x in wall[i]:
                if pre > 0: d[pre] = d.get(pre, 0) + 1
                pre += x
        m = 0
        for k, v in d.items():
            m = max(m, v)
        return n - m

if __name__ == '__main__':
    a = Solution()
    a.leastBricks([[1,2,2,1],
      [3,1,2],
      [1,3,2],
      [2,4],
      [3,1,2],
      [1,3,1,1]])