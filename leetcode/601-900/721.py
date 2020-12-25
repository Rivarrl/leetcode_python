# -*- coding: utf-8 -*-
# ======================================
# @File    : 721.py
# @Time    : 2020/12/25 9:40 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [721. 账户合并](https://leetcode-cn.com/problems/accounts-merge/)
    """
    @timeit
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = {}
        rec = []
        tot = 0
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                cur = name + ',' + email
                if cur not in d:
                    d[cur] = tot
                    rec.append(cur)
                    tot += 1
        dsu = [i for i in range(tot)]
        def find(u):
            if u == dsu[u]: return u
            dsu[u] = find(dsu[u])
            return dsu[u]
        def union(u, v):
            x, y = find(u), find(v)
            if x == y: return
            dsu[x] = y
        for account in accounts:
            name = account[0]
            prev = d[name + ',' + account[1]]
            for email in account[2:]:
                cur = d[name + ',' + email]
                union(prev, cur)
                prev = cur
        for i in range(tot):
            find(i)
        dr = {}
        for i in range(tot):
            if rec[dsu[i]] not in dr:
                dr[rec[dsu[i]]] = []
            dr[rec[dsu[i]]].append(rec[i])
        res = []
        for k, vs in dr.items():
            for i, v in enumerate(sorted(vs)):
                name, email = v.split(',')
                if i == 0:
                    res.append([name])
                res[-1].append(email)
        return res

if __name__ == '__main__':
    a = Solution()
    a.accountsMerge(accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])