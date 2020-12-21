# -*- coding: utf-8 -*-
# ======================================
# @File    : 667.py
# @Time    : 2020/12/21 7:36 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [667. 优美的排列 II](https://leetcode-cn.com/problems/beautiful-arrangement-ii/)
    """
    @timeit
    def constructArray(self, n: int, k: int) -> List[int]:
        # 摆动数组是k=n-1，n-2到1可通过摆动的尾巴来控制
        res = []
        i, j, x = 1, n, 1
        for _ in range(k):
            if x:
                res.append(i)
                i += 1
            else:
                res.append(j)
                j -= 1
            x ^= 1
        if x == 0:
            res.extend([a for a in range(i, j+1)])
        else:
            res.extend([a for a in range(j, i-1, -1)])
        return res

if __name__ == '__main__':
    a = Solution()
    a.constructArray(3, 1)
    a.constructArray(3, 2)
    a.constructArray(10, 4)