# -*- coding: utf-8 -*-
# ======================================
# @File    : 1128.py
# @Time    : 2019/12/9 23:21
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1128. 等价多米诺骨牌对的数量](https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/)
    """
    @timeit
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        思路: 由于多米诺骨牌的值是1到9,可以用邻接矩阵
        """
        matrix = [[0] * 9 for _ in range(9)]
        for x, y in dominoes:
            if x > y: x, y = y, x
            matrix[x-1][y-1] += 1
        res = 0
        for i in range(9):
            for j in range(9):
                if matrix[i][j] >= 2:
                    res += (matrix[i][j] * (matrix[i][j] - 1)) // 2
        return res

if __name__ == '__main__':
    a = Solution()
    a.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]])
    a.numEquivDominoPairs([[2,1],[1,2],[1,2],[1,2],[2,1],[1,1],[1,2],[2,2]])