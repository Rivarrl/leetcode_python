# -*- coding: utf-8 -*-
# ======================================
# @File    : 659.py
# @Time    : 2020/12/4 9:43 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [659. 分割数组为连续子序列](https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/)
    """
    @timeit
    def isPossible(self, nums: List[int]) -> bool:
        # hashmap + minheap O(nlogn) & O(n)
        import heapq
        d = {}
        for x in nums:
            if x not in d:
                d[x] = []
            cur = 1 if x-1 not in d or len(d[x-1]) == 0 else heapq.heappop(d[x-1])+1
            heapq.heappush(d[x], cur)
        for k, vs in d.items():
            while vs:
                if heapq.heappop(vs) < 3:
                    return False
        return True

    @timeit
    def isPossible2(self, nums: List[int]) -> bool:
        # hashmap * 2 O(n) & O(n)
        # 元素x的出现次数 = 连接x-1的次数 + 以x开头的次数
        from collections import defaultdict
        d1, d2 = defaultdict(int), defaultdict(int)
        for x in nums:
            d1[x] += 1
        for x in nums:
            ctr = d1[x]
            if ctr > 0:
                if d2.get(x - 1, 0) > 0:
                    d1[x] -= 1
                    d2[x] += 1
                    d2[x-1] -= 1
                else:
                    if d1.get(x+1, 0) > 0 and d1.get(x+2, 0) > 0:
                        d1[x] -= 1
                        d1[x+1] -= 1
                        d1[x+2] -= 1
                        d2[x+2] += 1
                    else:
                        return False
        return True

    @timeit
    def isPossible3(self, nums: List[int]) -> bool:
        # O(n) & O(1)
        dp1 = dp2 = dp3 = 0
        i, n = 0, len(nums)
        while i < n:
            j, x = i, nums[i]
            while i < n and nums[i] == x:
                i += 1
            total = i - j
            if j > 0 and x != nums[j - 1] + 1: # nums[i] > nums[i-1] + 1 截断
                if dp1 + dp2 > 0:
                    return False
                else:
                    dp1 = total
                    dp2 = dp3 = 0
            else:
                if dp1 + dp2 > total:
                    return False
                left = total - dp1 - dp2 # 补给dp1和dp2之后剩余的数量
                tail = min(dp3, left) # 补给dp3的数量，不能超过dp3
                dp3 = tail + dp2
                dp2 = dp1
                dp1 = left - tail
        return dp1 + dp2 == 0

if __name__ == '__main__':
    a = Solution()
    a.isPossible([1,2,3,3,4,5])
    a.isPossible([1,2,3,3,4,4,5,5])
    a.isPossible([1,2,3,4,4,5])