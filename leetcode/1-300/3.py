# -*- coding: utf-8 -*-
# ======================================
# @File    : 5277.py
# @Time    : 2019/11/9 16:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)
        思路：利用双指针和字典构造一个只能装下无重复字符的滑动窗口，重复字符进入窗口时更新左边界，向右滑出边界停止
        """
        d = {}
        res = j = 0
        for i, x in enumerate(s):
            if x in d:
                j = max(d[x], j)
            res = max(res, i - j + 1)
            d[x] = i + 1
        return res



if __name__ == '__main__':
    sol = Solution()
    res = sol.lengthOfLongestSubstring("abcabcbb")
    print(res)
    res = sol.lengthOfLongestSubstring("au")
    print(res)
    res = sol.lengthOfLongestSubstring("abba")
    print(res)
    res = sol.lengthOfLongestSubstring("tmmzuxt")
    print(res)