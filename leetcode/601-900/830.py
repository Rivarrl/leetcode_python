# -*- coding: utf-8 -*-
# ======================================
# @File    : 830.py
# @Time    : 2019/12/24 0:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [830. 较大分组的位置](https://leetcode-cn.com/problems/positions-of-large-groups/)
    """
    @timeit
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []
        i = j = 0
        n = len(S)
        while j < n:
            while j < n and S[j] == S[i]:
                j += 1
            if j - i >= 3: res.append([i, j-1])
            i = j
        return res


if __name__ == '__main__':
    a = Solution()
    a.largeGroupPositions("abbxxxxzzy")
    a.largeGroupPositions("abc")
    a.largeGroupPositions("abcdddeeeeaabbbcd")
