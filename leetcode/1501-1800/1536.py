# -*- coding: utf-8 -*-
# ======================================
# @File    : 1536.py
# @Time    : 2020/8/3 12:29 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1536. 排布二进制网格的最少交换次数](https://leetcode-cn.com/problems/minimum-swaps-to-arrange-a-binary-grid/)
    """
    @timeit
    def minSwaps(self, grid: List[List[int]]) -> int:
        # 统计从右向左数第一个1的位置，结果为按从小到大排序
        n = len(grid)
        arr = [0] * n
        for i in range(n):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    arr[i] = j
                    break
        res = 0
        for i in range(n):
            if arr[i] <= i: continue
            k = 0
            j = i+1
            while j < n:
                if arr[j] <= i:
                    k = j
                    break
                j += 1
            if j == n: return -1
            res += (k - i)
            while k > i:
                arr[k], arr[k-1] = arr[k-1], arr[k]
                k -= 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.minSwaps(grid = [[0,0,1],[1,1,0],[1,0,0]])
    a.minSwaps(grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]])
    a.minSwaps(grid = [[1,0,0],[1,1,0],[1,1,1]])