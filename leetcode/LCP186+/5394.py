# -*- coding: utf-8 -*-
# ======================================
# @File    : 5394.py
# @Time    : 2020/4/26 16:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5394. 对角线遍历 II](https://leetcode-cn.com/problems/diagonal-traverse-ii/submissions/)
    """
    @timeit
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        tmp = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j >= len(tmp):
                    tmp.append([])
                tmp[i+j].append(nums[i][j])
        res = []
        for e in tmp:
            res.extend(e[::-1])
        return res


if __name__ == '__main__':
    a = Solution()
    a.findDiagonalOrder(nums = [[1,2,3],[4,5,6],[7,8,9]])
    a.findDiagonalOrder(nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])
    a.findDiagonalOrder(nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]])
    a.findDiagonalOrder(nums = [[1,2,3,4,5,6]])