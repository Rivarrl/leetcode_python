# -*- coding:utf-8 -*-

# 冒泡排序

class BubbleSort:

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(len(self.arr)):
            for j in range(i+1, len(self.arr)):
                if self.arr[i] > self.arr[j]:
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        return self.arr

if __name__ == '__main__':
    x = [24,53,12,34,55,9,3,-1,56,34,32,65]
    bs = BubbleSort(x)
    print("BEFORE:", x)
    bs.sort()
    print("AFTER :", x)