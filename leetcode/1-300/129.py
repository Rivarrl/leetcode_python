# -*- coding: utf-8 -*-
# ======================================
# @File    : 129.py
# @Time    : 2020/11/2 0:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [129. 求根到叶子节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/)
    """
    @timeit
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, curr):
            c = curr * 10 + root.val
            if not root.left and not root.right:
                nonlocal ans
                ans += c
                return
            if root.left:
                dfs(root.left, c)
            if root.right:
                dfs(root.right, c)
        ans = 0
        if root: dfs(root, 0)
        return ans

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,3])
    a.sumNumbers(x)
    x = construct_tree_node([4,9,0,5,1])
    a.sumNumbers(x)