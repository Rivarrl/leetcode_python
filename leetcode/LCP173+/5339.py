# -*- coding: utf-8 -*-
# ======================================
# @File    : 5339.py
# @Time    : 2020/3/7 23:28
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1373. 二叉搜索子树的最大键值和](https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree/)
    """
    @timeit
    def maxSumBST(self, root: TreeNode) -> int:
        res = 0
        def dfs(p):
            if not p: return True, 0
            left, right = dfs(p.left), dfs(p.right)
            cur = left[1] + right[1] + p.val
            if p.left and p.val <= p.left.val: return False, cur
            if p.right and p.val >= p.right.val: return False, cur
            if left[0] and right[0]:
                nonlocal res
                res = max(res, cur)
            return left[0] and right[0], cur
        dfs(root)
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,4,3,2,4,2,5,null,null,null,null,null,null,4,6])
    a.maxSumBST(x)
    x = construct_tree_node([4,3,null,1,2,null,null])
    a.maxSumBST(x)
    x = construct_tree_node([-4,-2,-5])
    a.maxSumBST(x)
    x = construct_tree_node([2,1,3])
    a.maxSumBST(x)
    x = construct_tree_node([5,4,8,3,null,6,3])
    a.maxSumBST(x)