# -*- coding: utf-8 -*-
# ======================================
# @File    : 5335.py
# @Time    : 2020/2/9 10:40
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5335. 参加考试的最大学生数](https://leetcode-cn.com/problems/maximum-students-taking-exam)
    """
    @timeit
    def maxStudents(self, seats: List[List[str]]) -> int:
        def valid(arr, x):
            for i in range(m):
                if (1 << i) & x > 0 and arr[i] == '#':
                    return False
            return True
        def ok(x):
            while x > 0:
                if x & 1 and (x >> 1) & 1:
                    return False
                x >>= 1
            return True
        def count(x):
            ctr = 0
            while x > 0:
                ctr += (x & 1)
                x >>= 1
            return ctr
        n, m = len(seats), len(seats[0])
        dp = [[0] * (1 << m) for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(1 << m):
                if not valid(seats[i], j) or not ok(j): continue
                ctr = count(j)
                if i == 0:
                    dp[i][j] = ctr
                else:
                    for k in range(1 << m):
                        if ok(j | k):
                            dp[i][j] = max(dp[i][j], dp[i-1][k] + ctr)
                res = max(res, dp[i][j])
        return res

if __name__ == '__main__':
    a = Solution()
    a.maxStudents([["#",".","#","#",".","#"],
              [".","#","#","#","#","."],
              ["#",".","#","#",".","#"]])
    a.maxStudents([[".","#"],
              ["#","#"],
              ["#","."],
              ["#","#"],
              [".","#"]])
    a.maxStudents([["#",".",".",".","#"],
              [".","#",".","#","."],
              [".",".","#",".","."],
              [".","#",".","#","."],
              ["#",".",".",".","#"]])
    a.maxStudents([[".","#","#",".","#","#","#"],
                   [".","#","#",".",".",".","."],
                   ["#","#",".",".","#","#","#"],
                   [".",".",".","#","#",".","."],
                   [".","#","#",".",".",".","#"],
                   [".",".",".",".",".","#","."]])
    a.maxStudents([[".",".",".",".","#",".",".","."],
                   [".",".",".",".",".",".",".","."],
                   [".",".",".",".",".",".",".","."],
                   [".",".",".",".",".",".","#","."],
                   [".",".",".",".",".",".",".","."],
                   [".",".","#",".",".",".",".","."],
                   [".",".",".",".",".",".",".","."],
                   [".",".",".","#",".",".","#","."]])