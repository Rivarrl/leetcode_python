# -*- coding: utf-8 -*-
# ======================================
# @File    : 997.py
# @Time    : 2019/12/27 11:28
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [997. 找到小镇的法官](https://leetcode-cn.com/problems/find-the-town-judge/submissions/)
    """
    @timeit
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # 找出唯一的入度为N-1出度为0的点
        degree_in = [0] * (N+1)
        degree_out = [0] * (N+1)
        for x, y in trust:
            degree_in[y] += 1
            degree_out[x] += 1
        res = []
        for i in range(1, N + 1):
            if degree_out[i] == 0 and degree_in[i] == N - 1:
                res.append(i)
                if len(res) > 1: return -1
        return res[0] if res else -1


if __name__ == '__main__':
    a = Solution()
    a.findJudge(N = 2, trust = [[1,2]])
    a.findJudge(N = 3, trust = [[1,3],[2,3]])
    a.findJudge(N = 3, trust = [[1,3],[2,3],[3,1]])
    a.findJudge(N = 3, trust = [[1,2],[2,3]])
    a.findJudge(N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]])