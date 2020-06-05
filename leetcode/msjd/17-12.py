# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-12.py
# @Time    : 2020/6/4 12:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        def dfs(p):
            if not p: return
            nonlocal head, last
            dfs(p.left)
            p.left = None
            if not last:
                head = p
            else:
                last.right = p
            last = p
            dfs(p.right)
        head = last = None
        dfs(root)
        return head

    @timeit
    def convertBiNode2(self, root: TreeNode) -> TreeNode:
        # 非递归
        stk = []
        last = head = TreeNode(-1)
        p = root
        while p or stk:
            while p:
                stk.append(p)
                p = p.left
            p = stk.pop()
            p.left = None
            last.right = p
            last = p
            p = p.right
        return head.right

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([4,2,5,1,3,null,6,0])
    a.convertBiNode2(x)