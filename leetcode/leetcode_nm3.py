# -*- coding: utf-8 -*-
# ======================================
# @File    : leetcode_nm3.py
# @Time    : 2019/10/3 22:54
# @Author  : Rivarrl
# ======================================

def findPeakElement(nums):
    """
    162. 寻找峰值
    峰值元素是指其值大于左右相邻值的元素。
    给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
    数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
    你可以假设 nums[-1] = nums[n] = -∞。
    示例 1:
    输入: nums = [1,2,3,1]
    输出: 2
    解释: 3 是峰值元素，你的函数应该返回其索引 2。
    示例 2:
    输入: nums = [1,2,1,3,5,6,4]
    输出: 1 或 5
    解释: 你的函数可以返回索引 1，其峰值元素为 2；
         或者返回索引 5， 其峰值元素为 6。
    说明:
    你的解法应该是 O(logN) 时间复杂度的。
    :param nums: List[int]
    :return: int
    """
    """
    # 暴力
    nums.insert(0, -float('inf'))
    nums.append(-float('inf'))
    n = len(nums)
    for i in range(1, n - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            return i - 1
    """
    # 二分查找
    l, r = 0, len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        if nums[m] > nums[m+1]:
            r = m
        else:
            l = m + 1
    return l


def largerstNumber(nums):
    """
    179. 最大数
    给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
    示例 1:
    输入: [10,2]
    输出: 210
    示例 2:
    输入: [3,30,34,5,9]
    输出: 9534330
    说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
    :param nums: List[int]
    :return: str
    """
    # 冒泡排序
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                nums[i], nums[j] = nums[j], nums[i]
    return str(int("".join([str(i) for i in nums])))


if __name__ == '__main__':
    arr = [10,2]
    res = largerstNumber(arr)
    pass