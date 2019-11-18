# -*- coding: utf-8 -*-
# ======================================
# @File    : 842.py
# @Time    : 2019/11/18 13:15
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [842. 将数组拆分成斐波那契序列](https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/)
    """
    @timeit
    def splitIntoFibonacci(self, S: str) -> List[int]:
        """
        思路：回溯
        """
        n = len(S)
        up = (1 << 31) - 1
        def dfs(i, cur):
            if i == n:
                if len(cur) >= 3 and cur[-1] == cur[-2] + cur[-3]:
                    nonlocal res
                    res = cur[:]
                return
            if int(S[i]) == 0:
                dfs(i + 1, cur + [int(S[i])])
            else:
                c = 0
                for j in range(i, min(i + n//3 + 1, n)):
                    c = c * 10 + int(S[j])
                    if c > up: break
                    if len(cur) < 2 or c == cur[-1] + cur[-2]:
                        cur += [c]
                        dfs(j+1, cur)
                        cur.pop()
                    elif c > cur[-1] + cur[-2]:
                        break
        res = []
        dfs(0, [])
        return res

if __name__ == '__main__':
    a = Solution()
    a.splitIntoFibonacci("17522")
    a.splitIntoFibonacci("123456579")
    a.splitIntoFibonacci("0123")
    a.splitIntoFibonacci("1101111")
    a.splitIntoFibonacci("11235813")
    a.splitIntoFibonacci("112358130")
    a.splitIntoFibonacci("0000")
    a.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511")