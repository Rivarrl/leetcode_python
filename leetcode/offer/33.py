# -*- coding: utf-8 -*-
# ======================================
# @File    : 33.py
# @Time    : 2020/5/6 21:48
# @Author  : Rivarrl
# ======================================
# [面试题33. 二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)
from algorithm_utils import *

class Solution:
    @timeit
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(set(postorder)) < len(postorder): return False
        def dfs(arr):
            if not arr or len(arr) == 1: return True
            i, j = 0, len(arr) - 1
            while i < j:
                if arr[i] < arr[-1]:
                    i += 1
                elif arr[j] >= arr[-1]:
                    j -= 1
                else:
                    return False
            return dfs(arr[:i]) and dfs(arr[i:-1])
        return dfs(postorder)

    @timeit
    def verifyPostorder2(self, postorder: List[int]) -> bool:
        stk = []
        last = 0x3f3f3f3f
        for x in postorder[::-1]:
            if x > last: return False
            while stk and x < stk[-1]:
                last = stk.pop()
            stk.append(x)
        return True


if __name__ == '__main__':
    a = Solution()
    # a.verifyPostorder([1,6,3,2,5])
    a.verifyPostorder([1,3,2,6,5])
    # a.verifyPostorder([5, 2, -17, -11, 25, 76, 62, 98, 92, 61])
