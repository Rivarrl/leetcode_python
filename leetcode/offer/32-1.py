# -*- coding: utf-8 -*-
# ======================================
# @File    : 32-1.py
# @Time    : 2020/5/7 0:50
# @Author  : Rivarrl
# ======================================
# [面试题32 - I. 从上到下打印二叉树](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        stk = [root]
        res = []
        while stk:
            p = stk.pop(0)
            res.append(p.val)
            if p.left: stk.append(p.left)
            if p.right: stk.append(p.right)
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,9,20,null,null,15,7])
    a.levelOrder(x)