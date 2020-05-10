# -*- coding: utf-8 -*-
# ======================================
# @File    : 5404.py
# @Time    : 2020/5/10 10:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5404. 用栈操作构建数组](https://leetcode-cn.com/problems/build-an-array-with-stack-operations/)
    """
    @timeit
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i, j = 1, 0
        while i <= n and j < len(target):
            res.append("Push")
            if target[j] > i:
                res.append("Pop")
            else:
                j += 1
            i += 1
        return res

if __name__ == '__main__':
    a = Solution()
    a.buildArray([1,3],3)
    a.buildArray([1,2,3],3)
    a.buildArray([1,2],4)
    a.buildArray([2,3,4],4)