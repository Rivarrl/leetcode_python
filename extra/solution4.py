# -*- coding: utf-8 -*-
# ======================================
# @File    : solution3.py
# @Time    : 2019/10/16 15:45
# @Author  : Rivarrl
# ======================================
import sys
import heapq

# def q2(n, arr1, arr2):
#     total = sum(arr1)
#     pq = []
#     for x, y in zip(arr1, arr2):
#         heapq.heappush(pq, (-y, x))
#     des = []
#     res = total
#     last = res
#     while total > 0:
#         e = heapq.heappop(pq)
#         des.append(-e[0])
#         last, res = res, res - e[1]
#         total -= des[-1]
#     e = heapq.heappop(pq)
#     while e[0] == -des[-1]:
#         res = min(res, last - e[1])
#         if not pq: break
#         e = heapq.heappop(pq)
#     return '{} {}'.format(len(des), res)

def q2(n, arr1, arr2):
    if n == 1: return '1 0'
    arr = []
    for x, y in zip(arr1, arr2):
        arr.append([x, y])
    arr.sort(key=lambda x:(x[1], x[0]), reverse=True)
    total = sum(arr1)
    res = total
    i = 0
    while total > 0:
        total -= arr[i][1]
        res -= arr[i][0]
        i += 1
    return '{} {}'.format(i, res)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    line1 = sys.stdin.readline().strip()
    line2 = sys.stdin.readline().strip()
    list1 = [int(e) for e in line1.split()]
    list2 = [int(e) for e in line2.split()]
    a = q2(n, list1, list2)
    print(a)