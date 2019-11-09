# -*- coding: utf-8 -*-
# ======================================
# @File    : 5.py
# @Time    : 2019/11/9 22:27
# @Author  : Rivarrl
# ======================================

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        [5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)
        思路：动态规划，dp[i][j]表示nums[i:j]是回文串
        """
        n = len(s)
        if n <= 1: return s
        dp = [[False] * n for _ in range(n)]
        m = 1
        res = s[0]
        for right in range(1, n):
            for left in range(right):
                if s[right] == s[left] and (right - left <= 2 or dp[left+1][right-1] == True):
                    dp[left][right] = True
                    if right - left + 1 > m:
                        m = right - left + 1
                        res = s[left:right+1]
        return res

    def longestPalindrome2(self, s: str) -> str:
        """
        Manacher算法
        """
        n = len(s)
        if n <= 1: return s
        # 构造#字符串
        t = "#" + "#".join([e for e in s]) + "#"
        t_len = len(t)
        p = [0] * t_len
        center, r_max = 0, 0
        m, st = 0, 0
        for i in range(t_len):
            if i < r_max:
                mirror = center * 2 - i
                p[i] = min(p[mirror], r_max - i)
            left, right = i - (p[i] + 1), i + (p[i] + 1)
            while left >= 0 and right < t_len and t[left] == t[right]:
                p[i] += 1
                left -= 1
                right += 1
            if i + p[i] > r_max:
                center, r_max = i, i + p[i]
            if p[i] > m:
                m = p[i]
                st = (i - p[i]) // 2
        # print(st, m)
        return s[st: st+m]

if __name__ == '__main__':
    sol = Solution()
    res = sol.longestPalindrome2("aaaa")
    print(res)