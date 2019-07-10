# -*- coding:utf-8 -*-

# 插入排序

class InsertionSort:
    """
    直观的插入排序：sort_v1
    还原整理扑克牌的操作，先把当前值拿出，然后将前面比当前值大的值依次右移一位最后在停止位放入当前值，一趟结束
    算法书中的插入排序：sort
    当前一趟插入操作前面的值已经是有序的，只要判断前面比当前值大就不断进行交换
    """

    def __init__(self, arr):
        self.arr = arr

    def sort_v1(self):
        for i in range(1, len(self.arr)):
            cur = self.arr[i]
            j = i
            while j > 0 and cur < self.arr[j-1]:
                self.arr[j] = self.arr[j - 1]
                j -= 1
            self.arr[j] = cur
        return self.arr

    def sort(self):
        for i in range(1, len(self.arr)):
            j = i
            while j > 0 and self.arr[j] < self.arr[j-1]:
                self.arr[j], self.arr[j-1] = self.arr[j-1], self.arr[j]
                j -= 1
        return self.arr


if __name__ == '__main__':
    x = [24,53,12,34,55,9,3,-1,56,34,32,65]
    iss = InsertionSort(x)
    print("BEFORE:", x)
    iss.sort()
    print("AFTER :", x)

