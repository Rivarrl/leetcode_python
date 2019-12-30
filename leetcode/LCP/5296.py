# -*- coding: utf-8 -*-
# ======================================
# @File    : 5296.py
# @Time    : 2019/12/29 13:19
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5296. 两棵二叉搜索树中的所有元素](https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees)
    """
    @timeit
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(p):
            if not p: return
            dfs(p.left)
            res.append(p.val)
            dfs(p.right)
        res = []
        dfs(root1)
        dfs(root2)
        return sorted(res)


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([2,1,4])
    y = construct_tree_node([1,0,3])
    a.getAllElements(x, y)