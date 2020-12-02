# -*- coding: utf-8 -*-
# ======================================
# @File    : 1674.py
# @Time    : 2020/12/2 7:15 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1674. 使数组互补的最少操作次数](https://leetcode-cn.com/problems/minimum-moves-to-make-array-complementary/)
    """
    @timeit
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        d = {}
        for i in range(n//2):
            s = nums[i] + nums[n-1-i]
            d[s] = d.get(s, 0) + 1
        arr = sorted(d.keys())
        na = len(arr)
        z = [arr[na//2]] if na & 1 else [arr[na//2], arr[na//2-1]]
        res = n + 1
        for s in z:
            tmp = 0
            for i in range(n//2):
                cur = nums[i] + nums[n-1-i]
                if cur > s:
                    diff = cur - s
                    f = 2
                    for x in (nums[i], nums[n-1-i]):
                        if x - 1 >= diff:
                            f = 1
                            break
                    tmp += f
                elif cur < s:
                    diff = s - cur
                    f = 2
                    for x in (nums[i], nums[n-1-i]):
                        if limit - x >= diff:
                            f = 1
                            break
                    tmp += f
            res = min(res, tmp)
        return res

if __name__ == '__main__':
    a = Solution()
    # a.minMoves(nums = [1,2,4,3], limit = 4)
    # a.minMoves(nums = [1,2,2,1], limit = 2)
    # a.minMoves(nums = [1,2,1,2], limit = 2)
    a.minMoves([28,50,76,80,64,30,32,84,53,8], 84)