# -*- coding: utf-8 -*-
# ======================================
# @File    : 5172.py
# @Time    : 2020/2/23 11:39
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5172. 形成三的最大倍数](https://leetcode-cn.com/problems/largest-multiple-of-three/)
    """
    @timeit
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        n = len(digits)
        s = sum(digits)
        k = s % 3
        if k == 0:
            res = ''.join([str(e) for e in digits])
        else:
            r1 = -1
            for i in range(n-1, -1, -1):
                if digits[i] % 3 == k:
                    r1 = i
                    break
            r2 = []
            c = 0
            for i in range(n-1, -1, -1):
                if digits[i] % 3 == 3 - k:
                    r2 += [i]
                    c += 1
                    if c == 2:
                        break
            if not r2 or r1 < 0:
                if not r2:
                    res = ''.join([str(digits[i]) for i in range(n) if i != r1])
                else:
                    res = ''.join([str(digits[i]) for i in range(n) if not i in r2])
            else:
                if digits[r1] <= sum([digits[i] for i in r2]):
                    res = ''.join([str(digits[i]) for i in range(n) if i != r1])
                else:
                    res = ''.join([str(digits[i]) for i in range(n) if not i in r2])
        if not res: return res
        res = res.lstrip('0')
        if not res: res = '0'
        return res


if __name__ == '__main__':
    a = Solution()
    # a.largestMultipleOfThree([8, 1, 9])
    # a.largestMultipleOfThree([8,6,7,1,0])
    # a.largestMultipleOfThree([1])
    # a.largestMultipleOfThree([0,0,0,0,0,0])
    a.largestMultipleOfThree([1,1,1,2])