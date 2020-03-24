# -*- coding: utf-8 -*-
# ======================================
# @File    : m21.py
# @Time    : 2020/3/24 17:19
# @Author  : Rivarrl
# ======================================
# 美团二面第一题
"""
给定一个可能含有重复值的数组 arr，找到每一个 i 位置左边和右边离 i 位置最近且值比 arr[i] 小的位置。返回所有位置相应的信息。
输入描述
第一行输入一个数字 n，表示数组 arr 的长度。
以下一行输入 n 个数字，表示数组的值
输出描述
输出n行，每行两个数字 L 和 R，如果不存在，则值为 -1，下标从 0 开始。
示例1
输入
7
3 4 1 5 6 2 7
输出
-1 2
0 2
-1 -1
2 5
3 5
2 -1
5 -1
"""
import sys
n = int(input().strip())
arr = list(map(int, input().strip().split()))
stk = []
res = [[-1, -1] for _ in range(n)]
for i in range(n):
    while stk and arr[stk[-1]] > arr[i]:
        j = stk.pop()
        res[j][1] = i
    if stk:
        res[i][0] = stk[-1]
    stk.append(i)
for i, j in res:
    print(i, j)