# -*- coding: utf-8 -*-
# ======================================
# @File    : 440.py
# @Time    : 2019/11/28 0:25
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import sys
sys.setrecursionlimit(10000)
class Solution:
    """
    [440. 字典序的第K小数字](https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/)
    """
    @timeit
    def findKthNumber(self, n: int, k: int) -> int:
        """
        思路：模拟10叉树的先序非递归遍历。
        每棵树访问前计算完整遍历它一共需要多少步，如果步数大于k，说明第k小数字在该树中
        """
        k -= 1
        res = 1
        while k > 0:
            step, left, right = 0, res, res+1
            while left <= n:
                step += min(n+1, right) - left
                left *= 10
                right *= 10
            if step <= k:
                k -= step
                res += 1
            else:
                k -= 1
                res *= 10
        return res


if __name__ == '__main__':
    a = Solution()
    a.findKthNumber(7747794, 5857460)