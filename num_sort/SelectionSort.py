# -*- coding:utf-8 -*-

# 选择排序

class SelectionSort:

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(len(self.arr)):
            # m记录当前最小值索引
            m = i
            for j in range(i+1, len(self.arr)):
                if self.arr[j] < self.arr[m]:
                    m = j
            self.arr[i], self.arr[m] = self.arr[m], self.arr[i]
        return self.arr

if __name__ == '__main__':
    x = [24,53,12,34,55,9,3,-1,56,34,32,65]
    ss = SelectionSort(x)
    print("BEFORE:", x)
    ss.sort()
    print("AFTER :", x)