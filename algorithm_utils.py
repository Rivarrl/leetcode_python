# -*- coding:utf-8 -*-
# 算法辅助类

class Trie:
    def __init__(self, x):
        self.val = x
        self.children = [None] * 26

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

def binary_search(bs, b, e, x):
    """
    二分查找返回位置，查不到则返回大于x的第一个值的位置
    :param bs: 待查数组（非递减）
    :param b: 起始位置
    :param e: 结束位置
    :param x: 待查数字
    :return:
    """
    l, r = b, e
    while l <= r:
        mid = (l + r) // 2
        if bs[mid] == x:
            return mid
        elif bs[mid] < x:
            l = mid + 1
        elif bs[mid] > x:
            r = mid - 1
    return l

def quick_sort(arr, l, r):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    if l >= r:
        return
    i, j = l, r
    base = arr[l]
    while i < j:
        while arr[j] >= base and i < j:
            j -= 1
        while arr[i] <= base and i < j:
            i += 1
        swap(arr, i, j)
    swap(arr, l, j)
    quick_sort(arr, l, i-1)
    quick_sort(arr, i+1, r)

if __name__ == '__main__':
    a = [12, 4, 7, 2]
    quick_sort(a, 0, 3)
    print(a)