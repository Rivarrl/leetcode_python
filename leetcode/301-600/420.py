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
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        miss = [0] * 3
        counts = [0] * 3
        fix = i = 0
        while i < n:
            cur = password[i]
            if 9 >= ord(password[i]) - ord('0') >= 0:
                miss[0] = 1
            elif ord('a') <= ord(password[i]) <= ord('z'):
                miss[1] = 1
            else:
                miss[2] = 1
            j = i+1
            while j < n and password[j] == cur:
                j += 1
            l = j - i
            if l >= 3:
                fix += l // 3
                counts[l % 3] += 1
            i = j
        sms = 3 - sum(miss)
        if n < 6: return max(sms, 6 - n)
        if n <= 20: return max(sms, fix)
        rms = rm = n - 20
        # 删除3n
        if rm < counts[0]:
            return max(sms, fix - rm) + rms
        rm -= counts[0]
        fix -= counts[0]
        # 删除3n+1
        if rm < counts[1] * 2:
            return max(sms, fix - rm//2) + rms
        # 删除3n+2
        rm -= counts[1] * 2
        fix -= counts[1]
        return max(sms, fix - rm//3) + rms

if __name__ == '__main__':
    a = Solution()
    # a.strongPasswordChecker("666")
    # a.strongPasswordChecker("Tql333")
    a.strongPasswordChecker("gG2222233544gpg3444rrrrrrr")