# -*- coding: utf-8 -*-
# ======================================
# @File    : 5294.py
# @Time    : 2019/12/22 10:52
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5294. 你能从盒子里获得的最大糖果数](https://leetcode-cn.com/problems/maximum-candies-you-can-get-from-boxes/)
    """
    @timeit
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        stk = [e for e in initialBoxes if status[e] == 1]
        bag = [0] * len(status)
        for i in range(len(status)):
            if i in initialBoxes:
                bag[i] |= 1
            if status[i] == 1:
                bag[i] |= 2
        score = 0
        while stk:
            i = stk.pop()
            score += candies[i]
            for x in containedBoxes[i]:
                if bag[x] == 3: continue
                bag[x] |= 1
                if bag[x] == 3:
                    stk.insert(0, x)
            for j in keys[i]:
                if bag[j] == 3: continue
                bag[j] |= 2
                if bag[j] == 3:
                    stk.insert(0, j)
        return score


if __name__ == '__main__':
    a = Solution()
    a.maxCandies(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0])
    a.maxCandies(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0])
    a.maxCandies(status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1])
    a.maxCandies(status = [1], candies = [100], keys = [[]], containedBoxes = [[]], initialBoxes = [])
    a.maxCandies(status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0])