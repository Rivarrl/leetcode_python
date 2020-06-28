# -*- coding: utf-8 -*-
# ======================================
# @File    : 1477.py
# @Time    : 2020/6/28 5:39 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1477. 找两个和为目标值且不重叠的子数组](https://leetcode-cn.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/)
    """
    @timeit
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # 超时了
        INT_MAX = 0x3f3f3f3f
        left = right = 0
        n = len(arr)
        total = 0
        d = {}
        while right < n:
            total += arr[right]
            right += 1
            if total < target: continue
            while left <= right and total > target:
                total -= arr[left]
                left += 1
            if total == target:
                d[right - left] = d.get(right - left, []) + [left]
        res = INT_MAX
        sd = sorted(d)
        for k in sd:
            if k * 2 > res: break
            idxs = d[k]
            f = True
            for i in idxs:
                l1, l2 = i, i + k
                for k2 in sd:
                    for j in d[k2]:
                        l3, l4 = j, j + k2
                        if (l3 < l2 and l1 < l4) or (l4 < l1 and l2 < l3): continue
                        res = min(res, k + k2)
                        f = False
                        break
                    if not f: break
                if not f: break
        return res if res != INT_MAX else -1

if __name__ == '__main__':
    a = Solution()
    a.minSumOfLengths(arr = [3,2,2,4,3], target = 3)
    a.minSumOfLengths(arr = [7,3,4,7], target = 7)
    a.minSumOfLengths(arr = [4,3,2,6,2,3,4], target = 6)
    a.minSumOfLengths(arr = [5,5,4,4,5], target = 3)
    a.minSumOfLengths(arr = [3,1,1,1,5,1,2,1], target = 3)