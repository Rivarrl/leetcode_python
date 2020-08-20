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
        from queue import PriorityQueue
        n = len(s)
        miss = [0] * 3
        ctr = 0
        pq = PriorityQueue()
        for i in range(n):
            if i == 0 or s[i] == s[i-1]:
                ctr += 1
            else:
                pq.put((ctr % 3, ctr, s[i-1]))
                ctr = 1
            if 9 >= ord(s[i]) - ord('0') >= 0:
                miss[0] = 1
            elif ord('a') <= ord(s[i]) <= ord('z'):
                miss[1] = 1
            else:
                miss[2] = 1
        sms = sum(miss)
        if n < 6: return max(3 - sms, 6 - n)



if __name__ == '__main__':
    a = Solution()
    # a.strongPasswordChecker("666")
    # a.strongPasswordChecker("Tql333")
    a.strongPasswordChecker("gG2222233544gpg3444rrrrrrr")