# -*- coding: utf-8 -*-
# ======================================
# @File    : 832
# @Time    : 2021/2/24 13:11
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [832. 翻转图像](https://leetcode-cn.com/problems/flipping-an-image/)
    """
    @timeit
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[1^x for x in one[::-1]] for one in A]

if __name__ == '__main__':
    a = Solution()
    a.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
    a.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])
