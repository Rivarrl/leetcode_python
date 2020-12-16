# -*- coding: utf-8 -*-
# ======================================
# @File    : 623.py
# @Time    : 2020/12/16 7:25 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [623. 在二叉树中增加一行](https://leetcode-cn.com/problems/add-one-row-to-tree/)
    """
    @timeit
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        from collections import deque
        if d == 1:
            p = TreeNode(v)
            p.left = root
            return p
        stk = deque([[root, 1]])
        while stk:
            p, depth = stk.popleft()
            if depth == d-1:
                t1, t2 = TreeNode(v), TreeNode(v)
                p.left, t1.left, p.right, t2.right = t1, p.left, t2, p.right
                continue
            if p.left:
                stk.append([p.left, depth+1])
            if p.right:
                stk.append([p.right, depth+1])
        return root


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([4,2,6,3,1,5])
    a.addOneRow(x, 1, 2)
    x = construct_tree_node([4,2,null,3,1])
    a.addOneRow(x, 1, 3)