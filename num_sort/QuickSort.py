# -*- coding:utf-8 -*-

# 快速排序


class QuickSort:

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self.sort_helper(0, len(self.arr)-1)

    def sort_helper(self, l, r):
        if l >= r: return
        i, j = l, r
        base = self.arr[l]
        while i < j:
            while i < j and self.arr[j] >= base:
                j -= 1
            while i < j and self.arr[i] <= base:
                i += 1
            self.swap(self.arr, i, j)
        self.swap(self.arr, l , j)
        self.sort_helper(l, j)
        self.sort_helper(j+1, r)

    @staticmethod
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

if __name__ == '__main__':
    x = [4,3,5,1,2,0,6,-1,9]
    qs = QuickSort(x)
    print("BEFORE:", x)
    qs.sort()
    print("AFTER :", x)
