# -*- coding: utf-8 -*-
# ======================================
# @File    : solution3.py
# @Time    : 2019/10/16 15:45
# @Author  : Rivarrl
# ======================================
import sys

# 美团点评算法岗1

class MSDSort:
    R = 256

    def sort(self, a):
        N = len(a)
        self.aux = [str()] * N
        self.helper(a, 0, N-1, 0)

    @staticmethod
    def char_at(s, d):
        return -1 if len(s) == d else 256 - ord(s[d])

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

def q1(words):
    msd = MSDSort()
    msd.sort(words)
    return ','.join(words)

if __name__ == '__main__':
    line1 = sys.stdin.readline().strip()
    words = line1.split(',')
    a = q1(words)
    print(a)