# -*- coding: utf-8 -*-
# ======================================
# @File    : t3.py
# @Time    : 2020/5/7 20:12
# @Author  : Rivarrl
# ======================================
x = input().strip()
res = ''
for i in range(0, len(x), 2):
    a = int(x[i])
    b = x[i+1]
    res += b * a
print(res)