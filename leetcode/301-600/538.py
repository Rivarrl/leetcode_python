# -*- coding: utf-8 -*-
# ======================================
# @File    : 538.py
# @Time    : 2020/9/21 12:14 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [538. 把二叉搜索树转换为累加树](https://leetcode-cn.com/problems/convert-bst-to-greater-tree/)
    """
    @timeit
    def convertBST(self, root: TreeNode) -> TreeNode:
        last = 0
        def f(p):
            if not p: return
            f(p.right)
            nonlocal last
            p.val += last
            last = p.val
            f(p.left)
            return p
        return f(root)

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([5,2,13])
    a.convertBST(x)
    x = construct_tree_node([1,0,4,-2,null,3])
    a.convertBST(x)
    x = construct_tree_node([2,0,3,-4,1])
    a.convertBST(x)