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
        tot = 0
        for s in synonyms:
            s1, s2 = s[1:-1].split(',')
            if s1 not in d:
                d[s1] = tot
                tot += 1
            if s2 not in d:
                d[s2] = tot
                tot += 1
        arr = [i for i in range(tot)]
        def find(u):
            if arr[u] != u:
                arr[u] = find(arr[u])
            return arr[u]
        def union(u, v):
            x, y = find(u), find(v)
            if x == y: return
            arr[y] = x
            find(v)
        for s in synonyms:
            s1, s2 = s[1:-1].split(',')
            u, v = d[s1], d[s2]
            union(u, v)
        print(arr)
        for s in names:
            name, num = s[:-1].split('(')
            num = int(num)


if __name__ == '__main__':
    a = Solution()
    a.trulyMostPopular(names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"])