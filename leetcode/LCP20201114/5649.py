# -*- coding: utf-8 -*-
# ======================================
# @File    : 5649.py
# @Time    : 2021/1/10 17:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5649. 解码异或后的数组]()
    """
    @timeit
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for x in encoded:
            first ^= x
            res.append(first)
        return res

if __name__ == '__main__':
    a = Solution()
    a.decode(encoded = [1,2,3], first = 1)
    a.decode(encoded = [6,2,7,3], first = 4)