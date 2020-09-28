# -*- coding: utf-8 -*-
# ======================================
# @File    : 145.py
# @Time    : 2020/9/29 0:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [145. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)
    """
    @timeit
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        def f(root):
            if not root: return []
            res = f(root.left)
            res += f(root.right)
            return res + [root.val]
        return f(root)

    @timeit
    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        # 迭代
        if not root: return []
        p = root
        q = None
        stk, res = [], []
        while stk or p:
            while p:
                stk.append(p)
                p = p.left
            t = stk[-1]
            if t.right and t.right != q:
                p = t.right
            else:
                res.append(stk.pop().val)
                q = t
        return res

    @timeit
    def postorderTraversal3(self, root: TreeNode) -> List[int]:
        # Morris


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,null,2,null,null,3])
    a.postorderTraversal2(x)