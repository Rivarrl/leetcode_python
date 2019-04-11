# -*- coding:utf-8 -*-
# 算法辅助类

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