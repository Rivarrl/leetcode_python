# -*- coding:utf-8 -*-

# 希尔排序

class ShellSort:
    """
    设置步长，1，4，13，40.....
    其中步长为1时就是插入排序
    """

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        h = 1
        while h < n // 3: h = h * 3 + 1
        while h >= 1:
            for i in range(1, n):
                j = i
                while j >= h and self.arr[j] < self.arr[j-h]:
                    self.arr[j], self.arr[j-h] = self.arr[j-h], self.arr[j]
                    j -= h
            h //= 3
        return self.arr

if __name__ == '__main__':
    x = [24,53,12,34,55,9,3,-1,56,34,32,65]
    ss = ShellSort(x)
    print("BEFORE:", x)
    ss.sort()
    print("AFTER :", x)