# -*- coding: utf-8 -*-
# ======================================
# @File    : 480.py
# @Time    : 2020/5/13 0:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [480. 滑动窗口中位数](https://leetcode-cn.com/problems/sliding-window-median/)
    """
    @timeit
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # 二分查找，维护有序数组
        import bisect
        n = len(nums)
        arr = []
        j = 0
        res = []
        for i in range(n):
            bisect.insort(arr, nums[i])
            if i >= k:
                arr.pop(bisect.bisect_left(arr, nums[j]))
                j += 1
            if i >= k - 1:
                res.append((arr[k//2] + arr[((k-1)//2)])/2)
        return res

    @timeit
    def medianSlidingWindow2(self, nums: List[int], k: int) -> List[float]:
        # 维护两个堆，前半部分最大堆，后半部分最小堆，需要用一个字典记录需要出堆的元素，在它影响结果的时候做出堆操作
        import heapq
        lo, hi = [], []
        for i in range(k):
            heapq.heappush(lo, nums[i])
        for j in range(k//2):
            heapq.heappush(hi, -heapq.heappop(lo))
        res = []
        d = {}
        for i in range(k, len(nums)+1):
            res.append(lo[0] if k & 1 else (lo[0]-hi[0])/2)
            if i == len(nums): break
            x, y = nums[i], nums[i-k]
            balance = -1 if y >= lo[0] else 1
            d[y] = d.get(y, 0) + 1
            if lo and x < lo[0]:
                balance -= 1
                heapq.heappush(hi, -x)
            else:
                balance += 1
                heapq.heappush(lo, x)
            if balance > 0:
                heapq.heappush(hi, -heapq.heappop(lo))
                balance -= 1
            if balance < 0:
                heapq.heappush(lo, -heapq.heappop(hi))
                balance += 1
            while d.get(lo[0], 0) > 0:
                d[lo[0]] -= 1
                heapq.heappop(lo)
            while hi and d.get(-hi[0], 0) > 0:
                d[-hi[0]] -= 1
                heapq.heappop(hi)
        return res

if __name__ == '__main__':
    a = Solution()
    a.medianSlidingWindow2([1,3,-1,-3,5,3,6,7], 3)