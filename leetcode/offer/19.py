# -*- coding: utf-8 -*-
# ======================================
# @File    : 19.py
# @Time    : 2020/4/21 16:53
# @Author  : Rivarrl
# ======================================
# [面试题19. 正则表达式匹配](https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/)
from algorithm_utils import *
class Solution:
    @timeit
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[0][0] = True
        for j in range(m):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j-1] if j > 0 else True
        for i in range(n):
            for j in range(m):
                if p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    if dp[i+1][j-1] or dp[i+1][j]:
                        dp[i+1][j+1] = True
                    elif (s[i] == p[j-1] or p[j-1] == '.') and dp[i][j]:
                        dp[i+1][j+1] = True
                    elif p[j-1] == '.' and dp[i][j+1]:
                        dp[i+1][j+1] = True
                elif s[i] == p[j]:
                    dp[i+1][j+1] = dp[i][j]
        return dp[-1][-1]



if __name__ == '__main__':
    a = Solution()
    a.isMatch('aa', 'a')
    a.isMatch('aa', 'a*')
    a.isMatch('ab', '.*')
    a.isMatch('aab', 'c*a*b')
    a.isMatch('mississippi', 'mis*is*p*.')
    a.isMatch('aaba', 'ab*a*c*a')
    a.isMatch('aaa','ab*a*c*a')
    a.isMatch('aaa', '.*')