# -*- coding: utf-8 -*-
# ======================================
# @File    : 5550.py
# @Time    : 2020/11/14 22:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5550. 拆炸弹]()
    """
    @timeit
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        code = code * 2
        if k > 0:
            for i in range(n):
                res[i] = sum(code[i+1:i+1+k])
        elif k < 0:
            for i in range(n, 2*n):
                res[i-n] = sum(code[i+k:i])
        return res

if __name__ == '__main__':
    a = Solution()
    a.decrypt(code = [5,7,1,4], k = 3)
    a.decrypt(code = [1,2,3,4], k = 0)
    a.decrypt(code = [2,4,9,3], k = -2)