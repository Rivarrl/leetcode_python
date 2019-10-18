#coding=utf-8
# 依图科技秋招算法

import sys
import heapq

def q4(arr, n, m, k):
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dp = []
    for j in range(m):
        dp.append((arr[0][j], letter[j]))
    if n == 1:
        res = sorted(dp, key=lambda x:(x[0], -sum([ord(e) for e in x[1]])), reverse=True)[:k]
    else:
        i = 1
        while i < n:
            ndp = []
            for score, s in sorted(dp, key=lambda x:(x[0], -sum([ord(e) for e in x[1]])), reverse=True)[:k]:
                for j in range(m):
                    ndp.append((score+arr[i][j], s+letter[j]))
            dp = ndp
            i += 1
        res = sorted(dp, key=lambda x:(x[0], -sum([ord(e) for e in x[1]])), reverse=True)[:k]
    return '\n'.join([e[1] for e in res])


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip().split()
    n = int(line1[0])
    m = int(line1[1])
    k = int(line1[2])
    arr = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        arr.append([int(e) for e in line.split(' ')])
    res = q4(arr, n, m, k)
    print(res)