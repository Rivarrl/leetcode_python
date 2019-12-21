# -*- coding: utf-8 -*-
# ======================================
# @File    : 606.py
# @Time    : 2019/12/21 21:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [606. 根据二叉树创建字符串](https://leetcode-cn.com/problems/construct-string-from-binary-tree/)
    """
    @timeit
    def tree2str(self, t: TreeNode) -> str:
        def dfs(p):
            if not p: return ""
            left, right = dfs(p.left), dfs(p.right)
            if not left and not right: return str(p.val)
            left = "({})".format(left)
            right = "({})".format(right) if right else right
            return "{}{}{}".format(p.val, left, right)
        return dfs(t)

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,3,4])
    a.tree2str(x)