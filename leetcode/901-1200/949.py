# -*- coding: utf-8 -*-
# ======================================
# @File    : 949.py
# @Time    : 2019/12/4 16:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [949. 给定数字能组成的最大时间](https://leetcode-cn.com/problems/largest-time-for-given-digits/)
    """
    @timeit
    def largestTimeFromDigits(self, A: List[int]) -> str:
        """
        思路：贪心，从左到右每一位挑能挑的最大值
        """
        A.sort()
        res = [0] * 4
        # 24以上的小时不合理
        if A[0] > 2 or A[0] == 2 and A[1] > 3: return ""
        # 超过3个>=6的组不成分针十位
        if A[1] >= 6: return ""
        # 22:66这种情况也不行
        if A[0] == 2 and A[2] >= 6: return ""
        # 21:66 -> 16:26
        if A[1] == 2 and A[2] >= 6:
            res[0] = A[0]
            res[1] = A[3]
            res[2] = A[1]
            res[3] = A[2]
        elif 2 in A:
            A.remove(2)
            res[0] = 2
            i = 2
            while i > 0:
                if A[i] < 4: break
                i -= 1
            res[1] = A.pop(i)
            if A[-1] < 6: res[2], res[3] = A[::-1]
            else: res[2], res[3] = A
        else:
            if 1 in A:
                A.remove(1)
                res[0] = 1
            else:
                A.remove(0)
            res[1] = A.pop()
            if A[-1] < 6: res[2], res[3] = A[::-1]
            else: res[2], res[3] = A
        return "{}{}:{}{}".format(*res)


    @timeit
    def largestTimeFromDigits2(self, A: List[int]) -> str:
        # 没那么多判断,把全排列从大到小遍历
        from itertools import permutations
        t = 0
        for a, b, c, d in permutations(A):
            if a >= 3 or a == 2 and b >= 4 or c >= 6: continue
            hh = a * 10 + b
            mi = c * 10 + d
            t = max(t, hh * 100 + mi)
        if t == 0 and sum(A) > 0: return ""
        res = [0] * 4
        i = 3
        while t > 0:
            res[i] = t % 10
            t //= 10
            i -= 1
        return "{}{}:{}{}".format(*res)

if __name__ == '__main__':
    a = Solution()
    a.largestTimeFromDigits2([1,2,3,4])
    a.largestTimeFromDigits2([1,2,9,9])
    a.largestTimeFromDigits2([5,5,5,5])
    a.largestTimeFromDigits2([0,0,4,0])
    a.largestTimeFromDigits2([1,0,8,6])