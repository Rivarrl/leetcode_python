# -*- coding: utf-8 -*-
# ======================================
# @File    : test.py
# @Time    : 2019/11/1 0:38
# @Author  : Rivarrl
# ======================================
from typing import List


def sortItems(n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
    groupId = m
    for i in range(len(group)):
        if group[i] == -1:
            group[i] = groupId
            groupId += 1

    indegreeG = [0 for _ in range(groupId)]
    indegreeI = [0 for _ in range(n)]
    vectorG = [set() for _ in range(groupId)]
    graphG = [set() for _ in range(groupId)]
    graphI = [set() for _ in range(n)]

    for i in range(len(group)):
        vectorG[group[i]].add(i)

    for i in range(len(beforeItems)):
        for item in beforeItems[i]:
            if group[i] == group[item]:
                indegreeI[i] += 1
                graphI[item].add(i)
            else:
                if group[i] not in graphG[group[item]]:
                    indegreeG[group[i]] += 1
                    graphG[group[item]].add(group[i])

    # group top sort
    qu = []
    orderG = []
    for i in range(groupId):
        if indegreeG[i] == 0:
            qu.append(i)
    if len(qu) == 0:
        return []
    while len(qu) > 0:
        t = []
        while len(qu) > 0:
            curr = qu.pop()
            print(curr)
            orderG.append(curr)

            for neg in graphG[curr]:
                indegreeG[neg] -= 1
                if indegreeG[neg] == 0:
                    t.append(neg)
        qu = t

    if len(orderG) != groupId:
        return []

    print("======")
    # items top sort
    res = []
    for i in range(len(orderG)):

        qu = []
        for item in vectorG[orderG[i]]:
            if indegreeI[item] == 0:
                qu.append(item)

        count = 0
        while len(qu) > 0:
            t = []
            while len(qu) > 0:
                curr = qu.pop()
                res.append(curr)
                count += 1

                for neg in graphI[curr]:
                    indegreeI[neg] -= 1
                    if indegreeI[neg] == 0:
                        t.append(neg)
            qu = t

        if count != len(vectorG[orderG[i]]):
            return []

    return res

if __name__ == '__main__':
    res = sortItems(5, 3, [0,0,2,1,0], [[3],[],[],[],[1,3,2]])
    print(res)