# -*- coding: utf-8 -*-
# ======================================
# @File    : 1145.py
# @Time    : 2019/12/3 0:12
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def dfs(p):
            if not p: return 0
            nonlocal res
            left = dfs(p.left)
            right = dfs(p.right)
            if left + right >= n // 2 and not (left > n // 2 or right > n // 2) and p.val != x:
                res = True
            return left + right + 1
        res = False
        dfs(root)
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,3,4,5,6,7,8,9,10,11,null,null,null,null])
    a.btreeGameWinningMove(x, 11, 3)
