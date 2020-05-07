# -*- coding: utf-8 -*-
# ======================================
# @File    : 113.py
# @Time    : 2020/5/7 19:22
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [113. 路径总和 II](https://leetcode-cn.com/problems/path-sum-ii/)
    """
    @timeit
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(p, s, path):
            if not p.left and not p.right:
                if s + p.val == sum:
                    res.append(path + [p.val])
            if p.left:
                dfs(p.left, s+p.val, path+[p.val])
            if p.right:
                dfs(p.right, s+p.val, path+[p.val])
        if not root: return []
        res = []
        dfs(root, 0, [])
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([5,4,8,11,null,13,4,7,2,null,null,null,null,5,1])
    a.pathSum(x, 22)