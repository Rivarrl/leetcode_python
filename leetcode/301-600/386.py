# -*- coding: utf-8 -*-
# ======================================
# @File    : 386.py
# @Time    : 2019/12/11 11:03
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [386. 字典序排数](https://leetcode-cn.com/problems/lexicographical-numbers/)
    """
    @timeit
    def lexicalOrder(self, n: int) -> List[int]:
        """
        思路: 先序遍历十叉树
        """
        if n < 1: return []
        def dfs(x):
            res.append(x)
            for i in range(x*10, (x+1)*10):
                if i > n: break
                dfs(i)
        res = []
        for i in range(1, min(10, n+1)): dfs(i)
        return res

if __name__ == '__main__':
    a = Solution()
    a.lexicalOrder(13)
    # 2.6s
    a.lexicalOrder(5000000)