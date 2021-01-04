# -*- coding: utf-8 -*-
# ======================================
# @File    : 605.py
# @Time    : 2019/11/11 0:49
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        [605. 种花问题](https://leetcode-cn.com/problems/can-place-flowers/)
        思路：先把两侧加上两块空地，使得左右边界的空地可以比较，然后用贪心法，能种就种下
        """
        if n == 0: return True
        size = len(flowerbed)
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, size+1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
        return n == 0


if __name__ == '__main__':
    a = Solution()
    a.canPlaceFlowers([1,0,0,0,1,0,0], 2)