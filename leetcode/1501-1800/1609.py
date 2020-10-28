# -*- coding: utf-8 -*-
# ======================================
# @File    : 1609.py
# @Time    : 2020/10/28 12:58 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1609. 奇偶树](https://leetcode-cn.com/problems/even-odd-tree/)
    """
    @timeit
    def isEvenOddTree(self, root: TreeNode) -> bool:
        stk = [root]
        odd = 0
        def op(p, r, t=0):
            if t == 2: return
            if r == 0:
                if p.left: tmp.append(p.left)
            if r == 1:
                if p.right: tmp.append(p.right)
            op(p, r ^ 1, t+1)
        while stk:
            tmp = []
            last = 0
            for p in stk:
                if p.val & 1 == odd or p.val <= last: return False
                last = p.val
                op(p, odd)
            stk = tmp[:][::-1]
            odd ^= 1
        return True

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,10,4,3,null,7,9,12,8,null,null,6,null,null,2])
    a.isEvenOddTree(x)
    x = construct_tree_node([5,4,2,3,3,7])
    a.isEvenOddTree(x)
    x = construct_tree_node([5,9,1,3,5,7])
    a.isEvenOddTree(x)
    x = construct_tree_node([1])
    a.isEvenOddTree(x)
    x = construct_tree_node([11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17])
    a.isEvenOddTree(x)
