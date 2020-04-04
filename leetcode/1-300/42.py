# -*- coding: utf-8 -*-
# ======================================
# @File    : 42.py
# @Time    : 2020/4/4 11:27
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    def trap(self, height: List[int]) -> int:
        # 分治
        n = len(height)
        if n <= 2: return 0
        mm = min(height[0], height[-1])
        if n == 3:
            return max(0, mm - height[1])
        m = max(height[1:-1])
        if m < mm:
            return sum([mm - height[i] for i in range(1, n-1)])
        else:
            idx = 0
            for i in range(1, n-1):
                if height[i] == m:
                    idx = i
            return self.trap(height[:idx+1]) + self.trap(height[idx:])

    def trap2(self, height: List[int]) -> int:
        # 按每个格子的蓄水量为单位，看左边最大值和右边最大值的较小值减去自身高度
        n = len(height)
        res = 0
        l, r = [0] * n, [0] * n
        for i in range(1, n):
            l[i] = max(l[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            r[i] = max(r[i+1], height[i+1])
        for i in range(n):
            res += max(0, min(l[i], r[i]) - height[i])
        return res

if __name__ == '__main__':
    a = Solution()
    r = a.trap2([0,1,0,2,1,0,1,3,2,1,2,1])
    print(r)