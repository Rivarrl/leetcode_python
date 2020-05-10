# -*- coding: utf-8 -*-
# ======================================
# @File    : t5.py
# @Time    : 2020/5/10 20:59
# @Author  : Rivarrl
# ======================================

def f(s, k):
    n = len(s)
    c = s.count('T')
    if c <= k: return n - ((k - c) & 1)
    t = c - k
    if t & 1:
        l, r = s.find('T'), s.rfind('T')
        return max(f(s[l+1:], k) - l, f(s[:r], k) - (n-1-r))
    res = ctr = i = j = 0
    rs = n = len(s)
    st, ed = 0, rs - 1
    while i < n:
        if s[i] == 'T':
            ctr += 1
        while ctr == t and s[j] != 'T':
            j += 1
        if ctr == t and i - j + 1 < rs:
            rs = i - j + 1
            st, ed = j, i
            j += 1
            ctr -= 1
        i += 1
    step = 1
    for i, x in enumerate(s):
        if x == 'T' and st <= i <= ed:
            step *= -1
        else:
            res += step
    return abs(res)

if __name__ == '__main__':
    s = input()
    k = int(input())
    res = f(s, k)
    print(res)

"""
FFTFTFTTTFFTFFTTFFFF
3
9
"""