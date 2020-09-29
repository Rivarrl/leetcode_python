# -*- coding: utf-8 -*-
# ======================================
# @File    : 701.py
# @Time    : 2020/9/30 0:04
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [701. 二叉搜索树中的插入操作](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/)
    """
    @timeit
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def f(root):
            if not root:
                return TreeNode(val)
            if root.val > val:
                root.left = f(root.left)
            else:
                root.right = f(root.right)
            return root
        return f(root)

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([4,2,7,1,3])
    a.insertIntoBST(x, 5)