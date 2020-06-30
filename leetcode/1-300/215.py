# -*- coding: utf-8 -*-
# ======================================
# @File    : 215.py
# @Time    : 2019/12/21 12:07
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)
    """
    @timeit
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 使用快排partition，第k大，就是倒序快排的第k个索引位置
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        def kth(arr, lo, hi, k):
            if lo >= hi: return arr[lo]
            j, base = lo - 1, arr[hi]
            for i in range(lo, hi):
                if arr[i] > base:
                    j += 1
                    swap(arr, i, j)
            j += 1
            swap(arr, j, hi)
            if j == k: return arr[j]
            elif j < k: return kth(arr, j+1, hi, k)
            else: return kth(arr, lo, j-1, k)
        return kth(nums, 0, len(nums) - 1, k - 1)


    @timeit
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        # 维护堆
        # 大顶堆就是建好堆之后删除k-1个堆顶元素
        # 小顶堆就是维护一个大小为k的小顶堆，遍历过后堆顶即为所求
        # 这里用小顶堆
        def sift_down(arr, i):
            j = i
            left, right = j * 2 + 1, j * 2 + 2
            if left < len(arr) and arr[j] > arr[left]:
                j = left
            if right < len(arr) and arr[j] > arr[right]:
                j = right
            if j != i:
                arr[i], arr[j] = arr[j], arr[i]
                sift_down(arr, j)
        mheap = [-0x3f3f3f3f] * k
        for x in nums:
            if x > mheap[0]:
                mheap[0] = x
                sift_down(mheap, 0)
        return mheap[0]

if __name__ == '__main__':
    a = Solution()
    a.findKthLargest2([3,2,1,5,6,4], 2)
    a.findKthLargest2([3,2,3,1,2,4,5,5,6], 4)