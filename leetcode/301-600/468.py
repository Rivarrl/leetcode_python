# -*- coding: utf-8 -*-
# ======================================
# @File    : 468.py
# @Time    : 2019/12/9 19:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [468. 验证IP地址](https://leetcode-cn.com/problems/validate-ip-address/)
    """
    @timeit
    def validIPAddress(self, IP: str) -> str:
        """
        思路:暴力分类讨论
        """
        def v4_valid(s):
            if not s: return False
            if s == '0': return True
            prefix_0 = 0
            for c in s:
                if not ord('0') <= ord(c) <= ord('9'):
                    return False
                if c == '0':
                    prefix_0 += 1
                else:
                    if prefix_0: return False
                    prefix_0 = 0
            return prefix_0 == 0 and int(s) < 256

        def v6_valid(s):
            if not s or len(s) > 4: return False
            if s == '0': return True
            s = s.lower()
            for c in s:
                if not (ord('0') <= ord(c) <= ord('9') or ord('a') <= ord(c) <= ord('f')):
                    return False
            return True

        ret = ["IPv4", "IPv6", "Neither"]
        r = 2
        if '.' in IP:
            # v4
            if IP.count('.') == 3:
                for seg in IP.split('.'):
                    if not v4_valid(seg):
                        break
                else:
                    r = 0
        elif ':' in IP:
            # v6
            if IP.count(':') == 7:
                for seg in IP.split(':'):
                    if not v6_valid(seg):
                        break
                else:
                    r = 1
        return ret[r]

if __name__ == '__main__':
    a = Solution()
    a.validIPAddress("172.16.254.1")
    a.validIPAddress("172.16.254.0")
    a.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")
    a.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334")
    a.validIPAddress("256.256.256.256")