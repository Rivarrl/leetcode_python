# -*- coding: utf-8 -*-
# ======================================
# @File    : msd_sort.py
# @Time    : 2019/10/4 23:26
# @Author  : Rivarrl
# ======================================
from strings.utils import *

class MSDSort:
    R = 256

    def sort(self, a):
        N = len(a)
        self.aux = [str()] * N
        self.helper(a, 0, N-1, 0)

    @staticmethod
    def char_at(s, d):
        return -1 if len(s) == d else ord(s[d])

    def helper(self, a, lo, hi, d):
        if hi <= lo: return
        count = [0] * (self.R + 2)
        for i in range(lo, hi+1):
            count[self.char_at(a[i], d) + 2] += 1
        for r in range(self.R+1):
            count[r+1] += count[r]
        for i in range(lo, hi+1):
            c = self.char_at(a[i], d) + 1
            self.aux[count[c]] = a[i]
            count[c] += 1
        for i in range(lo, hi+1):
            a[i] = self.aux[i - lo]
        for r in range(self.R):
            self.helper(a, lo + count[r], lo + count[r+1] - 1, d+1)


if __name__ == '__main__':
    arr = ["yell", "mplr", "artificial", "ko", "mpr", "art", "trace", "arp", "gg", "disk", "mp", "mpq"]
    msd = MSDSort()
    msd.sort(arr)
    list_print(arr)
