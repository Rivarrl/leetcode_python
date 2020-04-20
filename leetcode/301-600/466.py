# -*- coding: utf-8 -*-
# ======================================
# @File    : 466.py
# @Time    : 2020/4/19 14:08
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [466. 统计重复个数](https://leetcode-cn.com/problems/count-the-repetitions/)
    """
    @timeit
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        c1 = c2 = i = 0
        loop = {}
        while True:
            c1 += 1
            for c in s1:
                if s2[i] == c:
                    i += 1
                    if i == len(s2):
                        c2 += 1
                        i = 0
            if c1 == n1: return c2 // n2
            if not i in loop:
                loop[i] = (c1, c2)
            else:
                pre = loop[i]
                last = (c1-pre[0], c2-pre[1])
                break
        res = pre[1] + (n1 - pre[0]) // last[0] * last[1]
        # 剩下的部分遍历模拟
        rest = (n1 - pre[0]) % last[0]
        while rest > 0:
            for c in s1:
                if s2[i] == c:
                    i += 1
                    if i == len(s2):
                        res += 1
                        i = 0
            rest -= 1
        return res // n2


if __name__ == '__main__':
    a = Solution()
    a.getMaxRepetitions(s1="acb", n1=4, s2="ab", n2=2)
    a.getMaxRepetitions("abaacdbac",100,"adcbd",4)
    a.getMaxRepetitions("baba",11,"baab",1)