# -*- coding: utf-8 -*-
# ======================================
# @File    : 655.py
# @Time    : 2020/10/9 6:54 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    [655. 输出二叉树](https://leetcode-cn.com/problems/print-binary-tree/)
    """
    @timeit
    def printTree(self, root: TreeNode) -> List[List[str]]:
        if not root: return []
        stk = [[0, root]]
        rec = []
        level = 0
        while stk:
            tmp = []
            rec.append(list())
            while stk:
                n, p = stk.pop()
                rec[level].append([n, p.val])
                if p.right:
                    tmp.append([n*2+2, p.right])
                if p.left:
                    tmp.append([n*2+1, p.left])
            stk = tmp[:]
            level += 1
        res = [[''] * ((1 << level) - 1) for _ in range(level)]
        lv, last = -1, 0
        for i in range(level):
            for j in range(1 << i, 1 << (i+1)):
                if j - 1
        for lv in range(level-1, -1, -1):
            pre = (1 << (level - 1 - lv)) - 1
            for i, v in rec[lv]:
                res[lv][pre + i] = str(v)
        matrix_pretty_print(res)
        print(res)
        return res

if __name__ == '__main__':
    a = Solution()
    # x = construct_tree_node([1,2])
    # a.printTree(x)
    # x = construct_tree_node([1,2,3,null,4])
    # a.printTree(x)
    x = construct_tree_node([1,2,5,3,null,null,null,null,4])
    a.printTree(x)