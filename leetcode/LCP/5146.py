# -*- coding: utf-8 -*-
# ======================================
# @File    : 5146
# @Time    : 2020/1/11 23:09
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5146. 不同的循环子字符串]()
    """
    @timeit
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        st = set()
        res = 0
        for i in range(n):
            for j in range(2, n-i+1, 2):
                if not text[i:i+j//2] in st and text[i:i+j//2] == text[i+j//2:i+j]:
                    st.add(text[i:i+j//2])
                    res += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.distinctEchoSubstrings(text = "abcabcabc")
    a.distinctEchoSubstrings(text = "leetcodeleetcode")