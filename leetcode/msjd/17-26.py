# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-26.py
# @Time    : 2020/10/13 21:50
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.26. 稀疏相似度](https://leetcode-cn.com/problems/sparse-similarity-lcci/)
    """
    @timeit
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        # 注意进位，四舍五入不要用round
        d = {}
        for i, row in enumerate(docs):
            for x in row:
                d[x] = d.get(x, []) + [i]
        ns = [len(e) for e in docs]
        rd = {}
        for k, ids in d.items():
            if len(ids) > 1:
                ni = len(ids)
                for di in range(ni):
                    for dj in range(di+1, ni):
                        i, j = ids[di], ids[dj]
                        rd[(i, j)] = rd.get((i, j), 0) + 1
        res = []
        for (i, j), v in rd.items():
            r = ((v / (ns[i] + ns[j] - v)) * 10 ** 5) // 1
            rr = (int(r % 10 >= 5) + (r // 10)) / 10 ** 4
            res.append("{},{}: {:.4f}".format(i, j, rr))
        return res

if __name__ == '__main__':
    a = Solution()
    a.computeSimilarities([[14, 15, 100, 9, 3],
                           [32, 1, 9, 3, 5],
                           [15, 29, 2, 6, 8, 7],
                           [7, 10]])