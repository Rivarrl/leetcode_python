# -*- coding: utf-8 -*-
# ======================================
# @File    : 5145
# @Time    : 2020/1/11 22:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5145. 祖父节点值为偶数的节点和]()
    """
    @timeit
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        stk = [(root, 0, 0)]
        while stk:
            p, v1, v2 = stk.pop()
            res += p.val * v2
            x = 1 if p.val & 1 == 0 else 0
            if p.right:
                stk.insert(0, (p.right, x, v1))
            if p.left:
                stk.insert(0, (p.left, x, v1))
        return res


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([6,7,8,2,7,1,3,9,null,1,4,null,null,null,5])
    a.sumEvenGrandparent(x)