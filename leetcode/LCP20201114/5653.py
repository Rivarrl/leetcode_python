# -*- coding: utf-8 -*-
# ======================================
# @File    : 5653.py
# @Time    : 2021/1/17 10:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5653. 可以形成最大正方形的矩形数目](https://leetcode-cn.com/contest/weekly-contest-224/problems/number-of-rectangles-that-can-form-the-largest-square/)
    """
    @timeit
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        arr = [min(rec) for rec in rectangles]
        return arr.count(max(arr))

if __name__ == '__main__':
    a = Solution()
    a.countGoodRectangles(rectangles = [[5,8],[3,9],[5,12],[16,5]])
    a.countGoodRectangles(rectangles = [[2,3],[3,7],[4,3],[3,7]])