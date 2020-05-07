# -*- coding: utf-8 -*-
# ======================================
# @File    : 32-2.py
# @Time    : 2020/5/6 23:58
# @Author  : Rivarrl
# ======================================
# [面试题32 - II. 从上到下打印二叉树 II](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        stk = [root]
        res = []
        while stk:
            tmp = []
            res.append([])
            for p in stk:
                if p.left: tmp.append(p.left)
                if p.right: tmp.append(p.right)
                res[-1].append(p.val)
            stk = tmp
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,9,20,null,null,15,7])
    a.levelOrder(x)