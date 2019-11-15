# -*- coding: utf-8 -*-
# ======================================
# @File    : 17.py
# @Time    : 2019/11/15 15:35
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [17. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)
    """
    @timeit
    def letterCombinations(self, digits: str) -> List[str]:
        """
        思路：回溯算法，注意7和9是四个键
        """
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
             }
        def helper(i):
            if i == len(digits): return [""]
            cur = []
            for x in helper(i+1):
                for c in d[digits[i]]:
                    cur.append(c + x)
            return cur
        if not digits: return []
        return helper(0)

if __name__ == '__main__':
    a = Solution()
    a.letterCombinations("23")