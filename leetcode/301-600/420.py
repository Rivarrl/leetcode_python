# -*- coding: utf-8 -*-
# ======================================
# @File    : 420.py
# @Time    : 2020/7/30 12:01 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [420. 强密码检验器](https://leetcode-cn.com/problems/strong-password-checker/)
    """
    @timeit
    def strongPasswordChecker(self, s: str) -> int:
        n = len(s)
        miss = [0] * 3
        loc = []
        for i in range(n):
            if 9 >= ord(s[i]) - ord('0') >= 0:
                miss[0] = 1
            elif ord('a') <= ord(s[i]) <= ord('z'):
                miss[1] = 1
            else:
                miss[2] = 1
        sms = sum(miss)
        if n < 6: return max(3 - sms, 6 - n)
        p = c = 0
        r = [0] * 2
        for i in range(n):
            if i > 0 and s[i] == s[i - 1]:
                p += 1
            else:
                c += p // 3
                if p >= 3 and p % 3 < 2:
                    r[p%3] += 1
                p = 1
        print(r)
        if n <= 20: return max(3 - sms, c)



if __name__ == '__main__':
    a = Solution()
    # a.strongPasswordChecker("666")
    # a.strongPasswordChecker("Tql333")
    a.strongPasswordChecker("gG2222233544gpg3444rrrrrrr")