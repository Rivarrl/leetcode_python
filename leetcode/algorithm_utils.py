# -*- coding:utf-8 -*-
# 算法辅助类
import time
from typing import List
null = None

class Trie:
    def __init__(self, x):
        self.val = x
        self.children = [None] * 26

class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

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

class NextNode:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class NeighborNode:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class QuadNode:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class RandomNode:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Bucket:
    def __init__(self,m=0,M=0,isempty=True):
        self.m = m
        self.M = M
        self.isempty = isempty

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


def print_list_node(head, cnt=20):
    while head.next and cnt > 0:
        print(head.val, end='->')
        head = head.next
        cnt -= 1
    print(head.val)


def construct_list_node(arr):
    res = ListNode(None)
    p = res
    for x in arr:
        p.next = ListNode(x)
        p = p.next
    return res.next


def binary_fills(i):
    if i == 0: return 0
    x = 1
    while x <= i:
        x <<= 1
    return x - i - 1


def split_tree_list(arr):
    depth = pow((len(arr) + 1), 2)
    arrl, arrr = [], []
    for i in range(1, depth):
        l = 2 ** i
        r = l * 2 - 1
        m = (l + r) // 2
        arrl += arr[l - 1 : m]
        arrr += arr[m: r]
    return arrl, arrr

def construct_tree_node(arr):
    arr += [None] * binary_fills(len(arr))
    if len(arr) == 0 or arr[0] == None: return None
    root = TreeNode(arr[0])
    arrl, arrr = split_tree_list(arr)
    left = construct_tree_node(arrl)
    right = construct_tree_node(arrr)
    root.left = left
    root.right = right
    return root

# deprecated
def construct_tree_node_v2(arr):
    if not arr: return
    def _construct(i):
        if i >= len(arr):
            return None
        root = TreeNode(arr[i])
        root.left = _construct(i*2+1)
        root.right = _construct(i*2+2)
        return root
    return _construct(0)


def print_tree_node(root):
    def inner(root):
        res = None
        if root:
            res = []
            res.append(root.val)
            left, right = inner(root.left), inner(root.right)
            if left or right:
                res += [left, right]
        return res
    res = inner(root)
    print(res)


def deconstruct_tree_node(root):
    res = []
    if root:
        res.extend([root.val])
        stk = [root]
        while stk:
            cur = []
            for each in stk:
                if each:
                    cur.append(each.right)
                    cur.append(each.left)
            if cur != []:
                res.extend([None if not x else x.val for x in cur][::-1])
            stk = [x for x in cur]
    return res


def matrix_pretty_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
    print()

def build_max_heap(arr):
    for i in range(len(arr)//2, -1, -1):
        heapify(arr, i)

def heapify(arr, i):
    left = 2 * i + 1
    right = left + 1
    root = i
    if left < arr_size and arr[left] > arr[root]:
        root = left
    if right < arr_size and arr[right] > arr[root]:
        root = right
    if root != i:
        swap(arr, i, root)
        heapify(arr, root)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heap_sort(arr):
    global arr_size
    arr_size = len(arr)
    build_max_heap(arr)
    for i in range(len(arr)-1, 0, -1):
        swap(arr, 0, i)
        arr_size -= 1
        heapify(arr, 0)


def timeit(f):
    def inner(*args, **kwargs):
        t1 = time.time()
        x = f(*args, **kwargs)
        t2 = time.time()
        print("{0} runs: {1:.4f} sec".format(f.__name__, t2 - t1))
        print(x)
        return x
    return inner


if __name__ == '__main__':
    # x = [4,1,6,3,5,2]
    # heap_sort(x)
    # print(x)
    # matrix_pretty_print([[1,2,3],[4,5,6]])
    # a = [5,4,2,3,6,1,7,9]
    # quick_sort(a, 0, len(a) - 1)
    # print(a)
    # a = construct_list_node([1,2,3,4,5,6])
    # print_list_node(a)
    # b = construct_tree_node([8,12,2,None,None,6,4,None,None,None,None])
    # print_tree_node(b)
    # c = deconstruct_tree_node(b)
    # print(c)
    pass
