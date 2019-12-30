# -*- coding: utf-8 -*-
# ======================================
# @File    : 1022.py
# @Time    : 2019/12/30 19:17
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1022. 从根到叶的二进制数之和](https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers/)
    """
    @timeit
    def sumRootToLeaf(self, root: TreeNode) -> int:
        mod = 10 ** 9 + 7
        def dfs(p, s):
            if not p: return
            s = (s << 1) | p.val
            if not p.left and not p.right:
                nonlocal res
                res += s
                res %= mod
                return
            dfs(p.left, s)
            dfs(p.right, s)
        res = 0
        dfs(root, 0)
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,0,1,0,1,0,1])
    a.sumRootToLeaf(x)