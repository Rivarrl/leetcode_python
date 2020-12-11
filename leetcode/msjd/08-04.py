# -*- coding: utf-8 -*-
# ======================================
# @File    : 08-04.py
# @Time    : 2020/12/11 1:24 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 08.04. 幂集](https://leetcode-cn.com/problems/power-set-lcci/)
    """
    @timeit
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 迭代，遍历所有状态
        n = len(nums)
        def f(n):
            idx = 0
            while n:
                if n & 1:
                    yield idx
                n >>= 1
                idx += 1
        res = [[]]
        for i in range(1, 1 << n):
            x = [nums[j] for j in f(i)]
            res.append(x)
        return res

    @timeit
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        # 回溯，选或不选
        n = len(nums)
        res = []
        def f(i, arr):
            if i == n:
                res.append(arr)
                return
            f(i+1, arr)
            f(i+1, arr + [nums[i]])
        f(0, [])
        return res

    @timeit
    def subsets3(self, nums: List[int]) -> List[List[int]]:
        # 递归
        n = len(nums)
        def f(i):
            c = nums[i]
            if i == n - 1:
                return [[c], []]
            res = []
            for x in f(i+1):
                res.append(x)
                res.append([c] + x)
            return res
        return f(0)

if __name__ == '__main__':
    a = Solution()
    # a.subsets([1,2,3])
    # a.subsets2([1,2,3])
    a.subsets3([1,2,3])