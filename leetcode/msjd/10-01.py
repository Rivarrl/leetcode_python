# -*- coding:utf-8 -*-
# 程序员面试金典
# [面试题 10.01. 合并排序的数组](https://leetcode-cn.com/problems/sorted-merge-lcci/)
from algorithm_utils import *


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        for k in range(m+n-1, -1, -1):
            if i < 0:
                A[k] = B[j]
                j -= 1
            elif j < 0:
                A[k] = A[i]
                i -= 1
            elif A[i] >= B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1


if __name__ == '__main__':
    a = Solution()
    a.merge(A = [1,2,3,0,0,0], m = 3, B = [2,5,6], n = 3)
    a.merge(A = [4,5,6,0,0,0], m = 3, B = [1,2,3], n = 3)
    a.merge(A = [1,2,4,5,6,0], m = 5, B = [3], n = 1)
