# -*- coding: utf-8 -*-
# ======================================
# @File    : 5153.py
# @Time    : 2019/12/28 23:00
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5137. 最大得分的路径数目](https://leetcode-cn.com/contest/biweekly-contest-16/problems/number-of-paths-with-max-score/)
    """
    @timeit
    def deepestLeavesSum(self, root: TreeNode) -> int:
        stk = [root]
        res = 0
        while stk:
            res = 0
            stk1 = []
            for p in stk:
                res += p.val
                if p.right: stk1.append(p.right)
                if p.left: stk1.append(p.left)
            stk = stk1[:]
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,3,4,5,null,6,7,null,null,null,null,null,8])
    a.deepestLeavesSum(x)