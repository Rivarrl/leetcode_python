# -*- coding: utf-8 -*-
# ======================================
# @File    : 5298.py
# @Time    : 2019/12/29 17:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5298. 口算难题](https://leetcode-cn.com/problems/verbal-arithmetic-puzzle/)
    """
    @timeit
    def isSolvable(self, words: List[str], result: str) -> bool:
        # 列式并合并同类项
        head = [1] * 26
        weights = [0] * 26
        cset = set()
        words.append(result)
        for a, word in enumerate(words):
            n = len(word)
            for i in range(n):
                w = 10 ** (n - 1 - i)
                k = ord(word[i]) - ord('A')
                if i == 0: head[k] = 0
                if a == len(words) - 1: w *= -1
                weights[k] += w
                cset.add(k)
        vis = [0] * 10
        weights = sorted([[weights[i], i] for i in range(26) if i in cset], key=lambda x: abs(x[0]), reverse=True)

        n = len(weights)
        def dfs(j, ans):
            if j == n: return ans == 0
            i = max([i for i in range(10) if vis[i] == 0])
            if i * sum([w[0] for w in weights[j:] if w[0] > 0]) + ans < 0 or i * sum([w[0] for w in weights[j:] if w[0] < 0]) + ans > 0:
                return False
            for i in range(9, -1, -1):
                if (i > 0 or head[weights[j][1]] == 1) and vis[i] == 0:
                    vis[i] = 1
                    if dfs(j+1, ans + i * weights[j][0]): return True
                    vis[i] = 0
            return False
        return dfs(0, 0)


    @timeit
    def isSolvable2(self, words: List[str], result: str) -> bool:
        # 暴力搜索, 血妈超时
        words.append(result)
        words = [w[::-1] for w in words]
        zeros = {w[-1] for w in words}
        vis = [0] * 10
        n = len(words)
        d = {}
        def dfs(i, j, s):
            if i == n - 1:
                if j == len(words[i]):
                    return s == 0
                else:
                    c = words[i][j]
                    a = s % 10
                    if a == 0 and j == len(words[i]) - 1: return False
                    if not c in d or d[c] < 0:
                        if vis[a] == 0:
                            vis[a] = 1
                            d[c] = a
                            if dfs(i, j+1, s//10): return True
                            vis[a] = 0
                            d[c] = -1
                    else:
                        if a == 0 and c in zeros: return False
                        if a == d[c]:
                            return dfs(i, j+1, s//10)
            else:
                if j == len(words[i]):
                    return dfs(i+1, 0, s)
                else:
                    c = words[i][j]
                    if not c in d or d[c] < 0:
                        for k in range(9, -1, -1):
                            if c in zeros and k == 0: continue
                            if vis[k] == 0:
                                vis[k] = 1
                                d[c] = k
                                if dfs(i, j + 1, s + k * (10**j)): return True
                                vis[k] = 0
                                d[c] = -1
                    else:
                        if c in zeros and d[c] == 0: return False
                        return dfs(i, j+1, s + d[c] * (10 ** j))
            return False
        return dfs(0, 0, 0)


    @timeit
    def isSolvable3(self, words: List[str], result: str) -> bool:
        # 改良版暴力搜索, 按位搜
        words.append(result)
        words = [w[::-1] for w in words]
        zeros = {w[-1] for w in words}
        vis = [0] * 10
        n, m = len(words), len(result)
        d = {}
        def dfs(i, j, s):
            if j == m: return s == 0
            if i == n - 1:
                c = words[i][j]
                a = s % 10
                if c in zeros and a == 0: return False
                if c in d and d[c] >= 0:
                    if d[c] == a: return dfs(0, j+1, s // 10)
                else:
                    if vis[a] == 0:
                        d[c] = a
                        vis[a] = 1
                        if dfs(0, j+1, s // 10): return True
                        d[c] = -1
                        vis[a] = 0
            else:
                if j >= len(words[i]):
                    return dfs(i+1, j, s)
                c = words[i][j]
                if c in d and d[c] >= 0:
                    if c in zeros and d[c] == 0: return False
                    return dfs(i+1, j, s + d[c])
                else:
                    for k in range(10):
                        if c in zeros and k == 0: continue
                        if vis[k] == 0:
                            vis[k] = 1
                            d[c] = k
                            if dfs(i+1, j, s + d[c]): return True
                            d[c] = -1
                            vis[k] = 0
            return False
        return dfs(0, 0, 0)


if __name__ == '__main__':
    a = Solution()
    # a.isSolvable3(words = ["SEND","MORE"], result = "MONEY")
    # a.isSolvable3(words = ["SIX","SEVEN","SEVEN"], result = "TWENTY")
    # a.isSolvable3(words = ["THIS","IS","TOO"], result = "FUNNY")
    # a.isSolvable2(words = ["LEET","CODE"], result = "POINT")
    # a.isSolvable2(["THAT","IS","WHY","IT","IS"], "FALSE")
    a.isSolvable3(["HOPE","THIS","HELPS","OTHER"], "PEOPLE")
