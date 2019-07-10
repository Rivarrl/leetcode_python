# -*- coding:utf-8 -*-

# 归并排序

class MergeSort:

    def __init__(self, arr):
        self.arr = arr
        self.aux = [x for x in self.arr]

    def merge(self, lo, mid, hi):
        i, j = lo, mid+1
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

    def sort_bottom_up(self):
        N = len(self.arr)
        sz = 1
        for sz in range(1, N, sz):
            for lo in range(0, N-sz, sz+sz):
                self.merge(lo, lo+sz-1, min(lo+sz+sz-1, N-1))

    def sort_helper(self, lo, hi):
        if hi <= lo: return
        mid = lo + (hi - lo) // 2
        self.sort_helper(lo, mid)
        self.sort_helper(mid+1, hi)
        self.merge(lo, mid, hi)

if __name__ == '__main__':
    x = [24,53,12,34,55,9,3,-1,56,34,32,65]
    ms = MergeSort(x)
    print("BEFORE:", x)
    ms.sort_bottom_up()
    print("AFTER :", x)