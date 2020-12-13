# -*- coding: utf-8 -*-
# ======================================
# @File    : 5245.py
# @Time    : 2020/12/13 11:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5245. 堆叠长方体的最大高度]()
    """
    @timeit
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        arr = []
        for i, e in enumerate(cuboids):
            arr.append([e[0], e[1], e[2], i])
            arr.append([e[0], e[2], e[1], i])
            arr.append([e[1], e[0], e[2], i])
            arr.append([e[1], e[2], e[0], i])
            arr.append([e[2], e[0], e[1], i])
            arr.append([e[2], e[1], e[0], i])
        arr.sort()
        print(arr)
        n = len(arr)
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = arr[i][2]
            for j in range(i):
                if arr[i][3] != arr[j][3] and arr[j][1] <= arr[i][1] and arr[j][2] <= arr[i][2]:
                    dp[i] = max(dp[i], dp[j] + arr[i][2])
        return max(dp)

if __name__ == '__main__':
    a = Solution()
    # a.maxHeight(cuboids = [[50,45,20],[95,37,53],[45,23,12]])
    # a.maxHeight(cuboids = [[38,25,45],[76,35,3]])
    # a.maxHeight(cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]])
    # a.maxHeight([[26,38,38],[37,93,79]])
    a.maxHeight([[92,47,83],
                 [75,20,87],
                 [68,12,83],
                 [12,85,15],
                 [16,24,47],
                 [69,65,35],
                 [96,56,93],
                 [89,93,11],
                 [86,20,41],
                 [69,77,12],
                 [83,80,97],
                 [90,22,36]])