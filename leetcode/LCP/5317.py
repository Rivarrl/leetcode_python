# -*- coding: utf-8 -*-
# ======================================
# @File    : 5317.py
# @Time    : 2020/1/19 10:43
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(p):
            left = dfs(p.left) if p.left else None
            right = dfs(p.right) if p.right else None
            if left == True: p.left = None
            if right == True: p.right = None
            if not p.left and not p.right:
                return p.val == target
            return False
        return None if dfs(root) else root

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,3,2,null,2,4])
    res = a.removeLeafNodes(x, 2)
    tree_node_print(res)
    x = construct_tree_node([1,1,1])
    res = a.removeLeafNodes(x, 1)
    tree_node_print(res)