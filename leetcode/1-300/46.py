# -*- coding: utf-8 -*-
# ======================================
# @File    : 46.py
# @Time    : 2019/11/16 21:55
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [46. 全排列](https://leetcode-cn.com/problems/permutations/)
    """
    @timeit
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        思路：回溯算法，由于没有重复的数字，每次传一个值，用二进制代表哪个位置被选过
        """
        n = len(nums)
        def dfs(a, cur):
            nonlocal res
            if a == (1 << n) - 1: res.append(cur)
            for i in range(n):
                if a & (1 << i): continue
                dfs(a | (1 << i), cur + [nums[i]])
        res = []
        dfs(0, [])
        return res


    @timeit
    def permute2(self, nums: List[int]) -> List[List[int]]:
        """
        思路：回溯算法，大佬的交换法，可以随递归深度缩小遍历次数
        """
        n = len(nums)
        def dfs(start):
            nonlocal res
            if start == n: res.append(nums[:])
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        res = []
        dfs(0)
        return res


if __name__ == '__main__':
    a = Solution()
    a.permute([1,2,3])
    a.permute2([1,2,3])