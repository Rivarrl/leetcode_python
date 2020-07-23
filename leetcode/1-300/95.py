# -*- coding: utf-8 -*-
# ======================================
# @File    : 95.py
# @Time    : 2020/7/21 1:08 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [95. 不同的二叉搜索树 II](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/)
    """
    @timeit
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(l, r):
            res = []
            if l > r: res.append(None)
            for i in range(l, r+1):
                left, right = dfs(l, i-1), dfs(i+1, r)
                for j in left:
                    for k in right:
                        root = TreeNode(i)
                        root.left, root.right = j, k
                        res.append(root)
            return res
        if n == 0: return []
        return dfs(1, n)

if __name__ == '__main__':
    a = Solution()
    a.generateTrees(3)