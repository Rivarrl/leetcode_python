# -*- coding: utf-8 -*-
# ======================================
# @File    : 1203.py
# @Time    : 2021/1/13 18:27
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1203. 项目管理](https://leetcode-cn.com/problems/sort-items-by-groups-respecting-dependencies/)
    """
    @timeit
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:


if __name__ == '__main__':
    a = Solution()
    a.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]])
    a.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]])
