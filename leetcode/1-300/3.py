# -*- coding: utf-8 -*-
# ======================================
# @File    : 3.py
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
        n = len(s)
        left, right = 0, 0
        d = {}
        res = 0
        while right < n:
            if s[right] in d:
                left = max(d[s[right]], left)
            res = max(res, right - left + 1)
            d[s[right]] = right + 1
            right += 1
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