# -*- coding: utf-8 -*-
# ======================================
# @File    : 519.py
# @Time    : 2020/5/9 18:54
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import random
class Solution:
    """
    [519. 随机翻转矩阵](https://leetcode-cn.com/problems/random-flip-matrix/)
    黑名单映射至白名单，每次roll点都会产生一个{点数：上限}的键值对，点数就是黑名单，上限值为白名单
    因为之后的roll点，将不包含此上限值，roll到黑名单中的数字时，将其对应的白名单值返回。
    """
    def __init__(self, n_rows: int, n_cols: int):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.total = n_rows * n_cols
        self.flapped = 0
        self.d = {}

    def flip(self) -> List[int]:
        rem = self.total - 1 - self.flapped
        r = random.randint(0, rem)
        x = self.d.get(r, r)
        self.d[r] = self.d.get(rem, rem)
        self.flapped += 1
        return [x // self.n_cols, x % self.n_cols]

    def reset(self) -> None:
        self.d.clear()
        self.flapped = 0

if __name__ == '__main__':
    a = Solution(2,3)
    a.flip()
    a.flip()
    a.flip()
    a.flip()
    a = Solution(1,2)
    a.flip()
    a.flip()
    a.reset()
    a.flip()

