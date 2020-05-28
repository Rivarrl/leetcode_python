# -*- coding: utf-8 -*-
# ======================================
# @File    : 5418.py
# @Time    : 2020/5/24 10:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5418. 二叉树中的伪回文路径]()
    """
    @timeit
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def ok(c, q):
            if (q & 1) == 0: return c == 0
            r = 0
            while c:
                c &= (c-1)
                r += 1
            return r == 1
        def dfs(p, c, d):
            nonlocal res
            c ^= (1 << p.val)
            if not p.left and not p.right:
                if ok(c, d): res += 1
            if p.left:
                dfs(p.left, c, d + 1)
            if p.right:
                dfs(p.right, c, d + 1)
        res = 0
        dfs(root, 0, 1)
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([2,3,1,3,1,null,1])
    a.pseudoPalindromicPaths(x)
    x = construct_tree_node([2,1,1,1,3,null,null,null,null,null,1])
    a.pseudoPalindromicPaths(x)
    x = construct_tree_node([9])
    a.pseudoPalindromicPaths(x)
