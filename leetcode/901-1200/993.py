# -*- coding: utf-8 -*-
# ======================================
# @File    : 993.py
# @Time    : 2019/12/24 12:22
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [993. 二叉树的堂兄弟节点](https://leetcode-cn.com/problems/cousins-in-binary-tree/)
    """
    @timeit
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        层序遍历
        """
        stk = [root]
        state = 0
        while stk and state == 0:
            stk1 = []
            while stk:
                p = stk.pop()
                if p.val == x: state += 1
                if p.val == y: state += 1
                if p.left and p.right and sorted([p.left.val, p.right.val]) == sorted([x, y]): return False
                if p.right: stk1.append(p.right)
                if p.left: stk1.append(p.left)
            stk = stk1[:]
        return state == 2

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,3,4])
    a.isCousins(x, 4, 3)
    x = construct_tree_node([1,2,3,null,4,null,5])
    a.isCousins(x, 5, 4)
    x = construct_tree_node([1,2,3,null,4])
    a.isCousins(x, 2, 3)