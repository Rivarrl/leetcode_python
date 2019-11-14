# -*- coding: utf-8 -*-
# ======================================
# @File    : 390.py
# @Time    : 2019/11/14 9:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import timeit

class Solution:
    """
    [390. 消除游戏](https://leetcode-cn.com/problems/elimination-game/)
    """
    @timeit
    def lastRemaining(self, n: int) -> int:
        """
        思路：数学，n是奇数个数的时候最后一个是多余的，和n-1答案一样，f(x) = f(x-1)
        而去掉奇数部分后的数列整体/2，又得到了一个1到n/2的数列，但是由于是S型消除，得到的数列从后向前消除，f(x) = 2 * f(x/2)'
        也就是说需要找到跟顺序消除的答案在位置上镜像相反的那个数，也就是r = x+1-r'，f(x)' = x + 1 - f(x)
        整理上面两个式子，n为偶数时f(x) = 2 * (x/2 + 1 - f(x/2))
        """
        def f(x):
            if x == 1: return 1
            if x & 1: return f(x - 1)
            return 2 * (x//2 + 1 - f(x//2))
        return f(n)

if __name__ == '__main__':
    a = Solution()
    for i in range(1, 25):
        a.lastRemaining(i)
