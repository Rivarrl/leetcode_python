# -*- coding:utf-8 -*-
# 算法辅助类

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


def print_list_node(head):
    while head.next:
        print(head.val, end='->')
        head = head.next
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


def matrix_pretty_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()

if __name__ == '__main__':
    pass
    matrix_pretty_print([[1,2,3],[4,5,6]])
    # a = [12, 4, 7, 2]
    # quick_sort(a, 0, 3)
    # print(a)
    # a = construct_list_node([1,2,3,4,5,6])
    # print_list_node(a)
    # b = construct_tree_node([1,2,3,4,5,None,6])
    # print_tree_node(b)
