# -*- coding: utf-8 -*-
# ======================================
# @File    : 5108.py
# @Time    : 2019/11/16 23:21
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    5108. 加密数字
    给你一个非负整数 num ，返回它的「加密字符串」。
    加密的过程是把一个整数用某个未知函数进行转化，你需要从下表推测出该转化函数：
    示例 1：
    输入：num = 23
    输出："1000"
    示例 2：
    输入：num = 107
    输出："101100"
    提示：
    0 <= num <= 10^9
    """
    @timeit
    def encode(self, num: int) -> str:
        return bin(num + 1)[3:]


if __name__ == '__main__':
    a = Solution()
    a.encode(0)
    a.encode(1)
    a.encode(7)
    a.encode(107)
