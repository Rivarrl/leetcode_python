# -*- coding: utf-8 -*-
# ======================================
# @File    : 5405.py
# @Time    : 2020/5/10 10:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5405. 形成两个异或相等数组的三元组数目](https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)
    """
    @timeit
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        for i in range(n):
            x = arr[i]
            for k in range(i+1, n):
                x ^= arr[k]
                if x == 0: res += k - i
        return res

if __name__ == '__main__':
    a = Solution()
    a.countTriplets([2,3,1,6,7])
    a.countTriplets([1,1,1,1,1])
    a.countTriplets([2,3])
    a.countTriplets([1,3,5,7,9])
    a.countTriplets([7,11,12,9,5,2,7,17,22])