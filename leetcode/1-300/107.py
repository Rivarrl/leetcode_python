# -*- coding: utf-8 -*-
# ======================================
# @File    : 107.py
# @Time    : 2020/9/6 1:25
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [107. 二叉树的层次遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)
    """
    @timeit
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        from collections import deque
        if not root: return []
        stk = [root]
        res = deque()
        while stk:
            nxt = []
            res.appendleft([])
            while stk:
                p = stk.pop()
                res[0].append(p.val)
                if p.left:
                    nxt.append(p.left)
                if p.right:
                    nxt.append(p.right)
            while nxt:
                stk.append(nxt.pop())
        return list(res)

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,9,20,null,null,15,7])
    a.levelOrderBottom(x)