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
        x = []
        i, n = 0, len(S)
        cnt = 0
        c = ''
        last = 1
        while i < n and cnt < K:
            if S[i].isdigit():
                cnt *= int(S[i])
                if last:
                    x.append(cnt)
                last = 0
            else:
                c += S[i]
                cnt += 1
                x.append(cnt)
                last = 1
            i += 1
        ret = ''
        if last:
            ret = c[-1]
        else:
            print(x)
            print(c)
            l = len(c) - 1
            while x:
                print(K)
                t = x.pop()
                if K % t == 0:
                    ret = c[l]
                    break
                if x and t == x[-1] + 1:
                    l -= 1
                else:
                    K %= t
        print(ret)
        return ret

if __name__ == '__main__':
    a = Solution()
    # a.decodeAtIndex("leet2code3", 10)
    # a.decodeAtIndex("a2345678999999999999999", 1)
    # a.decodeAtIndex("a2b3c4d5e6f7g8h9", 10)
    # a.decodeAtIndex("vk3u5xhq2v", 50)
    # a.decodeAtIndex("ha22", 5)
    # a.decodeAtIndex("vzpp636m8y", 2920)
    a.decodeAtIndex("vk6u5xhq9v", 554)
    a.decodeAtIndex("ixm5xmgo78", 711)