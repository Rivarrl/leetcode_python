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


def reverseParentheses(s):
    """
    1190. 反转每对括号间的子串
    给出一个字符串 s（仅含有小写英文字母和括号）。
    请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
    注意，您的结果中 不应 包含任何括号。
    示例 1：
    输入：s = "(abcd)"
    输出："dcba"
    示例 2：
    输入：s = "(u(love)i)"
    输出："iloveu"
    示例 3：
    输入：s = "(ed(et(oc))el)"
    输出："leetcode"
    示例 4：
    输入：s = "a(bcdefghijkl(mno)p)q"
    输出："apmnolkjihgfedcbq"
    提示：
    0 <= s.length <= 2000
    s 中只有小写英文字母和括号
    我们确保所有括号都是成对出现的
    :param s: str
    :return: str
    """
    n = len(s)
    stk = []
    i = 0
    while i < n:
        if s[i] == '(':
            stk.append(i)
        elif s[i] == ')':
            j = stk.pop()
            s = s[:j] + s[j+1:i][::-1] + s[i+1:]
            i -= 2
            n -= 2
        i += 1
    return s


def kConcatenationMaxSum(arr, k):
    """
    1191. K 次串联后最大子数组之和
    给你一个整数数组 arr 和一个整数 k。
    首先，我们要对该数组进行修改，即把原数组 arr 重复 k 次。
    举个例子，如果 arr = [1, 2] 且 k = 3，那么修改后的数组就是 [1, 2, 1, 2, 1, 2]。
    然后，请你返回修改后的数组中的最大的子数组之和。
    注意，子数组长度可以是 0，在这种情况下它的总和也是 0。
    由于 结果可能会很大，所以需要 模（mod） 10^9 + 7 后再返回。 
    示例 1：
    输入：arr = [1,2], k = 3
    输出：9
    示例 2：
    输入：arr = [1,-2,1], k = 5
    输出：2
    示例 3：
    输入：arr = [-1,-2], k = 7
    输出：0
    提示：
    1 <= arr.length <= 10^5
    1 <= k <= 10^5
    -10^4 <= arr[i] <= 10^4
    :param arr: List[int]
    :param k: int
    :return: int
    """
    mod = 10 ** 9 + 7
    s, maxs = 0, 0
    for a in arr * min(2, k):
        s = a if s < 0 else s + a  # 连续和
        if s > maxs:
            maxs = s  # 最大连续和
    if k <= 2:
        return maxs  # 两个周期以内之间返回最大连续和
    return (max(sum(arr), 0) * (k - 2) + maxs) % mod


def sortArray(nums):
    """
    912. 排序数组
    给定一个整数数组 nums，将该数组升序排列。
    示例 1：
    输入：[5,2,3,1]
    输出：[1,2,3,5]
    示例 2：
    输入：[5,1,1,2,0,0]
    输出：[0,0,1,1,2,5]
    提示：
    1 <= A.length <= 10000
    -50000 <= A[i] <= 50000
    :param nums: List[int]
    :return: List[int]
    """
    def sort(l, r, arr):
        if l >= r: return
        base = arr[l]
        i, j = l, r - 1
        while i < j:
            while i <= j and arr[i] <= base:
                i += 1
            while i <= j and arr[j] >= base:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[i] = arr[i], arr[l]
        sort(l, i, arr)
        sort(i+1, r, arr)
    sort(0, len(nums), nums)
    return nums


if __name__ == '__main__':
    # arr = [10,2]
    # res = largerstNumber(arr)
    s = "(ed(et(oc))el)"
    reverseParentheses(s)
    pass