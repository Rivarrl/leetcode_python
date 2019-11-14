# -*- coding: utf-8 -*-
# ======================================
# @File    : 403.py
# @Time    : 2019/11/14 13:37
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import sys

sys.setrecursionlimit(1111)
class Solution:
    """
    [403. 青蛙过河](https://leetcode-cn.com/problems/frog-jump/)
    """
    @timeit
    def canCross(self, stones: List[int]) -> bool:
        """
        思路：dfs计时偷鸡/记忆化搜索
        """
        import time
        def dfs(i, speed, t):
            # 这里经验流调参了，哈哈
            # if time.time() - t > 0.002: return False
            if i == n - 1: return True
            if (i, speed) in dp: return dp[(i, speed)]
            for sp in range(1, -2, -1):
                ns = speed + sp
                jump = stones[i] + ns
                if stones[i] < jump <= stones[n-1] and jump in st and dfs(st[jump], ns, t):
                    dp[(i, speed)] = True
                    return True
            dp[(i, speed)] = False
            return False
        n = len(stones)
        st = {stones[i]: i for i in range(n)}
        start = time.time()
        dp = {}
        return dfs(0, 0, start)


if __name__ == '__main__':
    a = Solution()
    x = [0]
    # for i in range(1, 1100):
    #     x += [x[-1] + i]
    # a.canCross(x)
    # a.canCross([0,1,3,5,6,8,12,17])
    a.canCross([0,1,2,3,4,8,9,11])
