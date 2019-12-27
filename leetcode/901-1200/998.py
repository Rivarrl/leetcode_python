# -*- coding: utf-8 -*-
# ======================================
# @File    : 998.py
# @Time    : 2019/12/24 18:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [998. 最大二叉树 II](https://leetcode-cn.com/problems/maximum-binary-tree-ii/)
    保证新插入的val在中序遍历的最后一位，也就是只能是右子或者没有右子的根
    """
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        # 递归
        def dfs(p):
            if not p: return TreeNode(val)
            if p.val < val:
                q = TreeNode(val)
                q.left = p
                return q
            else:
                p.right = dfs(p.right)
            return p
        return dfs(root)


    def insertIntoMaxTree2(self, root: TreeNode, val: int) -> TreeNode:
        # 非递归
        dummy = TreeNode(0)
        dummy.right = root
        pre, cur = dummy, root
        while cur.right and cur.val > val:
            pre, cur = cur, cur.right
        p = TreeNode(val)
        if cur.val > val:
            cur.right = p
        else:
            p.left, pre.right = cur, p
        return dummy.right


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([4,1,3,null,null,2])
    a.insertIntoMaxTree2(x, 5)
    x = construct_tree_node([5,2,4,null,1])
    a.insertIntoMaxTree2(x, 3)
    x = construct_tree_node([5,2,3,null,1])
    a.insertIntoMaxTree2(x, 4)