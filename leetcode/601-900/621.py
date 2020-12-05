# -*- coding: utf-8 -*-
# ======================================
# @File    : 621.py
# @Time    : 2020/12/5 9:37 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [621. 任务调度器](https://leetcode-cn.com/problems/task-scheduler/)
    """
    @timeit
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = [0] * 26
        for x in tasks:
            i = ord(x) - ord('A')
            d[i] += 1
        s = max(d)
        mx = 0
        for x in d:
            if x == s:
                mx += 1
        return max((s - 1) * (n + 1) + mx, len(tasks))

if __name__ == '__main__':
    a = Solution()
    a.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2)
    a.leastInterval(tasks = ["A","A","A","B","B","B"], n = 0)
    a.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2)