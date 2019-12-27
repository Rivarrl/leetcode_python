# -*- coding: utf-8 -*-
# ======================================
# @File    : 394.py
# @Time    : 2019/12/20 11:15
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [394. 字符串解码](https://leetcode-cn.com/problems/decode-string/)
    """
    @timeit
    def decodeString(self, s: str) -> str:
        """
        思路：dfs可解
        """
        # 用栈模拟
        stk = []
        ctr = res = ''
        for i in range(len(s)):
            if s[i] == '[':
                stk.append([res, int(ctr)])
                ctr = res = ''
            elif s[i] == ']':
                pre, cnt = stk.pop()
                res = pre + res * cnt
            elif '0' <= s[i] <= '9':
                ctr += s[i]
            else:
                res += s[i]
        return res


    @timeit
    def decodeString2(self, s: str) -> str:
        # 递归
        def dfs(i):
            ctr = res = ''
            while i < len(s):
                if s[i] == '[':
                    tmp, i = dfs(i+1)
                    res += int(ctr) * tmp
                    ctr = ''
                elif s[i] == ']':
                    return res, i
                elif '0' <= s[i] <= '9':
                    ctr += s[i]
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(0)


if __name__ == '__main__':
    a = Solution()
    a.decodeString2("3[a]2[bc]")
    a.decodeString2("3[a2[c]]")
    a.decodeString2("2[abc]3[cd]ef")