# -*- coding: utf-8 -*-
# ======================================
# @File    : 906
# @Time    : 2020/1/9 21:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [906. 超级回文数](https://leetcode-cn.com/problems/super-palindromes/)
    """
    @timeit
    def superpalindromesInRange(self, L: str, R: str) -> int:
        # 思路: 构造回文串, '', '0', '1'..开始向两侧添加, 由于不能按顺序插入得排序, 超时了
        l, r = int(L), int(R)
        stk = ['']
        stk1 = [str(i) for i in range(10)]
        res = 0
        while stk:
            stk2 = []
            for s in stk:
                if s and not s.startswith('0'):
                    n = int(s)
                    x = n ** 2
                    if l <= x <= r and str(x) == str(x)[::-1]:
                        res += 1
                    elif x > r:
                        return res
                for i in range(10):
                    p = str(i) + s + str(i)
                    stk2.append(p)
            stk = stk1[:]
            stk1 = sorted(stk2)

    @timeit
    def superpalindromesInRange2(self, L: str, R: str) -> int:
        # 改变构造的方法, 123 -> 12321, 123321
        def mirrors(x):
            return int(str(x) + str(x)[::-1]), int(str(x)[:-1] + str(x)[::-1])
        def is_mirror(x):
            return str(x) == str(x)[::-1]
        l, r = int(int(L) ** 0.5), int(int(R) ** 0.5) + 1
        res = 0
        for i in range(1, 100000):
            p, q = mirrors(i)
            if l <= p < r and is_mirror(p**2): res += 1
            if l <= q < r and is_mirror(q**2): res += 1
            if q > r: break
        return res


if __name__ == '__main__':
    a = Solution()
    # a.superpalindromesInRange("444", "17017")
    # a.superpalindromesInRange2("444", "17017")
    # a.superpalindromesInRange("4", "100000000000000000")
    # a.superpalindromesInRange2("4", "100000000000000000")
    # a.superpalindromesInRange("1", "19028")
    # a.superpalindromesInRange2("1", "19028")
    # a.superpalindromesInRange("1", "12")
    # a.superpalindromesInRange2("1", "12")
    a.superpalindromesInRange("396157669377720", "999999999999999999")
    a.superpalindromesInRange2("396157669377720", "999999999999999999")