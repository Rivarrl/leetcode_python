# -*- coding:utf-8 -*-

# 桶排序

class BucketSort:
    """
    建立max(arr)-min(arr)+1个桶。
    暂时不能排序小数，可以排序负数
    """
    def __init__(self, arr):
        self.arr = arr
        self.m = min(arr)
        self.M = max(arr)
        self.bucket = [0] * (self.M - self.m + 1)

    def sort(self):
        for i in self.arr:
            self.bucket[i - self.m] += 1
        k = 0
        for i, x in enumerate(self.bucket):
            for j in range(x):
                self.arr[k] = i + self.m
                k += 1
        return self.arr


if __name__ == '__main__':
    x = [24,53,12,34,55,9,3,-1,56,34,32,65]
    bks = BucketSort(x)
    print("BEFORE:", x)
    bks.sort()
    print("AFTER :", x)