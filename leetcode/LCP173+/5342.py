# -*- coding: utf-8 -*-
# ======================================
# @File    : 5342.py
# @Time    : 2020/2/16 10:47
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5342. 最多可以参加的会议数目](https://leetcode-cn.com/problems/maximum-number-of-events-that-can-be-attended/)
    """
    @timeit
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x:x[1])
        date = set()
        for x, y in events:
            for z in range(x, y+1):
                if not z in date:
                    date.add(z)
                    break
        return len(date)

if __name__ == '__main__':
    a = Solution()
    # a.maxEvents([[1,2],[2,3],[3,4]])
    # a.maxEvents([[1,2],[2,3],[3,4],[1,2]])
    # a.maxEvents([[1,4],[4,4],[2,2],[3,4],[1,1]])
    # a.maxEvents([[1,100000]])
    # a.maxEvents([[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]])
    a.maxEvents([[1,2],[1,2],[3,3],[1,5],[1,5]])