# -*- coding: utf-8 -*-
# ======================================
# @File    : 5273.py
# @Time    : 2019/11/24 10:34
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    5273. 搜索推荐系统
    """
    @timeit
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = {}
        for product in products:
            p = trie
            for i, e in enumerate(product):
                if not e in p:
                    p[e] = {}
                p = p[e]
            p['#'] = p.get('#', 0) + 1
        def dfs(res, d, cur):
            if len(res) == 3: return
            p = d
            if '#' in p:
                res.extend([cur] * min(3-len(res), p['#']))
                if len(p) == 1: return
            for i in range(26):
                a = chr(ord('a') + i)
                if not a in p: continue
                dfs(res, p[a], cur+a)

        n = len(searchWord)
        res = [list() for _ in range(n)]
        for i in range(n):
            c = searchWord[i]
            if not c in trie: break
            dfs(res[i], trie[c], searchWord[:i+1])
            trie = trie[c]
        return res


if __name__ == '__main__':
    a = Solution()
    a.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse")
