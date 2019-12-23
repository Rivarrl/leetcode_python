# -*- coding: utf-8 -*-
# ======================================
# @File    : 968.py
# @Time    : 2019/12/23 12:23
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [968. 监控二叉树](https://leetcode-cn.com/problems/binary-tree-cameras/)
    """
    @timeit
    def minCameraCover(self, root: TreeNode) -> int:
        """
        贪心：记录两个属性，是否装监控，是否被监控，由于装监控的一定被监控，所以有三种状态，0：不被监控，1：装监控，2：被监控但没装监控
        """
        def dfs(p):
            nonlocal res
            if not p: return
            left, right = dfs(p.left), dfs(p.right)
            if left == 0 or right == 0:
                res += 1
                return 1
            elif left == 1 or right == 1:
                return 2
            else:
                return 0
        res = 0
        if dfs(root) == 0: res += 1
        return res


if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([0,0,null,0,0])
    a.minCameraCover(x)
    x = construct_tree_node([0,0,null,0,null,0,null,null,0])
    a.minCameraCover(x)
    x = construct_tree_node([0])
    a.minCameraCover(x)