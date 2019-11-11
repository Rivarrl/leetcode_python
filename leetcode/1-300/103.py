# -*- coding: utf-8 -*-
# ======================================
# @File    : 103.py
# @Time    : 2019/11/11 10:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        [103. 二叉树的锯齿形层次遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)
        思路：层序遍历用bfs方便，入栈时带一个层数，每层根据其奇偶性决定下一层的入栈顺序
        """
        if not root: return []
        res, tmp = [], []
        stk = [(root, 1)]
        while stk:
            tmp.clear()
            res.append([])
            while stk:
                p, depth = stk.pop()
                res[-1].append(p.val)
                if depth & 1:
                    if p.left: tmp.append((p.left, depth+1))
                    if p.right: tmp.append((p.right, depth+1))
                else:
                    if p.right: tmp.append((p.right, depth+1))
                    if p.left: tmp.append((p.left, depth+1))
            stk = tmp[:]
        return res


if __name__ == '__main__':
    root = construct_tree_node([3,9,20,null,null,15,7])
    a = Solution()
    a.zigzagLevelOrder(root)