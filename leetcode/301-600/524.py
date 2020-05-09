# -*- coding: utf-8 -*-
# ======================================
# @File    : 524.py
# @Time    : 2020/5/9 17:48
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [524. 通过删除字母匹配到字典里最长单词](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/)
    """
    @timeit
    def findLongestWord(self, s: str, d: List[str]) -> str:
        from collections import Counter
        ds = Counter(s)
        n = len(s)
        d.sort(key=lambda x: (-len(x), x))
        for word in d:
            dw = Counter(word)
            flag = True
            for k, v in dw.items():
                if not k in ds or ds[k] < v:
                    flag = False
                    break
            if not flag: continue
            i = j = 0
            m = len(word)
            while i < n and j < m:
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == m: return word
        return ""


if __name__ == '__main__':
    a = Solution()
    a.findLongestWord(s = "abpcplea", d = ["ale","apple","monkey","plea"])
    a.findLongestWord(s = "abpcplea", d = ["a","b","c"])