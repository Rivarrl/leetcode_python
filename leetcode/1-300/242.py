# -*- coding: utf-8 -*-
# ======================================
# @File    : 242
# @Time    : 2020/1/11 18:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [242. 有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)
    """
    @timeit
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            d[c] = d.get(c, 0) - 1
            if d[c] < 0:
                return False
        return all(v == 0 for v in d.values())


if __name__ == '__main__':
    a = Solution()
    a.isAnagram(s = "anagram", t = "nagaram")
    a.isAnagram(s = "rat", t = "car")