# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-20.py
# @Time    : 2020/11/16 1:27 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.20. T9键盘](https://leetcode-cn.com/problems/t9-lcci/)
    """
    @timeit
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        arr = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
        arr = [str(e) for e in arr]
        a = ord('a')
        res = []
        for word in words:
            for i, c in enumerate(word):
                if arr[ord(c) - a] != num[i]:
                    break
            else:
                res.append(word)
        return res

if __name__ == '__main__':
    a = Solution()
    a.getValidT9Words(num = "8733", words = ["tree", "used"])
    a.getValidT9Words(num = "2", words = ["a", "b", "c", "d"])