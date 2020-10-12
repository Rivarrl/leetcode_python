# -*- coding: utf-8 -*-
# ======================================
# @File    : 662.py
# @Time    : 2020/10/12 9:38 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [662. 二叉树最大宽度](https://leetcode-cn.com/problems/maximum-width-of-binary-tree/)
    """
    @timeit
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        stk = [[0, root]]
        res = 0
        while stk:
            tmp = []
            l = r = -1
            for n, p in stk:
                l = n if l == -1 or l > n else l
                r = n if r == -1 or r < n else r
                if p.left: tmp.append([n*2+1, p.left])
                if p.right: tmp.append([n*2+2, p.right])
            res = max(res, r - l + 1)
            stk = tmp[:]
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,3,2,5,3,null,9])
    a.widthOfBinaryTree(x)
    x = construct_tree_node([1,3,null,5,3])
    a.widthOfBinaryTree(x)
    x = construct_tree_node([1,3,2,5])
    a.widthOfBinaryTree(x)
    x = construct_tree_node([1,3,2,5,null,null,9,6,null,null,null,null,null,null,7])
    a.widthOfBinaryTree(x)
