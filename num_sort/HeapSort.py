# -*- coding:utf-8 -*-

# 堆排序

class HeapSort:

    def __init__(self, arr):
        self.arr = arr

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def build_max_heap(self):
        for i in range(len(self.arr)//2, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        left = i * 2 + 1
        right = left + 1
        root = i
        if left < self.N and self.arr[left] > self.arr[root]:
            root = left
        if right < self.N and self.arr[right] > self.arr[root]:
            root = right
        if root != i:
            self.swap(i, root)
            self.heapify(root)

    def sort(self):
        self.N = len(self.arr)
        self.build_max_heap()
        for i in range(len(self.arr) - 1, 0, -1):
            self.swap(0, i)
            self.N -= 1
            self.heapify(0)


if __name__ == '__main__':
    x = [4,3,5,1,2,0,6,-1,9]
    hs = HeapSort(x)
    print("BEFORE:", x)
    hs.sort()
    print("AFTER :", x)