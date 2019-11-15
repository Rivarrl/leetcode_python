# -*- coding: utf-8 -*-
# ======================================
# @File    : 14.py
# @Time    : 2019/11/15 15:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [14. 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)
    """
    @timeit
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        思路：遍历比每个字母
        """
        if not strs: return ""
        i = -1
        flag = True
        while flag:
            i += 1
            if i >= len(strs[0]): break
            c = strs[0][i]
            for s in strs:
                if i == len(s) or s[i] != c:
                    flag = False
                    break
        return strs[0][:i]


if __name__ == '__main__':
    a = Solution()
    a.longestCommonPrefix(["flower","flow","flight"])
    a.longestCommonPrefix(["dog","racecar","car"])