# -*- coding: utf-8 -*-
# ======================================
# @File    : 102.py
# @Time    : 2020/5/13 0:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
    """
    @timeit
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        stk = [root]
        res = []
        while stk:
            res.append([])
            tmp = []
            for p in stk:
                res[-1].append(p.val)
                if p.left: tmp.append(p.left)
                if p.right: tmp.append(p.right)
            stk = tmp[:]
        return res



if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,9,20,null,null,15,7])
    a.levelOrder(x)