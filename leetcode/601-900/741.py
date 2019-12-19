# -*- coding: utf-8 -*-
# ======================================
# @File    : 741.py
# @Time    : 2019/12/19 11:24
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [741. 摘樱桃](https://leetcode-cn.com/problems/cherry-pickup/)
    """
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        可看成两个人同时从0，0点摘，走到n-1,n-1的时候最多可摘多少。
        """
        stk = [(0, 0), (0, 0)]
        vis = {}
        vis[(0, 0, 0)] = 1
        while stk:



if __name__ == '__main__':
    a = Solution()
    a.cherryPickup([[0, 1, -1],
                    [1, 0, -1],
                    [1, 1,  1]])