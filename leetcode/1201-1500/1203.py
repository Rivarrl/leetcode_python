# -*- coding: utf-8 -*-
# ======================================
# @File    : 1203.py
# @Time    : 2021/1/13 18:27
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1203. 项目管理](https://leetcode-cn.com/problems/sort-items-by-groups-respecting-dependencies/)
    """
    @timeit
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        indegree_group = [0 for _ in range(m)] # 组间入度
        indegree_item = [0 for _ in range(n)]
        graph_group = [set() for _ in range(m)]
        graph_item = [set() for _ in range(n)]
        group_data = [set() for _ in range(m)]
        # 存放组与项目的关系
        for i in range(n):
            group_data[group[i]].add(i)

        work_group = [i for i in range(m) if len(group_data[i]) > 0]

        for i in range(n):
            for j in beforeItems[i]:
                if group[i] == group[j]:
                    # 属于组内图
                    indegree_item[i] += 1
                    graph_item[j].add(i)
                else:
                    # 属于组间图
                    if not group[i] in graph_group[group[j]]:
                        indegree_group[group[i]] += 1
                        graph_group[group[j]].add(group[i])
        q = [i for i in range(m) if indegree_group[i] == 0]
        if len(q) == 0: return []
        seq = []
        while q:
            p = q.pop()
            seq.append(p)
            for i in graph_group[p]:
                indegree_group[i] -= 1
                if indegree_group[i] == 0:
                    q.insert(0, i)
        if len(seq) < len(indegree_group): return []
        for k in work_group:
            q = [i for i in group_data[k] if indegree_item[i] == 0]
            if len(q) == 0: return []
            _seq = []
            while q:
                p = q.pop()
                _seq.append(p)
                for i in graph_item[p]:
                    indegree_item[i] -= 1
                    if indegree_item[i] == 0:
                        q.insert(0, i)
            if len(_seq) < len(group_data[k]): return []
            group_data[k] = _seq
        res = []
        for i in range(m):
            res += group_data[seq[i]]
        return res


if __name__ == '__main__':
    a = Solution()
    a.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]])
    a.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]])
