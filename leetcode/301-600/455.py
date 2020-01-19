# -*- coding: utf-8 -*-
# ======================================
# @File    : 455
# @Time    : 2020/1/10 14:22
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [455. 分发饼干](https://leetcode-cn.com/problems/assign-cookies/)
    """
    @timeit
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                res += 1
            j += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.findContentChildren([10,9,8,7], [5,6,7,8])
    a.findContentChildren([1,2,3], [1,1])
    a.findContentChildren([1,2], [1,2,3])