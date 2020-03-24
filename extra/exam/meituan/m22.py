# -*- coding: utf-8 -*-
# ======================================
# @File    : m22.py
# @Time    : 2020/3/24 17:20
# @Author  : Rivarrl
# ======================================
# 美团二面第二题
"""
字符串距离计算
给定两个长度相等的，由小写字母组成的字符串S1和S2，定义S1和S2的距离为两个字符串有多少个位置上的字母不相等。
现在牛牛可以选定两个字母X1和X2，将S1中的所有字母X1均替换成X2。（X1和X2可以相同）
牛牛希望知道执行一次替换之后，两个字符串的距离最少为多少。
示例1
输入
"aaa","bbb"
输出
0
说明
牛牛可以将S1中的字符'a'全部替换成字符'b'，这样S1就变成了"bbb"，那么S1和S2的距离就是0
示例2
输入
"aabb","cdef"
输出
3
说明
一种可行的方案是将S1中的字符'a'全部替换成字符'c'，那么S1变成了"ccbb"，和S2的距离是3
"""

line = input().strip()
s1, s2 = [e.strip('"') for e in line.split(',')]
d1 = {}
d2 = {}
for c in s1:
    d1[c] = d1.get(c, 0) + 1
for c in s2:
    d2[c] = d2.get(c, 0) + 1
chx, chy = '', ''
mx, my = 0, 0
for i in range(26):
    c = chr(ord('a') + i)
    x1 = d1.get(c, 0) - d2.get(c,0)
    x2 = d2.get(c, 0) - d2.get(c,0)
    if x1 - x2 > mx:
        mx = x1 - x2
        chx = c
    if x2 - x1 > my:
        my = x2 - x1
        chy = c
dis = lambda s, t: sum([1 if s[i] != t[i] else 0 for i in range(len(s))])
print(dis(s1.replace(chx, chy), s2))