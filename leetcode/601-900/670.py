# -*- coding: utf-8 -*-
# ======================================
# @File    : 670.py
# @Time    : 2020/12/22 10:16 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [670. 最大交换](https://leetcode-cn.com/problems/maximum-swap/)
    """
    @timeit
    def maximumSwap(self, num: int) -> int:
        # 记录右侧最大值下标
        arr = [int(e) for e in str(num)]
        n = len(arr)
        right = [0] * n
        m, mi = 0, n-1
        for i in range(n-1, -1, -1):
            if arr[i] > m:
                m, mi = arr[i], i
            right[i] = mi
        for i in range(n):
            if arr[i] < arr[right[i]]:
                arr[i], arr[right[i]] = arr[right[i]], arr[i]
                break
        return int(''.join([str(e) for e in arr]))


if __name__ == '__main__':
    a = Solution()
    a.maximumSwap(2736)
    a.maximumSwap(9973)
    a.maximumSwap(98368)
    a.maximumSwap(10909091)
