# -*- coding: utf-8 -*-
# ======================================
# @File    : 1028.py
# @Time    : 2020/6/18 13:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1028. 从先序遍历还原二叉树](https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/)
    """
    @timeit
    def recoverFromPreorder(self, S: str) -> TreeNode:
        i = 0
        n = len(S)
        val = 0
        while i < n and S[i] != '-':
            val = val * 10 + int(S[i])
            i += 1
        head = TreeNode(val)
        stk = [[0, head]]
        while i < n:
            ctr = 0
            while i < n and S[i] == '-':
                ctr += 1
                i += 1
            val = 0
            while i < n and S[i] != '-':
                val = val * 10 + int(S[i])
                i += 1
            p = TreeNode(val)
            if ctr > stk[-1][0]:
                stk[-1][1].left = p
            else:
                while stk[-1][0] >= ctr:
                    stk.pop()
                stk[-1][1].right = p
            stk.append([ctr, p])
        return head


if __name__ == '__main__':
    a = Solution()
    a.recoverFromPreorder("1-2--3--4-5--6--7")
    a.recoverFromPreorder("1-2--3---4-5--6---7")
    a.recoverFromPreorder("1-401--349---90--88")