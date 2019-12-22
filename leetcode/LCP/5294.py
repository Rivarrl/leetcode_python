# -*- coding: utf-8 -*-
# ======================================
# @File    : 5294.py
# @Time    : 2019/12/22 10:52
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        stk = [e for e in initialBoxes if status[e] == 1]
        vis = [0] * len(status)
        for i in range(len(status)):
            if i in initialBoxes:
                vis[i] |= 1
            if status[i] == 1:
                vis[i] |= 2
        res = 0
        while stk:
            i = stk.pop()
            res += candies[i]
            for x in containedBoxes[i]:
                if vis[x] == 3: continue
                vis[x] |= 1
                if vis[x] == 3:
                    stk.insert(0, x)
            for j in keys[i]:
                if vis[j] == 3: continue
                vis[j] |= 2
                if vis[j] == 3:
                    stk.insert(0, j)
        return res


if __name__ == '__main__':
    a = Solution()
    a.maxCandies(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0])
    a.maxCandies(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0])
    a.maxCandies(status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1])
    a.maxCandies(status = [1], candies = [100], keys = [[]], containedBoxes = [[]], initialBoxes = [])
    a.maxCandies(status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0])