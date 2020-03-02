# -*- coding: utf-8 -*-
# ======================================
# @File    : 1081.py
# @Time    : 2020/3/2 14:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1081. 不同字符的最小子序列](https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters/)
    """
    @timeit
    def smallestSubsequence(self, text: str) -> str:
        d = {}
        for c in text:
            d[c] = d.get(c, 0) + 1
        res = []
        for c in text:
            if not c in res:
                while res and c < res[-1] and d[res[-1]] > 0:
                    res.pop()
                res.append(c)
            d[c] -= 1
        return ''.join(res)

    @timeit
    def smallestSubsequence2(self, text: str) -> str:
        # 用位掩码实现
        n = len(text)
        stk = []
        pre = 0
        post = [0] * n
        f = lambda x: ord(x) - ord('a')
        for i in range(n):
            for j in range(i, n):
                post[i] |= (1 << f(text[j]))
        for i, c in enumerate(text):
            if pre & (1 << f(c)):
                continue
            while stk and c < stk[-1] and post[i] & (1 << f(stk[-1])):
                pre ^= (1 << f(stk.pop()))
            pre |= (1 << f(c))
            stk.append(c)
        return ''.join(stk)


if __name__ == '__main__':
    a = Solution()
    a.smallestSubsequence("cdadabcc")
    a.smallestSubsequence2("cdadabcc")
    # a.smallestSubsequence("abcd")
    # a.smallestSubsequence("ecbacba")
    # a.smallestSubsequence("leetcode")
    # a.smallestSubsequence("bccddeacacaceabcbbbbdbebbbaaaa")
    # a.smallestSubsequence("cbaacabcaaccaacababa")
    # a.smallestSubsequence("adaabbcacdbabaeabebc")
    # a.smallestSubsequence("bcbcbcababa")