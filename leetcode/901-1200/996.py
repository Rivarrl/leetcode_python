# -*- coding: utf-8 -*-
# ======================================
# @File    : 996.py
# @Time    : 2019/11/19 11:16
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [996. 正方形数组的数目](https://leetcode-cn.com/problems/number-of-squareful-arrays/)
    """
    @timeit
    def numSquarefulPerms(self, A: List[int]) -> int:
        """
        思路：回溯
        """
        def dfs(cur, nums):
            if not nums:
                res.append(cur)
            for i, x in enumerate(nums):
                if i > 0 and nums[i] == nums[i-1]: continue
                if not cur or (cur[-1] + x) ** 0.5 % 1 == 0:
                    dfs(cur + [x], nums[:i] + nums[i+1:])
        A.sort()
        res = []
        dfs([], A)
        return len(res)

    @timeit
    def numSquarefulPerms2(self, A: List[int]) -> int:
        """
        思路2：将所有满足条件的数作为连通边，构无向图，最终求哈密顿路径数
        如果两个不同数之和是完全平方数，建立一条边
        如果一个数*2是完全平方数，且这个数在A中重复2次以上，建立一条自环边
        分别以每个节点为起始点求完整遍历所有点的边数
        """
        from collections import defaultdict
        count = defaultdict(int)
        for x in A:
            count[x] += 1
        graph = defaultdict(list)
        nodes = list(count.keys())
        n, N = len(nodes), len(A)
        for i in range(n):
            u = nodes[i]
            if count[u] > 1 and (u * 2) ** 0.5 % 1 == 0:
                graph[u].append(u)
            for j in range(i+1, n):
                v = nodes[j]
                if (v + u) ** 0.5 % 1 == 0:
                    graph[v].append(u)
                    graph[u].append(v)
        def dfs(u, i):
            if i == N:
                nonlocal res
                res += 1
                return
            for v in graph[u]:
                if count[v] > 0:
                    count[v] -= 1
                    dfs(v, i+1)
                    count[v] += 1
        res = 0
        for i in range(n):
            u = nodes[i]
            count[u] -= 1
            dfs(u, 1)
            count[u] += 1
        return res



if __name__ == '__main__':
    a = Solution()
    # a.numSquarefulPerms2([1,17,8])
    # a.numSquarefulPerms2([2,2,2])
    # a.numSquarefulPerms2([1,17,8,8,8])
    a.numSquarefulPerms2([0,0,0,1,1,1])
    a.numSquarefulPerms2([80,1,80,1,3,6,3])