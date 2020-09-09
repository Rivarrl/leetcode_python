# -*- coding: utf-8 -*-
# ======================================
# @File    : 1576.py
# @Time    : 2020/9/9 12:43 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1576. 替换所有的问号](https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/)
    """
    @timeit
    def modifyString(self, s: str) -> str:
        s = ['z'] + [e for e in s] + ['z']
        for i in range(1, len(s)-1):
            if s[i] == '?':
                if sorted([s[i-1],s[i+1]]) == ['a', 'b']:
                    p = 'c'
                else:
                    p = 'b' if 'a' in (s[i-1], s[i+1]) else 'a'
            else:
                p = s[i]
            s[i] = p
        return ''.join(s[1:-1])

if __name__ == '__main__':
    a = Solution()
    a.modifyString(s = "?zs")
    a.modifyString(s = "ubv?w")
    a.modifyString(s = "j?qg??b")
    a.modifyString(s = "??yw?ipkj?")