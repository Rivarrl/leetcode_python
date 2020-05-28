# -*- coding: utf-8 -*-
# ======================================
# @File    : 1452.py
# @Time    : 2020/5/26 19:47
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1452. 收藏清单]()
    """
    @timeit
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        d = {}
        tot = 0
        for comps in favoriteCompanies:
            for c in comps:
                if not c in d:
                    d[c] = tot
                    tot += 1
        n = len(favoriteCompanies)
        dc = {tuple(sorted(d[e] for e in favoriteCompanies[i])):i for i in range(n)}
        ss = set()
        res = []
        favoriteCompanies.sort(key=lambda x:-len(x))
        def ok(x, y):
            i = j = 0
            while i < len(x) and j < len(y):
                if x[i] == y[j]:
                    j += 1
                i += 1
            return j == len(y)
        for comps in favoriteCompanies:
            sc = tuple(sorted(d[e] for e in comps))
            for k in ss:
                if ok(k, sc): break
            else:
                res.append(dc[sc])
            ss.add(sc)
        return sorted(res)

if __name__ == '__main__':
    a = Solution()
    # a.peopleIndexes(favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]])
    # a.peopleIndexes(favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]])
    # a.peopleIndexes(favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]])
    a.peopleIndexes([["nxaqhyoprhlhvhyojanr","ovqdyfqmlpxapbjwtssm","qmsbphxzmnvflrwyvxlc","udfuxjdxkxwqnqvgjjsp","yawoixzhsdkaaauramvg","zycidpyopumzgdpamnty"],
                     ["nxaqhyoprhlhvhyojanr","ovqdyfqmlpxapbjwtssm","udfuxjdxkxwqnqvgjjsp","yawoixzhsdkaaauramvg","zycidpyopumzgdpamnty"],
                     ["ovqdyfqmlpxapbjwtssm","qmsbphxzmnvflrwyvxlc","udfuxjdxkxwqnqvgjjsp","yawoixzhsdkaaauramvg","zycidpyopumzgdpamnty"]])