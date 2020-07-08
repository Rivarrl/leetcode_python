# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-11.py
# @Time    : 2020/7/8 21:42
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 16.11. 跳水板](https://leetcode-cn.com/problems/diving-board-lcci/)
    """
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        elif shorter == longer:
            return [k*shorter]
        return list(range(shorter*k, longer*k + 1, (longer-shorter)))

if __name__ == '__main__':
    a = Solution()
    a.divingBoard(1,2,3)