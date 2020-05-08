# -*- coding: utf-8 -*-
# ======================================
# @File    : 937.py
# @Time    : 2020/5/8 23:36
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [937. 重新排列日志文件](https://leetcode-cn.com/problems/reorder-data-in-log-files/)
    """
    @timeit
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(x):
            idx, content = x.split(' ', 1)
            return (0, content, idx) if content[0].isalpha() else (1, )
        return sorted(logs, key=f)

if __name__ == '__main__':
    a = Solution()
    a.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])