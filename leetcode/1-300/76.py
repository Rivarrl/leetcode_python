# -*- coding: utf-8 -*-
# ======================================
# @File    : 76.py
# @Time    : 2019/12/18 18:31
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)
    滑动窗口，窗口内有效字符统计，与t字符个数依次做对比，多退少补，更新最小长度和起始位即可。
    """
    @timeit
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter, defaultdict
        # 统计t中所需字符个数
        need = Counter(t)
        # 窗口中的字符个数
        cur = defaultdict(int)
        n = len(s)
        # 把无效字符过滤掉
        ls = [(i, s[i]) for i in range(n) if s[i] in need]
        i = j = 0
        start, length = 0, n + 1
        count = 0
        while j < len(ls):
            c = ls[j][1]
            cur[c] += 1
            if cur[c] == need[c]: count += 1
            while count == len(need):
                left, right = ls[i], ls[j]
                if right[0] + 1 - left[0] < length:
                    start, length = left[0], right[0] + 1 - left[0]
                cur[left[1]] -= 1
                if cur[left[1]] < need[left[1]]:
                    count -= 1
                i += 1
            j += 1
        return '' if length > n else s[start:start+length]


if __name__ == '__main__':
    a = Solution()
    a.minWindow(s = "ADOBECODEBANC", t = "ABC")
    a.minWindow(s = "a", t = "aa")