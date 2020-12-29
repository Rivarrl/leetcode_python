# -*- coding: utf-8 -*-
# ======================================
# @File    : 752.py
# @Time    : 2020/12/29 1:41 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [752. 打开转盘锁](https://leetcode-cn.com/problems/open-the-lock/)
    """
    @timeit
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        seen = set(deadends)
        if "0000" in seen: return -1
        seen.add("0000")
        q = deque([["0000",0]])
        while q:
            pwd, st = q.popleft()
            if pwd == target: return st
            for i in range(4):
                n1 = '{}{}{}'.format(pwd[:i], (int(pwd[i]) + 1) % 10, pwd[i+1:])
                n2 = '{}{}{}'.format(pwd[:i], (int(pwd[i]) + 10 - 1) % 10, pwd[i+1:])
                for n in (n1, n2):
                    if n in seen: continue
                    seen.add(n)
                    q.append([n, st+1])
        return -1

if __name__ == '__main__':
    a = Solution()
    a.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202")
    a.openLock(deadends = ["8888"], target = "0009")
    a.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888")
    a.openLock(deadends = ["0000"], target = "8888")