# -*- coding: utf-8 -*-
# ======================================
# @File    : 08-06.py
# @Time    : 2020/8/17 16:51
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 08.06. 汉诺塔问题](https://leetcode-cn.com/problems/hanota-lcci/)
    """
    @timeit
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        # f做的是在ABC中将顺序排列的n个盘子从A移动到C
        def f(n, A, B, C):
            if n == 1:
                C.append(A.pop())
            else:
                f(n-1, A, C, B)
                C.append(A.pop())
                f(n-1, B, A, C)
        f(len(A), A, B, C)

if __name__ == '__main__':
    a = Solution()
    a.hanota(A = [2, 1, 0], B = [], C = [])
    a.hanota(A = [1, 0], B = [], C = [])