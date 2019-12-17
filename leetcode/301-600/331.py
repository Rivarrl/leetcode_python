# -*- coding: utf-8 -*-
# ======================================
# @File    : 331.py
# @Time    : 2019/12/17 0:10
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [331. 验证二叉树的前序序列化](https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/)
    """
    @timeit
    def isValidSerialization(self, preorder: str) -> bool:
        """
        是个完全二叉树，除了#以外的点不存在只有一个子树的情况，用栈记录子树数
        """
        if preorder == "#": return True
        arr = preorder.split(',')
        if len(arr) & 1 == 0: return False
        stk = []
        for i in range(len(arr)):
            if arr[i] == "#":
                if not stk: return False
                while stk and stk[-1] == 1:
                    stk.pop()
                if stk: stk[-1] += 1
            else:
                stk.append(0)
        return not stk

    @timeit
    def isValidSerialization2(self, preorder: str) -> bool:
        """
        如果把父节点到子节点的边看作有向边，父节点每次可以使得出度+2，而每个子节点使得入度+1，整体入度等于出度
        """
        arr = preorder.split(',')
        degree = 1
        for p in arr:
            if degree < 0: return False
            if p != "#":
                degree += 2
            degree -= 1
        return degree == 0


if __name__ == '__main__':
    a = Solution()
    a.isValidSerialization2("9,3,4,#,#,1,#,#,2,#,6,#,#")
    a.isValidSerialization2("1,#")
    a.isValidSerialization2("9,#,#,1")
    a.isValidSerialization2("1,#,#,#,#")
    a.isValidSerialization2("#")