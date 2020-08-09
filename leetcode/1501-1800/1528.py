# -*- coding: utf-8 -*-
# ======================================
# @File    : 1528.py
# @Time    : 2020/8/7 15:27
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1528. 重新排列字符串](https://leetcode-cn.com/problems/shuffle-string/)
    """
    @timeit
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        t = [''] * n
        for i in range(n):
            t[indices[i]] = s[i]
        return ''.join(t)

if __name__ == '__main__':
    a = Solution()
    a.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3])
    a.restoreString(s = "abc", indices = [0,1,2])
    a.restoreString(s = "aiohn", indices = [3,1,4,2,0])
    a.restoreString(s = "aaiougrt", indices = [4,0,2,6,7,3,1,5])
    a.restoreString(s = "art", indices = [1,0,2])