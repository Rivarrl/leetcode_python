# -*- coding: utf-8 -*-
# ======================================
# @File    : 5332.py
# @Time    : 2020/2/9 10:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5332. 检查整数及其两倍数是否存在](https://leetcode-cn.com/problems/check-if-n-and-its-double-exist/)
    """
    @timeit
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        s1 = set()
        for e in arr:
            if e * 2 in s or e in s1:
                return True
            s.add(e)
            s1.add(e*2)
        return False


if __name__ == '__main__':
    a = Solution()
    a.checkIfExist(arr = [10,2,5,3])
    a.checkIfExist(arr = [7,1,14,11])
    a.checkIfExist(arr = [3,1,7,11])