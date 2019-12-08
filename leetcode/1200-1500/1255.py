# -*- coding: utf-8 -*-
# ======================================
# @File    : 1255.py
# @Time    : 2019/11/10 11:24
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

from collections import defaultdict, Counter


class Solution:
    @timeit
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        """
        [1255. 得分最高的单词集合](https://leetcode-cn.com/problems/maximum-score-words-formed-by-letters/)
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


    @timeit
    def maxScoreWords2(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # 位压缩遍历所有情况，1表示选，0表示不选 len(words)<=14, 用二进制表示的话枚举的种类为1<<len(words)
        n = len(words)
        ctr = Counter(letters)
        cw = {e: Counter(e) for e in words}
        res = 0
        for i in range(1 << n):
            cur = defaultdict(int)
            flag = True
            for j in range(n):
                if i & (1<<j):
                    for lt in cw[words[j]]:
                        cur[lt] += cw[words[j]][lt]
                        if cur[lt] > ctr[lt]:
                            flag = False
                            break
                    if not flag: break
            if flag: res = max(res, sum(score[ord(k) - ord('a')] * v for k, v in cur.items()))
        return res


if __name__ == '__main__':
    sol = Solution()
    sol.maxScoreWords2(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])
    sol.maxScoreWords2(words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10])
    sol.maxScoreWords2(words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0])