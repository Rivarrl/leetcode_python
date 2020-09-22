# -*- coding: utf-8 -*-
# ======================================
# @File    : 8.py
# @Time    : 2020/9/19 16:51
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def isMagic(self, target: List[int]) -> bool:
        arr = [i+1 for i in range(len(target))]
        arr = arr[1::2] + arr[::2]
        if target[0] != arr[0]: return False
        i = 0
        while i < len(target) and target[i] == arr[i]:
            i += 1
        def f(arr, k, tar):
            if len(arr) == 0: return True
            tmp = arr[1::2] + arr[::2]
            if tmp[:k] == tar[:k]:
                return f(tmp[k:], k, tar[k:])
            return False
        for k in range(i, 0, -1):
            if f(arr[k:], k, target[k:]): return True
        return False

if __name__ == '__main__':
    a = Solution()
    a.isMagic(target = [2,4,3,1,5])
    a.isMagic(target = [5,4,3,2,1])