# -*- coding: utf-8 -*-
# ======================================
# @File    : 1694.py
# @Time    : 2020/12/20 12:11
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1694. 重新格式化电话号码](https://leetcode-cn.com/problems/reformat-phone-number)
    """
    @timeit
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "").replace("-", "")
        n = len(number)
        tail = ""
        if n >= 4 and n % 3 == 1:
            tail = number[-4:-2] + '-' + number[-2:]
            number = number[:-4]
            n -= 4
        head = '-'.join([number[i:i+3] for i in range(0, n, 3)])
        if tail:
            if head:
                head = head + '-' + tail
            else:
                head = tail
        return head


if __name__ == '__main__':
    a = Solution()
    a.reformatNumber(number = "1-23-45 6")
    a.reformatNumber(number = "123 4-567")
    a.reformatNumber(number = "123 4-5678")
    a.reformatNumber(number = "12")
    a.reformatNumber(number = "--17-5 229 35-39475 ")