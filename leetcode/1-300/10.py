# -*- coding: utf-8 -*-
# ======================================
# @File    : 10.py
# @Time    : 2019/11/10 21:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def isMatch(self, s: str, p: str) -> bool:
        """
        [10. 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching)
        思路：动态规划，由于p中只包含a-z和.*，规则相比正则简单很多，也就是.代替随机a-z，*代表将前一字符重复0次以上。
        动态规划dp[i][j]表示p的前i+1(0-i)个字符可以匹配到s的前j+1(0-j)个字符，答案就是dp[len(p)-1][len(s)-1]
        所以程序从p的.和*去想，如果p[i] == '.'，那么不符合条件的表达式是'*.'，去匹配一个空字符串，那么有p[i-1]=='.'时，dp[i][j] = False
        """
        ls = len(s) + 1
        lp = len(p) + 1
        dp = [[False for _ in range(ls)] for _ in range(lp)]
        dp[0][0] = True
        for i in range(1, lp):
            for j in range(0, ls):
                if p[i-1] == '.':
                    if i >= 2 and p[i-2] == '*' and j == 0:
                        dp[i][j] = False
                    if j >= 1 and dp[i-1][j-1] == True:
                        dp[i][j] = True
                elif p[i-1] == '*':
                    if dp[i-1][j] == True:
                        dp[i][j] = True
                    elif dp[i][j-1] == True and p[i-2] == '.':
                        dp[i][j] = True
                    elif dp[i-2][j] == True:
                        dp[i][j] = True
                    elif dp[i-1][j-1] == True and (p[i-2] == s[j-1] or p[i-2] == '.'):
                        dp[i][j] = True
                elif j >= 1 and dp[i-1][j-1] == True and p[i-1] == s[j-1]:
                    dp[i][j] = True
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    sol.isMatch("aa", "a*")
    sol.isMatch("aa", "a.")
    sol.isMatch("aa", ".*")
    sol.isMatch("abbbabba", "ab.*aa")