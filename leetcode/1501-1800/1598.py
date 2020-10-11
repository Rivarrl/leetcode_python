# -*- coding: utf-8 -*-
# ======================================
# @File    : 1598.py
# @Time    : 2020/10/1 11:53
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1598. 文件夹操作日志搜集器](https://leetcode-cn.com/problems/crawler-log-folder/)
    """
    @timeit
    def minOperations(self, logs: List[str]) -> int:
        s = 0
        for op in logs:
            if op.startswith('..'):
                s = max(0, s-1)
            elif not op.startswith('.'):
                s += 1
        return s

if __name__ == '__main__':
    a = Solution()
    a.minOperations(logs = ["d1/","d2/","../","d21/","./"])
    a.minOperations(logs = ["d1/","d2/","./","d3/","../","d31/"])
    a.minOperations(logs = ["d1/","../","../","../"])