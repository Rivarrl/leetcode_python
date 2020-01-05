# -*- coding: utf-8 -*-
# ======================================
# @File    : 5303
# @Time    : 2020/1/5 14:58
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *


class Solution:
    """
    5303. 解码字母到整数映射
    """
    @timeit
    def freqAlphabets(self, s: str) -> str:
        i, n = 0, len(s)
        res = ''
        while i < n:
            z = chr(ord('a') - 1 + int(s[i]))
            if s[i] in {'1', '2'}:
                if i + 2 < n and s[i+2] == '#':
                    z = chr(ord('a') - 1 + int(s[i:i+2]))
                    i += 2
            res += z
            i += 1
        return res


if __name__ == '__main__':
    a = Solution()
    a.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#")

