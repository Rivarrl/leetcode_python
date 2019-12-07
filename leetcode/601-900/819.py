# -*- coding: utf-8 -*-
# ======================================
# @File    : 819.py
# @Time    : 2019/11/27 23:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [819. 最常见的单词](https://leetcode-cn.com/problems/most-common-word/)
    """
    @timeit
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        思路：字典
        """
        banned = set(banned)
        a, z, A, Z = ord('a'), ord('z'), ord('A'), ord('Z')
        j = k = 0
        words = {}
        res = ""
        def update(j, k):
            nonlocal res
            word = paragraph[j:k].lower()
            if word and not word in banned:
                words[word] = words.get(word, 0) + 1
                if words.get(res, 0) < words[word]:
                    res = word
        for i, c in enumerate(paragraph):
            if a <= ord(c) <= z or A <= ord(c) <= Z:
                k = i + 1
            else:
                update(j, k)
                j = i + 1
        update(j, k)
        return res


if __name__ == '__main__':
    a = Solution()
    a.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"])
    a.mostCommonWord('a.', [])
    a.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"])