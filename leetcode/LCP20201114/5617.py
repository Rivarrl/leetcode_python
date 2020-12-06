# -*- coding: utf-8 -*-
# ======================================
# @File    : 5617.py
# @Time    : 2020/12/6 10:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5617. 设计 Goal 解析器]
    """
    @timeit
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")


if __name__ == '__main__':
    a = Solution()
    a.interpret(command = "G()(al)")
    a.interpret(command = "G()()()()(al)")
    a.interpret(command = "(al)G(al)()()G")