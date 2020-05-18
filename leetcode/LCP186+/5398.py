# -*- coding: utf-8 -*-
# ======================================
# @File    : 5398.py
# @Time    : 2020/5/16 22:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5398. 统计二叉树中好节点的数目]()
    """
    @timeit
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(p, m):
            nonlocal res
            if not p: return
            cur = m
            if m <= p.val:
                cur = p.val
                res += 1
            dfs(p.left, cur)
            dfs(p.right, cur)
        dfs(root, -10001)
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,1,4,3,null,1,5])
    a.goodNodes(x)
    x = construct_tree_node([3,3,null,4,2])
    a.goodNodes(x)
    x = construct_tree_node([1])
    a.goodNodes(x)