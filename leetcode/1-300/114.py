# -*- coding: utf-8 -*-
# ======================================
# @File    : 114.py
# @Time    : 2020/8/2 18:06
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [114. 二叉树展开为链表](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/)
    """
    def flatten(self, root: TreeNode) -> None:
        if root:
            temp = root.right
            self.flatten(root.left)
            self.flatten(root.right)
            root.right, root.left = root.left, None
            if temp:
                while root.right:
                    root = root.right
                root.right = temp

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,5,3,4,null,6])
    a.flatten(x)
    tree_node_print(x)