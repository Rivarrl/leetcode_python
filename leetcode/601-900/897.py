# -*- coding: utf-8 -*-
# ======================================
# @File    : 897.py
# @Time    : 2019/12/1 23:59
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [897. 递增顺序查找树](https://leetcode-cn.com/problems/increasing-order-search-tree/)
    """
    def increasingBST(self, root: TreeNode) -> TreeNode:
        """
        中序遍历，把不对的连接调对
        """
        def dfs(p):
            nonlocal pre, res
            if not p: return
            dfs(p.left)
            if pre: pre.right = p
            else: res = p
            p.left, pre = None, p
            dfs(p.right)
        pre = None
        res = None
        dfs(root)
        return res


    def increasingBST2(self, root: TreeNode) -> TreeNode:
        """
        非递归
        """



if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([5,3,6,2,4,null,8,1,null,null,null,null,null,7,9])
    res = a.increasingBST(x)
    print_tree_node(res)