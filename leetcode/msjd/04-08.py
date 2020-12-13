# -*- coding: utf-8 -*-
# ======================================
# @File    : 04-08.py
# @Time    : 2020/12/11 22:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    [面试题 04.08. 首个共同祖先](https://leetcode-cn.com/problems/first-common-ancestor-lcci/)
    """
    @timeit
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 暴搜+记忆化
        def f(root):
            if not root: return 0
            if root.val in d: return d[root.val]
            res = 0
            if root.val == p.val:
                res |= 1
            if root.val == q.val:
                res |= 2
            res |= f(root.left)
            res |= f(root.right)
            d[root.val] = res
            return res
        d = {}
        def g(root):
            if f(root) == 3:
                if f(root.left) < 3 and f(root.right) < 3:
                    return root
                else:
                    return g(root.left) or g(root.right)
            return None
        return g(root)


    @timeit
    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 递归
        def f(root):
            if not root or root.val == p.val or root.val == q.val: return root
            left = f(root.left)
            right = f(root.right)
            if left and right: return root
            return left if left else right
        return f(root)

if __name__ == '__main__':
    a = Solution()
    nodes = [TreeNode(i) for i in range(9)]
    nodes[2].left, nodes[2].right = nodes[7], nodes[4]
    nodes[5].left, nodes[5].right = nodes[6], nodes[2]
    nodes[1].left, nodes[1].right = nodes[0], nodes[8]
    nodes[3].left, nodes[3].right = nodes[5], nodes[1]
    a.lowestCommonAncestor(nodes[3], nodes[5], nodes[1])
    a.lowestCommonAncestor(nodes[3], nodes[5], nodes[4])