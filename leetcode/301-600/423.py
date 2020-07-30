# -*- coding: utf-8 -*-
# ======================================
# @File    : 423.py
# @Time    : 2020/7/30 11:10 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [423. 从英文中重建数字](https://leetcode-cn.com/problems/reconstruct-original-digits-from-english/)
    """
    @timeit
    def originalDigits(self, s: str) -> str:
        # 0-9的英文分3级，每级的特殊字符可以一一对应一个数字，按1-3级的顺序找
        lv1 = {'z':0, 'w':2, 'u':4, 'x':6, 'g':8}
        lv2 = {'o':1, 't':3, 'f':5,'s':7}
        lv3 = {'i':9}
        arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        d = [0] * 26
        a = ord('a')
        for c in s:
            d[ord(c)-a] += 1
        res = []
        for lvx in (lv1, lv2, lv3):
            for k, v in lvx.items():
                x = d[ord(k)-a]
                for c in arr[v]:
                    d[ord(c)-a] -= x
                res += [v] * x
        return ''.join([str(x) for x in sorted(res)])

    @timeit
    def originalDigits2(self, s: str) -> str:
        # 优化，思路一样，直接用count
        f = [0] * 10
        f[0] = s.count('z')
        f[2] = s.count('w')
        f[4] = s.count('u')
        f[6] = s.count('x')
        f[8] = s.count('g')
        f[1] = s.count('o') - f[0] - f[2] - f[4]
        f[3] = s.count('h') - f[8]
        f[5] = s.count('f') - f[4]
        f[7] = s.count('s') - f[6]
        f[9] = s.count('i') - f[5] - f[6] - f[8]
        res = ''
        for i in range(10):
            if f[i] > 0: res += str(i) * f[i]
        return res

if __name__ == '__main__':
    a = Solution()
    a.originalDigits2("owoztneoer")
    a.originalDigits2("fviefuro")
    a.originalDigits2("egith")