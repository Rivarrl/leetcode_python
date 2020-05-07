# -*- coding: utf-8 -*-
# ======================================
# @File    : 32-3.py
# @Time    : 2020/5/6 23:31
# @Author  : Rivarrl
# ======================================
# [面试题32 - III. 从上到下打印二叉树 III](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        stk = [root]
        res = []
        lv = 1
        while stk:
            tmp = []
            res.append([])
            for p in stk:
                if p.right: tmp.append(p.right)
                if p.left: tmp.append(p.left)
                if lv & 1:
                    res[-1] = [p.val] + res[-1]
                else:
                    res[-1].append(p.val)
            stk = tmp
            lv += 1
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,9,20,null,null,15,7])
    a.levelOrder(x)