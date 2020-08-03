# -*- coding: utf-8 -*-
# ======================================
# @File    : 5476.py
# @Time    : 2020/8/3 9:48 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5476. 找出数组游戏的赢家](https://leetcode-cn.com/problems/find-the-winner-of-an-array-game/)
    """
    @timeit
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n: return max(arr)
        i = t = 0
        for j in range(1, n):
            if arr[i] < arr[j]:
                t = 1
                i = j
            else:
                t += 1
            if t == k: break
        return arr[i]

if __name__ == '__main__':
    a = Solution()
    a.getWinner(arr = [2,1,3,5,4,6,7], k = 2)
    a.getWinner(arr = [3,2,1], k = 10)
    a.getWinner(arr = [1,9,8,2,3,7,6,4,5], k = 7)
    a.getWinner(arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000)
    a.getWinner([1,25,35,42,68,70], 2)