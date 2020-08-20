# -*- coding: utf-8 -*-
# ======================================
# @File    : 111.py
# @Time    : 2020/8/21 0:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def minDepth(self, root: TreeNode) -> int:
        from collections import deque
        if not root: return 0
        stk = deque([(root, 1)])
        while stk:
            p, s = stk.pop()
            q = 0
            if p.left: stk.appendleft((p.left, s+1))
            else: q |= 1
            if p.right: stk.appendleft((p.right, s+1))
            else: q |= 2
            if q == 3: return s
        return -1

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,9,20,null,null,15,7])
    a.minDepth(x)