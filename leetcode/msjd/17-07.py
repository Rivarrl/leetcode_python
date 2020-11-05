# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-07.py
# @Time    : 2020/11/4 1:09 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.07. 婴儿名字](https://leetcode-cn.com/problems/baby-names-lcci/)
    """
    @timeit
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        d = {}
        rd = []
        tot = 0
        for s in synonyms:
            s1, s2 = s[1:-1].split(',')
            if s1 not in d:
                d[s1] = tot
                rd.append(s1)
                tot += 1
            if s2 not in d:
                d[s2] = tot
                rd.append(s2)
                tot += 1
        vd = [0] * tot
        for s in names:
            name, num = s[:-1].split('(')
            num = int(num)
            if name in d:
                vd[d[name]] = int(num)
            else:
                vd.append(num)
                tot += 1
                rd.append(name)
        arr = [i for i in range(tot)]
        def find(u):
            if arr[u] != u:
                arr[u] = find(arr[u])
            return arr[u]
        def union(u, v):
            x, y = find(u), find(v)
            if x == y: return
            arr[y] = x
        for s in synonyms:
            s1, s2 = s[1:-1].split(',')
            u, v = d[s1], d[s2]
            union(u, v)
        for i in range(tot):
            find(i)
        color = {}
        for i, j in enumerate(arr):
            color[j] = color.get(j, []) + [i]
        res = []
        for k, vs in color.items():
            name = sorted(list(map(lambda v: rd[v], vs)))[0]
            val = sum(vd[v] for v in vs)
            res.append('%s(%d)'%(name, val))
        return res

if __name__ == '__main__':
    a = Solution()
    a.trulyMostPopular(names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"])