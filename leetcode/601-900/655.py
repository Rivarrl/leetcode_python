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
        stk = [root]
        rec = []
        level = 0
        while stk and any(e is not None for e in stk):
            tmp = []
            rec.append(list())
            for p in stk:
                if p is not None:
                    pv = str(p.val)
                    tmp.append(p.left)
                    tmp.append(p.right)
                else:
                    pv = ''
                    tmp.extend([None, None])
                rec[level].append(pv)
            stk = tmp[:]
            level += 1
        res = [[''] * ((1 << level) - 1) for _ in range(level)]
        for i in range(level):
            j = (1 << (level - i - 1)) - 1
            s = (1 << (level - i))
            for r in rec[i]:
                res[i][j] = r
                j += s
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2])
    a.printTree(x)
    x = construct_tree_node([1,2,3,null,4])
    a.printTree(x)
    x = construct_tree_node([1,2,5,3,null,null,null,4])
    a.printTree(x)