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
        if not root: return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                prev = self.getPrevNode(root.left)
                prev.left = self.deletePrevNode(root.left)
                prev.right = root.right
                root = prev
        return root

    def deletePrevNode(self, root: TreeNode) -> TreeNode:
        if not root.right: return root.left
        root.right = self.deletePrevNode(root.right)
        return root

    def getPrevNode(self, root: TreeNode) -> TreeNode:
        if not root.right: return root
        return self.getPrevNode(root.right)


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([5,3,6,2,4,null,7])
    a.deleteNode(x, 3)
