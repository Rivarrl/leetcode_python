# -*- coding: utf-8 -*-
# ======================================
# @File    : 93.py
# @Time    : 2020/8/9 0:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [93. 复原IP地址](https://leetcode-cn.com/problems/restore-ip-addresses/)
    """
    @timeit
    def restoreIpAddresses(self, s: str) -> List[str]:
        def f(s, ctr):
            if ctr == 3:
                if not s or (s[0] == '0' and len(s) > 1) or int(s) > 255:
                    return []
                if int(s) < 256:
                    return [s]
            res = []
            for i in range(1,4):
                c = s[:i]
                if not c or int(c) >= 256: break
                for x in f(s[i:], ctr+1):
                    res.append(c + '.' + x)
                if s[0] == '0': break
            return res
        return f(s, 0)

if __name__ == '__main__':
    a = Solution()
    a.restoreIpAddresses("25525511135")
    a.restoreIpAddresses("010010")
    a.restoreIpAddresses("0000")
    a.restoreIpAddresses("00000")