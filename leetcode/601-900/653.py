# -*- coding: utf-8 -*-
# ======================================
# @File    : 653.py
# @Time    : 2019/12/21 22:06
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [653. 两数之和 IV - 输入 BST](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/)
    """
    @timeit
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def dfs(p):
            if not p: return False
            if dfs(p.left): return True
            if k - p.val in d: return True
            d.add(p.val)
            return dfs(p.right)
        d = set()
        return dfs(root)

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([5,3,6,2,4,null,7])
    a.findTarget(x, 9)
    a.findTarget(x, 28)