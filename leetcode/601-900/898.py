# -*- coding: utf-8 -*-
# ======================================
# @File    : 898.py
# @Time    : 2019/12/6 12:17
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [898. 子数组按位或操作](https://leetcode-cn.com/problems/bitwise-ors-of-subarrays/)
    """
    @timeit
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        """
        思路: 2个set存
        """
        res = set()
        B = set()
        for a in A:
            B = {b | a for b in B} | {a}
            res |= B
        return len(res)


    @timeit
    def subarrayBitwiseORs2(self, A: List[int]) -> int:
        """
        思路: 位运算剪枝来代替两个set轮流io
        """
        # 求天花板值
        max_a = max(A)
        mask = 1
        while mask <= max_a:
            mask <<= 1
        mask -= 1
        res = set()
        for i, a in enumerate(A):
            res.add(a)
            j = i - 1
            cur = a
            while j >= 0 and cur < mask:
                cur |= A[j]
                res.add(cur)
                j -= 1
        return len(res)


if __name__ == '__main__':
    a = Solution()
    a.subarrayBitwiseORs2([0])
    a.subarrayBitwiseORs2([1,1,2])
    a.subarrayBitwiseORs2([1,2,4])