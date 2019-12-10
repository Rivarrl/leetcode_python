# -*- coding: utf-8 -*-
# ======================================
# @File    : 1111.py
# @Time    : 2019/12/10 12:00
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1111. 有效括号的嵌套深度](https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/)
    """
    @timeit
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        """
        思路: 给的是有效括号,不考虑无效的情况,模拟栈计算深度, 分两份,就按深度的奇偶划分到0和1中
        """
        cnt = 0
        res = [0] * len(seq)
        for i, s in enumerate(seq):
            if s == ')':
                cnt -= 1
            res[i] = cnt & 1
            if s == '(':
                cnt += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxDepthAfterSplit("(()())")
    a.maxDepthAfterSplit("()(())()")
    a.maxDepthAfterSplit("()((()))()")