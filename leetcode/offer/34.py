# -*- coding: utf-8 -*-
# ======================================
# @File    : 34.py
# @Time    : 2020/5/7 21:45
# @Author  : Rivarrl
# ======================================
# [面试题34. 二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)
from algorithm_utils import *

class Solution:
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