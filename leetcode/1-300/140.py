# -*- coding: utf-8 -*-
# ======================================
# @File    : 140.py
# @Time    : 2020/11/1 22:21
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        from functools import lru_cache
        def _possible(s, words):
            dp = [False] * (n+1)
            dp[0] = True
            for i in range(n+1):
                for j in range(i-1, -1, -1):
                    if dp[j] and s[j:i] in words:
                        dp[i] = True
                        break
            return dp[n]

        n = len(s)
        ws = set(wordDict)
        if not _possible(s, ws): return []
        @lru_cache(None)
        def helper(i):
            res = []
            if i == n:
                res.append("")
            for j in range(i+1, n+1):
                if s[i:j] in ws:
                    back = helper(j)
                    for e in back:
                        cur = s[i:j] + " " + e if e != "" else s[i:j]
                        res.append(cur)
            return res
        return helper(0)

if __name__ == '__main__':
    a = Solution()
    a.wordBreak(s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"])
    a.wordBreak(s = "pineapplepenapple", wordDict = ["apple", "pen", "applepen", "pine", "pineapple"])
    a.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"])