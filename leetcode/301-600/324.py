# -*- coding: utf-8 -*-
# ======================================
# @File    : 324.py
# @Time    : 2019/12/19 1:19
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [324. 摆动排序 II](https://leetcode-cn.com/problems/wiggle-sort-ii/)
    """
    def wiggleSort(self, nums: List[int]) -> None:
        """
        nlogn，先排序再按位置分配，分配的时候注意先小后大，如果按序分配，假如是123334，就变成了132334，而答案应该是341323，观察可得倒序分配可避免此问题.
        """
        nums.sort()
        n = len(nums[::2])
        nums[::2], nums[1::2] = nums[:n][::-1], nums[n:][::-1]

    def wiggleSort2(self, nums: List[int]) -> None:
        """
        类似荷兰三色旗的方法，先找中位数，按中位数上下浮动去找中位数附近点分别放在2i和2i+1位置
        """
        import sys
        sys.setrecursionlimit(3000)
        # O(n)找中位数
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        def kth(arr, lo, hi, k):
            if lo >= hi: return arr[lo]
            base = arr[lo]
            i, j = lo, hi
            while i < j:
                while i < j and arr[j] >= base:
                    j -= 1
                while i < j and arr[i] <= base:
                    i += 1
                if i < j: swap(arr, i, j)
            swap(arr, j, lo)
            if j == k: return arr[j]
            elif j > k: return kth(arr, lo, j-1, k)
            else: return kth(arr, j+1, hi, k)
        def shuffle(arr):
            import random
            for i in range(1, n):
                j = random.randint(0, i)
                if j < i: swap(arr, i, j)
        # O(n)荷兰三色旗算法
        n = len(nums)
        # 打乱顺序，防止恶意卡快排的测试用例
        shuffle(nums)
        mid = kth(nums, 0, n - 1, n // 2)
        f = lambda i: (2 * i + 1) % (n | 1)
        i = j = 0
        k = n - 1
        while j <= k:
            if nums[f(j)] > mid:
                swap(nums, f(i), f(j))
                i += 1
                j += 1
            elif nums[f(j)] < mid:
                swap(nums, f(j), f(k))
                k -= 1
            else:
                j += 1

if __name__ == "__main__":
    a = Solution()
    # a.wiggleSort2([1, 5, 1, 1, 6, 4])
    # a.wiggleSort2([1, 3, 2, 2, 3, 1])
    # a.wiggleSort2([1, 3, 4, 2, 3, 3])
    a.wiggleSort2([2,3,3,2,2,2,1,1])
