# -*- coding: utf-8 -*-
# ======================================
# @File    : 5314.py
# @Time    : 2/8/20 10:50 PM
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5314. 跳跃游戏 IV]()
    """
    @timeit
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) > 1:
            narr = [arr[0]]
            for i in range(1, len(arr) - 1):
                if arr[i-1] == arr[i] == arr[i+1]:
                    continue
                narr.append(arr[i])
            narr.append(arr[-1])
            arr = narr[:]
        n = len(arr)
        move = {}
        for i in range(n):
            move[arr[i]] = move.get(arr[i], list()) + [i]
        stk_1 = [(0, 0)]
        vis_1 = {}
        while stk_1:
            i, step = stk_1.pop()
            if i == n - 1:
                return step
            vis_1[i] = step
            a = [j for j in (i-1, i+1) if 0 <= j < n] + [j for j in move[arr[i]] if not i-1 <= j <= i+1]
            for j in a:
                if not j in vis_1:
                    vis_1[j] = step + 1
                    stk_1.insert(0, (j, step + 1))


if __name__ == '__main__':
    a = Solution()
    a.minJumps([100,-23,-23,404,100,23,23,23,3,404])
    a.minJumps([7])
    a.minJumps([7,6,9,6,9,6,9,7])
    a.minJumps([6,1,9])
    a.minJumps([11,22,7,7,7,7,7,7,7,22,13])
