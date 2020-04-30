# -*- coding: utf-8 -*-
# ======================================
# @File    : 68-1.py
# @Time    : 2020/4/30 23:15
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: return self.lowestCommonAncestor(root, q, p)
        def dfs(c):
            if not c: return
            if c.val > q.val:
                return dfs(c.left)
            elif c.val < p.val:
                return dfs(c.right)
            else:
                return c
        return dfs(root)

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([6,2,8,0,4,7,9,null,null,3,5])
    p = x.left
    q = x.right
    a.lowestCommonAncestor(x, p, q)
    q = p.right
    a.lowestCommonAncestor(x, p, q)
    x = construct_tree_node([2,1])
    p, q = x, x.left
    a.lowestCommonAncestor(x, p, q)