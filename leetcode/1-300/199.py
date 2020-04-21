# -*- coding: utf-8 -*-
# ======================================
# @File    : 199.py
# @Time    : 2020/4/22 0:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        stk = [(root, 1)]
        vis = set()
        while stk:
            p, lv = stk.pop(0)
            if not lv in vis:
                res.append(p.val)
                vis.add(lv)
            if p.right:
                stk.append((p.right, lv+1))
            if p.left:
                stk.append((p.left, lv+1))
        return res


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,3,null,5,null,4])
    a.rightSideView(x)
    x = construct_tree_node([1,2,3,4])
    a.rightSideView(x)
