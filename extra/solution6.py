#coding=utf-8
# 依图科技秋招算法

import sys
from typing import List


def q3(arr: List[List], t: int, n: int) -> int:
    arr.sort(key=lambda x:(x[-1], max(x[0], x[1])), reverse=True)
    i = 0
    while t > 0 and i < n:
        tmp = t - arr[i][-1]
        if tmp < 0: break
        t = tmp
        i += 1
    ans = 0
    for j in range(i):
        ans += min(arr[j][:2]) + max(arr[j][:2]) * t
        t += arr[j][2]
    return ans


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip().split()
    n = int(line1[0])
    t = int(line1[1])
    arr = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        arr.append([int(e) for e in line.split(' ')])
    res = q3(arr, t, n)
    print(res)