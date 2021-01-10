# -*- coding: utf-8 -*-
# ======================================
# @File    : 5635.py
# @Time    : 2021/1/9 22:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5635. 构建字典序最大的可行序列]()
    """
    @timeit
    def constructDistancedSequence(self, n: int) -> List[int]:
        if n == 1: return [1]
        l = n * 2 - 1
        res = [0] * l
        res[0] = res[n] = n
        seen = [0] * (n + 1)
        seen[n] = 1
        def f(res, i):
            if i == l:
                for j in range(l):
                    if res[j] == 0: return False
                return True
            if res[i] > 0: return f(res, i+1)
            for k in range(n-1, 0, -1):
                if k > 1 and i + k >= l: continue
                if seen[k] == 0:
                    seen[k] = 1
                    if k == 1:
                        res[i] = k
                        if f(res, i+1): return True
                        res[i] = 0
                    elif res[i+k] == 0:
                        res[i] = res[i+k] = k
                        if f(res, i+1): return True
                        res[i] = res[i+k] = 0
                    seen[k] = 0
            return False
        f(res, 1)
        return res

if __name__ == '__main__':
    a = Solution()
    a.constructDistancedSequence(n = 3)
    a.constructDistancedSequence(n = 4)
    a.constructDistancedSequence(n = 5)
    a.constructDistancedSequence(n = 6)
    a.constructDistancedSequence(n = 7)