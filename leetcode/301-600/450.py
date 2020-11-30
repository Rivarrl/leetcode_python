# -*- coding: utf-8 -*-
# ======================================
# @File    : 450.py
# @Time    : 2020/12/1 1:02
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [450. 删除二叉搜索树中的节点](https://leetcode-cn.com/problems/delete-node-in-a-bst/)
    """
    @timeit
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        p, q = root, None
        while p:
            if not p: break
            if p.val == key:
                if not q:
                    t = p.right
                else:

            elif p.val > key:
                p, q = p.left, p
            else:
                p, q = p.right, p
        return root

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([5,3,6,2,4,null,7])
    a.deleteNode(x, 3)
