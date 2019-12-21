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
        _quick_sort(arr, l, j - 1)
        _quick_sort(arr, j + 1, r)
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


# 快排的另一种写法
def quick_sort2(arr):
    def _quick_sort(arr, l, r):
        if l >= r: return
        j, base = l - 1, arr[r]
        for i in range(l, r):
            if arr[i] < base:
                j += 1
                swap(arr, i, j)
        j += 1
        swap(arr, j, r)
        _quick_sort(arr, l, j-1)
        _quick_sort(arr, j+1, r)
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def quick_sort3(arr):
    def _quick_sort(arr, l, r):
        if l >= r: return
        pivot = arr[l]
        i, j = l, r
        while i < j:
            while i < j and arr[j] >= pivot: j -= 1
            arr[i] = arr[j]
            while i < j and arr[i] <= pivot: i += 1
            arr[j] = arr[i]
        arr[j] = pivot
        _quick_sort(arr, l, j-1)
        _quick_sort(arr, j+1, r)
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def get_min_max(arr):
    _MIN, _MAX = float("inf"), -float("inf")
    for x in arr:
        if x < _MIN:
            _MIN = x
        if x > _MAX:
            _MAX = x
    return _MIN, _MAX


# 计数排序
# 只能排整型数组
def count_sort(arr):
    _MIN, _MAX = get_min_max(arr)
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


# 桶排序
# 分配空间少的计数排序桶变为二维数组,每个桶存储多个元素.
# 计数排序也就是单桶大小为1时的桶排序
def bucket_sort(arr):
    _MIN, _MAX = get_min_max(arr)
    n = len(arr)
    k = (_MAX - _MIN) // 3 + 1
    tmp = [[] for _ in range(k)]
    for i in range(n):
        x = (arr[i] - _MIN) // 3
        tmp[x].append(arr[i])
        for j in range(len(tmp[x])-1, 0, -1):
            if tmp[x][j] < tmp[x][j-1]:
                swap(tmp[x], j, j-1)
            else:
                break
    i = 0
    for x in tmp:
        for e in x:
            arr[i] = e
            i += 1
    return arr


# 堆排序
# 每次要将根节点与末尾交换, 所以正序排序建大顶堆, 逆序排序建小顶堆
def heap_sort(arr):
    def _build_max_heap(arr):
        for i in range(len(arr)//2, -1, -1):
            _heapify(arr, i)

    def _heapify(arr, i):
        l = i * 2 + 1
        r = l + 1
        p = i
        if l < N and arr[p] < arr[l]:
            p = l
        if r < N and arr[p] < arr[r]:
            p = r
        if p != i:
            swap(arr, i, p)
            _heapify(arr, p)

    N = len(arr)
    _build_max_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        swap(arr, 0, i)
        N -= 1
        _heapify(arr, 0)
    return arr

# 归并排序
# 1: 自顶向下  2:自底向上
def merge_sort(arr, type=1):
    def _merge(arr, l, mid, r):
        i, j = l, mid + 1
        for k in range(l, r + 1):
            tmp[k] = arr[k]
        for k in range(l, r + 1):
            if i > mid:
                arr[k] = tmp[j]
                j += 1
            elif j > r:
                arr[k] = tmp[i]
                i += 1
            elif tmp[j] < tmp[i]:
                arr[k] = tmp[j]
                j += 1
            else:
                arr[k] = tmp[i]
                i += 1
    # 自顶向下
    def _sort(arr, l, r):
        if l >= r: return
        mid = l + (r - l) // 2
        _sort(arr, l, mid)
        _sort(arr, mid + 1, r)
        _merge(arr, l, mid, r)
    # 自底向上
    def _sort_bottom_up(arr):
        n, step = len(arr), 1
        while step < n:
            l = 0
            while l < n:
                _merge(arr, l, l + step - 1, min(l + step + step - 1, n-1))
                l += step + step
            step += step
    n = len(arr)
    tmp = [0] * n
    if type == 1:
        _sort(arr, 0, n-1)
    else:
        _sort_bottom_up(arr)
    return arr


# 基数排序
# 基数排序适用于数组中的数值不大的非负整数情况, 原理是按数值的每一位排序装桶
# 可以分为低位优先(LSD)和高位优先(MSD)
# 代码中使用的LSD
def radix_sort(arr):
    get_digit = lambda x, d: (x//d) % 10
    max_num = max(arr)
    _MAX_DIGIT = 1
    while max_num >= 10:
        max_num //= 10
        _MAX_DIGIT += 1
    n = len(arr)
    digit = 1
    for i in range(_MAX_DIGIT):
        pos = [0] * 10
        tmp = [x for x in arr]
        for x in tmp:
            k = get_digit(x, digit)
            pos[k] += 1
        for j in range(1, 10):
            pos[j] += pos[j-1]
        for i in range(n-1, -1, -1):
            base = tmp[i]
            k = get_digit(base, digit)
            arr[pos[k] - 1] = base
            pos[k] -= 1
        digit *= 10
    return arr


if __name__ == '__main__':
    x = [15, 6, 41, 24, 37, 96, 421]
    quick_sort(x)
    print(x)
