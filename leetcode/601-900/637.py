# -*- coding: utf-8 -*-
# ======================================
# @File    : 637.py
# @Time    : 2020/9/12 0:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
class Solution:
    """
    [637. 二叉树的层平均值](https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/)
    """
    @timeit
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        stk = []
        res = []
        if root:
            stk.append(root)
            while stk:
                cur = []
                m = 0
                for p in stk:
                    m += p.val
                    if p.right:
                        cur.insert(0, p.right)
                    if p.left:
                        cur.insert(0, p.left)
                res.append(m / len(stk))
                stk = cur
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([3,9,20,null,null,15,7])
    a.averageOfLevels(x)