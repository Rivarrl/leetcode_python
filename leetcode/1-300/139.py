# -*- coding: utf-8 -*-
# ======================================
# @File    : 139.py
# @Time    : 2020/6/25 22:12
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [139. 单词拆分](https://leetcode-cn.com/problems/word-break/)
    """
    @timeit
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

if __name__ == '__main__':
    a = Solution()
    a.wordBreak(s = "leetcode", wordDict = ["leet", "code"])
    a.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"])
    a.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"])
    a.wordBreak("a", ["a"])