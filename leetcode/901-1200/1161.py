# -*- coding: utf-8 -*-
# ======================================
# @File    : 1161.py
# @Time    : 2019/12/7 15:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1161. 最大层内元素和](https://leetcode-cn.com/problems/maximum-level-sum-of-a-binary-tree/)
    """
    @timeit
    def maxLevelSum(self, root: TreeNode) -> int:
        """
        思路：二叉树层序遍历
        """
        if not root: return 0
        stk = [root]
        level = res = m = 0
        while stk:
            level += 1
            nxt = []
            cur = 0
            while stk:
                p = stk.pop()
                cur += p.val
                if p.right: nxt.append(p.right)
                if p.left: nxt.append(p.left)
            stk = nxt[:]
            if cur > m:
                m = cur
                res = level
        return res


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,7,0,7,-8,null,null])
    a.maxLevelSum(x)