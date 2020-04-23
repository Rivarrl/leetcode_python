# -*- coding: utf-8 -*-
# ======================================
# @File    : 811.py
# @Time    : 2020/4/23 23:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for e in cpdomains:
            t, ws = e.split(' ')
            t = int(t)
            ws = ws.split('.')
            p = ''
            for w in ws[::-1]:
                if not p:
                    p = w
                else:
                    p = w + '.' + p
                d[p] = d.get(p, 0) + t
        return ['{} {}'.format(v, k) for k, v in d.items()]


if __name__ == '__main__':
    a = Solution()
    a.subdomainVisits(["9001 discuss.leetcode.com"])
    a.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])