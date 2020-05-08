# -*- coding: utf-8 -*-
# ======================================
# @File    : 336.py
# @Time    : 2020/5/8 18:25
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [336. 回文对](https://leetcode-cn.com/problems/palindrome-pairs/)
    """
    @timeit
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # 字典
        # 一共有三类：
        # 1. 中分：abc + cba
        # 2. 左侧尾部有回文串：abcxyxyx + cba
        # 3. 右侧头部有回文串：abc + xyxyxcba
        d = {word: i for i, word in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            rev = word[::-1]
            if rev in d and i != d[rev]:
                res.append([i, d[rev]])
            for j, x in enumerate(word):
                if word[j:] == word[j:][::-1] and word[:j][::-1] in d:
                    res.append([i, d[word[:j][::-1]]])
                if word[:j+1] == word[:j+1][::-1] and word[j+1:][::-1] in d:
                    res.append([d[word[j+1:][::-1]], i])
        return res


if __name__ == '__main__':
    a = Solution()
    a.palindromePairs(["abcd","dcba","lls","s","sssll"])
    a.palindromePairs(["bat","tab","cat"])