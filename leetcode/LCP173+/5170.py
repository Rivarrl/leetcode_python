# -*- coding: utf-8 -*-
# ======================================
# @File    : 5170.py
# @Time    : 2020/2/23 10:49
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5170. 验证二叉树](https://leetcode-cn.com/problems/validate-binary-tree-nodes/)
    """
    @timeit
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        degree_in = [0] * n
        for i in range(n):
            if leftChild[i] >= 0:
                degree_in[leftChild[i]] += 1
            if rightChild[i] >= 0:
                degree_in[rightChild[i]] += 1
        if len([i for i in range(n) if degree_in[i] == 0]) != 1: return False
        if any(e > 1 or e < 0 for e in degree_in): return False
        return True


if __name__ == '__main__':
    a = Solution()
    a.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1])
    a.validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1])
    a.validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1])
    a.validateBinaryTreeNodes(n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1])
