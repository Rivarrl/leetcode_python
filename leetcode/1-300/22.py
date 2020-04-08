# -*- coding: utf-8 -*-
# ======================================
# @File    : 22.py
# @Time    : 2020/4/9 0:18
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)
    """
    @timeit
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(i):
            if i == 1: return ["()"]
            pre = dfs(i-1)
            res = set()
            for x in pre:
                for j in range(len(x)):
                    res.add('(' + x[:j] + ')' + x[j:])
            return list(res)
        return dfs(n)

if __name__ == '__main__':
    a = Solution()
    a.generateParenthesis(3)