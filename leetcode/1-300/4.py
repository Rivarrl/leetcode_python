# -*- coding: utf-8 -*-
# ======================================
# @File    : 5278.py
# @Time    : 2019/11/9 17:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        [4. 寻找两个有序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)
        思路1：由于题目要求O(log(m+n))时间复杂度，需要二分查找。
        将两个数组想象成拼接到一起，每个数组相对有序，分为左右对等的两部分，如果为奇数，左比右多1个。
        最终的中位数与两个数组的左半部分的最大值和右半部分的最小值有关，如果两数组长度和为奇数，就是左半部分最大值，否则就是左最大加右最小/2。
        元素总数偶数时：i + j = n - i + m - j
        元素总数奇数时：i + j = n - i + m - j + 1
        所以有 j = (m + n + 1) // 2 - i
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        if m == 0:
            return nums2[(n - 1) // 2] / 1.0 if n & 1 else (nums2[(n - 1) // 2] + nums2[(n - 1) // 2 + 1]) / 2.0
        t = (m + n + 1) // 2
        begin, end = 0, m
        while begin <= end:
            i = (begin + end) // 2
            j = t - i
            if i > 0 and j < n and nums1[i - 1] > nums2[j]:
                end = i - 1
            elif j > 0 and i < m and nums2[j - 1] > nums1[i]:
                begin = i + 1
            else:
                if i == 0:
                    left = nums2[j - 1]
                elif j == 0:
                    left = nums1[i - 1]
                else:
                    left = max(nums1[i - 1], nums2[j - 1])
                if i == m:
                    right = nums2[j]
                elif j == n:
                    right = nums1[i]
                else:
                    right = min(nums1[i], nums2[j])
                return left / 1.0 if (m + n) & 1 else (left + right) / 2.0
        return 0.0

    def getKth(self, nums1, st1, ed1, nums2, st2, ed2, k):
        l1, l2 = ed1 - st1 + 1, ed2 - st2 + 1
        if l1 > l2: return self.getKth(nums2, st2, ed2, nums1, st1, ed1, k)
        if l1 == 0: return nums2[st2 + k - 1]
        if k == 1: return min(nums1[st1], nums2[st2])
        i, j = st1 + min(l1, k // 2) - 1, st2 + min(l2, k // 2) - 1
        if nums1[i] > nums2[j]:
            return self.getKth(nums1, st1, ed1, nums2, j+1, ed2, k - (j - st2 + 1))
        else:
            return self.getKth(nums1, i+1, ed1, nums2, st2, ed2, k - (i - st1 + 1))

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        left, right = (n + m + 1) // 2, (n + m + 2) // 2
        return (self.getKth(nums1, 0, n - 1, nums2, 0, m - 1, left) + self.getKth(nums1, 0, n - 1, nums2, 0, m - 1, right)) / 2.0


if __name__ == '__main__':
    sol = Solution()
    res = sol.findMedianSortedArrays2([1,3], [2])
    print(res)