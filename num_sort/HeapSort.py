# -*- coding:utf-8 -*-

# 堆排序

class HeapSort:

    def __init__(self, arr):
        self.arr = arr

    def sort(self):


if __name__ == '__main__':
    x = [4,3,5,1,2,0,6,-1,9]
    hs = HeapSort(x)
    print("BEFORE:", x)
    hs.sort()
    print("AFTER :", x)