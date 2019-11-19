# -*- coding: utf-8 -*-
# ======================================
# @File    : 44.py
# @Time    : 2019/11/19 11:16
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [44. 通配符匹配](https://leetcode-cn.com/problems/wildcard-matching/)
    """
    @timeit
    def isMatch(self, s: str, p: str) -> bool:
        """
        思路：和第十题类似，*的规则不同，动态规划，dp[i][j]表示p[:i+1]可以匹配s[:j+1].
        匹配成功的时候，按模式串p的种类可分三种情况：
        case1. p[i] == '?'
        case2. p[i] == '*'
        case3. p[i] == s[j]
        """
        n, m = len(s), len(p)
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[0][0] = 1
        for i in range(1, m+1):
            for j in range(n+1):
                if j > 0 and p[i-1] == '?': # case 1
                    dp[i][j] = dp[i-1][j-1]
                elif j > 0 and p[i-1] == s[j-1]: # case 3
                    dp[i][j] = dp[i-1][j-1]
                elif p[i - 1] == '*': # case 2
                    if j == 0:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        return dp[-1][-1] == 1


    @timeit
    def isMatch2(self, s: str, p: str) -> bool:
        """
        思路：回溯，上面O(n^2)的动态规划只超过了20%的用户，说明一定有比O(n^2)更低的复杂度解法。
        这个回溯，回溯的是'*'的位置，和全排列的回溯不太相像
        i和j分别代表p和s的位置，每次匹配成功则i和j都步进1步，匹配失败则将i回到上一个'*'的正确匹配位置
        """
        # p[i], s[j]
        i, j = 0, 0
        n, m = len(s), len(p)
        # 记录上一个'*'的位置i
        star_rec = 0
        # 记录上一次匹配'*'的s[j]的位置j
        match = -1
        while j < n:
            if i < m and (s[j] == p[i] or p[i] == '?'):
                i += 1
                j += 1
            elif i < m and p[i] == '*':
                star_rec = i
                match = j
                i += 1
            elif match >= 0:
                match += 1
                j = match
                i = star_rec + 1
            else:
                return False
        # 判断p没匹配完的部分，都是'*'就是True
        return all(x == '*' for x in p[i:])


if __name__ == '__main__':
    a = Solution()
    # a.isMatch2(s = "adceb", p = "*a*b")
    # a.isMatch2("aab", "c*a*b")
    # a.isMatch2(s = "acdcb", p = "a*c?b")
    # a.isMatch2(s = "cb", p = "?a")
    # a.isMatch2(s = "", p = "*")
    a.isMatch2('aa', 'a')
