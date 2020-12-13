# -*- coding: utf-8 -*-
# ======================================
# @File    : 04-12.py
# @Time    : 2020/12/11 22:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 04.12. 求和路径](https://leetcode-cn.com/problems/paths-with-sum-lcci/)
    """
    @timeit
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def f(root, pre, tot):
            nonlocal res
            if not root: return
            tot += root.val
            pre = {**pre}
            if tot - sum in pre:
                res += pre[tot-sum]
            pre[tot] = pre.get(tot, 0) + 1
            f(root.left, pre, tot)
            f(root.right, pre, tot)

        res = 0
        if root: f(root, {0:1}, 0)
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([5,4,8,11,null,13,4,7,2,null,null,null,null,5,1])
    a.pathSum(x, 22)
    x = construct_tree_node([1])
    a.pathSum(x, 0)
    x = construct_tree_node([-2,null,-3])
    a.pathSum(x, -3)
    x = construct_tree_node([0,1,1])
    a.pathSum(x, 0)