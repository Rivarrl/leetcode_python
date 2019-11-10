# -*- coding: utf-8 -*-
# ======================================
# @File    : 5258.py
# @Time    : 2019/11/10 11:24
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

from collections import defaultdict, Counter


class Solution:
    @timeit
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """
        [5258. 得分最高的单词集合]()
        # 结果集合较小，可以递归
        """
        nw = len(words)
        if nw == 0: return 0
        nwords = []
        d = Counter(letters)
        for i in range(nw):
            cur = 0
            for c in set(words[i]):
                if c not in d: break
                if words[i].count(c) > d[c]: break
                v = ord(c) - ord('a')
                cur += score[v]
            else:
                nwords.append(words[i])
        n = len(nwords)
        if n == 0: return 0
        res = 0
        def dfs(i, cur, d):
            if i == n:
                nonlocal res
                res = max(res, cur)
                return
            tmp = {k: v for k, v in d.items()}
            a = 0
            for c in nwords[i]:
                tmp[c] -= 1
                a += score[ord(c) - ord('a')]
                if tmp[c] < 0:
                    break
            else:
                dfs(i+1, cur + a, tmp)
            dfs(i+1, cur, d)
        dfs(0, 0, d)
        return res


if __name__ == '__main__':
    sol = Solution()
    sol.maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])
