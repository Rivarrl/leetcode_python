# -*- coding: utf-8 -*-
# ======================================
# @File    : 5650.py
# @Time    : 2021/1/10 18:18
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5650. 执行交换操作后的最小汉明距离]()
    """
    @timeit
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        from collections import defaultdict, Counter
        n = len(source)
        dsu = [i for i in range(n)]
        def find(u):
            if dsu[u] != u:
                dsu[u] = find(dsu[u])
            return dsu[u]
        def union(u, v):
            x, y = find(u), find(v)
            if x != y:
                dsu[x] = y
        for u, v in allowedSwaps:
            union(u, v)
        for u in range(n): find(u)
        d = defaultdict(list)
        for u in range(n):
            d[dsu[u]].append(u)
        res = 0
        for color, nodes in d.items():
            ctr = Counter([source[u] for u in nodes])
            for u in nodes:
                if ctr[target[u]] > 0:
                    ctr[target[u]] -= 1
                else:
                    res += 1
        return res

if __name__ == '__main__':
    a = Solution()
    # a.minimumHammingDistance(source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]])
    # a.minimumHammingDistance(source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = [])
    # a.minimumHammingDistance(source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]])
    a.minimumHammingDistance([41,37,51,100,25,33,90,49,65,87,11,18,15,18],
[41,92,69,75,29,13,53,21,17,81,33,19,33,32],
[[0,11],[5,9],[6,9],[5,7],[8,13],[4,8],[12,7],[8,2],[13,5],[0,7],[6,4],[8,9],[4,12],[6,1],[10,0],[10,2],[7,3],[11,10],[5,2],[11,1],[3,0],[8,5],[12,6],[2,1],[11,2],[4,9],[2,9],[10,6],[12,10],[4,13],[13,2],[11,9],[3,6],[0,4],[1,10],[5,11],[12,1],[10,4],[6,2],[10,7],[3,13],[4,5],[13,10],[4,7],[0,12],[9,10],[9,3],[0,5],[1,9],[5,10],[8,0],[12,11],[11,4],[7,9],[7,2],[13,9],[12,3],[8,6],[7,6],[8,12],[4,3],[7,13],[0,13],[2,0],[3,8],[8,1],[13,6],[1,4],[0,9],[2,3],[8,7],[4,2],[9,12]])