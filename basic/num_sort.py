# -*- coding:utf-8 -*-
# 排序算法汇总

# 交换
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# 选择排序
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        k = i
        for j in range(i+1, n):
            if arr[j] < arr[k]:
                k = j
        swap(arr, i, k)
    return arr


# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                swap(arr, i, j)
    return arr


# 插入排序1
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j, base = i, arr[i]
        while j > 0 and base < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = base
    return arr

# 插入排序2
# 1的简化版
def insertion_sort2(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            swap(arr, j, j-1)
            j -= 1
    return arr


# 希尔排序
# 带步长的插入排序, 对比插入排序2
def shell_sort(arr):
    n = len(arr)
    h = 1
    while h < n//3: h = h * 3 + 1
    while h >= 1:
        for i in range(1, n):
            j = i
            while j >= h and arr[j] < arr[j-h]:
                swap(arr, j, j-h)
                j -= h
        h //= 3
    return arr


# 快速排序
def quick_sort(arr):
    def _quick_sort(arr, l, r):
        if l >= r: return
        i, j, base = l, r, arr[l]
        while i < j:
            while i < j and arr[j] >= base:
                j -= 1
            while i < j and arr[i] <= base:
                i += 1
            swap(arr, i, j)
        swap(arr, l, j)
        _quick_sort(arr, l, i)
        _quick_sort(arr, i+1, r)
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


# 计数排序
# 只能排整型数组
def count_sort(arr):
    _MIN, _MAX = float("inf"), -float("inf")
    for x in arr:
        if x < _MIN:
            _MIN = x
        if x > _MAX:
            _MAX = x
    tmp = [0] * (_MAX - _MIN + 1)
    n = len(arr)
    for i in range(n):
        tmp[arr[i] - _MIN] += 1
    i = 0
    for j, x in enumerate(tmp):
        for _ in range(x):
            arr[i] = j + _MIN
            i += 1
    return arr


if __name__ == '__main__':
    x = [5, 6, 2, 4, 7, 9, -1]
    count_sort(x)
    print(x)