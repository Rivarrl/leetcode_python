# -*- coding: utf-8 -*-
# ======================================
# @File    : 04-09.py
# @Time    : 2020/6/25 0:09
# @Author  : Rivarrl
# ======================================
# [面试题 04.09. 二叉搜索树序列](https://leetcode-cn.com/problems/bst-sequences-lcci/)
from algorithm_utils import *

class Solution:
    @timeit
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        def merge(a, b):
            if len(a) == 0:
                return [b[:]]
            if len(b) == 0:
                return [a[:]]
            res = []
            select1 = merge(a[1:], b)
            select2 = merge(a, b[1:])
            for x in select1:
                res.append([a[0]] + x)
            for x in select2:
                res.append([b[0]] + x)
            return res

        def f(p):
            if not p: return [[]]
            if not p.left and not p.right: return [[p.val]]
            left_arrs = f(p.left) if p.left else [[]]
            right_arrs = f(p.right) if p.right else [[]]
            res = []
            for left_arr in left_arrs:
                for right_arr in right_arrs:
                    merge_res = merge(left_arr, right_arr)
                    for arr in merge_res:
                        res.append([p.val] + arr)
            return res
        return f(root)

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([2,1,3])
    a.BSTSequences(x)
    x = construct_tree_node([4,2,6,1,3,5,7])
    a.BSTSequences(x)
    x = construct_tree_node([1,2])
    a.BSTSequences(x)