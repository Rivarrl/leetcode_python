# -*- coding: utf-8 -*-
# ======================================
# @File    : t4.py
# @Time    : 2020/5/22 19:28
# @Author  : Rivarrl
# ======================================


"""
3
2,5,6,7,9,5,7
1,7,4,3,4

2,5,6,1,7,4,7,9,5,3,4,7

4
2,5,6,7,9,5,7
1,7,4,3,4

2,5,6,7,1,7,4,3,9,5,7,4
"""

def f(arr, k):
    n = len(arr)
    l = [0] * n
    tot = m = 0
    for i, e in enumerate(arr):
        l[i] = len(e)
        tot += l[i]
        m = max(m, l[i])
    p = q = 0
    res = [0] * tot
    while p < m:
        for i in range(n):
            for x in range(k):
                j = p + x
                if j >= l[i]: continue
                res[q] = arr[i][j]
                q += 1
        p += k
    return ','.join([str(e) for e in res])

if __name__ == '__main__':
    k = int(input())
    arr = []
    line = input()
    while line:
        arr.append(list(map(int, line.strip().split(','))))
        line = input()
    res = f(arr, k)
    print(res)