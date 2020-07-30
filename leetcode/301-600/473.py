# -*- coding: utf-8 -*-
# ======================================
# @File    : 473.py
# @Time    : 2020/7/30 11:59 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [473. 火柴拼正方形](https://leetcode-cn.com/problems/matchsticks-to-square/)
    """
    @timeit
    def makesquare(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0: return False
        s = sum(nums)
        a = s // 4
        if a * 4 < s: return False
        nums.sort(reverse=True)
        if nums[0] > a: return False
        arr = [0] * 4
        def f(i):
            if i == n:
                # 3条边满足即可
                return all(e == a for e in arr[:-1])
            for j in range(4):
                if arr[j] + nums[i] <= a:
                    arr[j] += nums[i]
                    if f(i+1): return True
                    arr[j] -= nums[i]
            return False
        return f(0)



if __name__ == '__main__':
    a = Solution()
    a.makesquare([1,1,2,2,2])
    a.makesquare([3,3,3,3,4])