# -*- coding: utf-8 -*-
# ======================================
# @File    : 880.py
# @Time    : 2019/12/9 17:18
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [880. 索引处的解码字符串](https://leetcode-cn.com/problems/decoded-string-at-index/)
    """
    # @timeit
    def decodeAtIndex(self, S: str, K: int) -> str:
        """
        思路: 用一个rec数组记录当前的模式串, 用x记录重复次数
        """
        i = cnt = 0
        c = ''
        x = []
        while i < len(S) and cnt < K:
            if S[i].isdigit():
                cnt *= int(S[i])
                if S[i-1].isdigit(): x[-1][0] = cnt
                else: x.append([cnt, len(c) - 1])
            else:
                c += S[i]
                cnt += 1
                x.append([cnt, len(c) - 1])
            i += 1
        ret = ''
        while x:
            t = x.pop()
            K %= t[0]
            if K == 0:
                ret = c[t[1]]
                break
        return ret

if __name__ == '__main__':
    a = Solution()
    # a.decodeAtIndex("leet2code3", 10)
    # a.decodeAtIndex("a2345678999999999999999", 1)
    # a.decodeAtIndex("a2b3c4d5e6f7g8h9", 10)
    # a.decodeAtIndex("ha22", 5)
    # a.decodeAtIndex("vk3u5xhq2v", 50)
    # a.decodeAtIndex("vzpp636m8y", 2920)
    a.decodeAtIndex("vk6u5xhq9v", 554)
    a.decodeAtIndex("ixm5xmgo78", 711)