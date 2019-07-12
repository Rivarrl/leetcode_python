# -*- coding:utf-8 -*-

# 归并排序

class MergeSort:

    aux = []
    def __init__(self, arr):
        self.arr = arr

    def merge(self, lo, mid, hi):
        i, j = lo, mid + 1
        self.aux = self.arr[:]
        for k in range(lo, hi + 1):
            if i > mid:
                self.arr[k] = self.aux[j]
                j += 1
            elif j > hi:
                self.arr[k] = self.aux[i]
                i += 1
            elif self.aux[j] < self.aux[i]:
                self.arr[k] = self.aux[j]
                j += 1
            else:
                self.arr[k] = self.aux[i]
                i += 1

    def sort(self):
        self.sort_helper(0, len(self.arr) - 1)

    def sort_helper(self, lo, hi):
        if hi <= lo: return
        mid = lo + (hi - lo) // 2
        self.sort_helper(lo, mid)
        self.sort_helper(mid+1, hi)
        self.merge(lo, mid, hi)

    def sort_bottom_up(self):
        N = len(self.arr)
        sz = 1
        while sz < N:
            lo = 0
            while lo < N - sz:
                self.merge(lo, lo+sz-1, min(lo+sz+sz-1, N-1))
                lo += sz + sz
            sz += sz

if __name__ == '__main__':
    x = [4,3,5,1,2,0,6,-1,9]
    ms = MergeSort(x)
    print("BEFORE:", x)
    ms.sort()
    print("AFTER :", x)