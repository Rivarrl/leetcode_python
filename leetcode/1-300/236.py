# -*- coding: utf-8 -*-
# ======================================
# @File    : 236.py
# @Time    : 2019/11/17 10:26
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [236. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)
    """
    @timeit
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node: return
            if node == p or node == q: return node
            left, right = dfs(node.left), dfs(node.right)
            if left and right: return node
            elif left: return left
            elif right: return right
        return dfs(root)

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,5,1,6,2,0,8,null,null,7,4])
    p = x.left
    q = x.right
    a.lowestCommonAncestor(x, p, q)
    q = p.right.right
    a.lowestCommonAncestor(x, p, q)