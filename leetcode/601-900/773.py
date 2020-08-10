# -*- coding: utf-8 -*-
# ======================================
# @File    : 773.py
# @Time    : 2020/8/10 23:20
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [773. 滑动谜题](https://leetcode-cn.com/problems/sliding-puzzle/)
    """
    @timeit
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        from collections import deque
        n, m = len(board), len(board[0])
        k1 = ''.join(''.join(str(e) for e in one) for one in board)
        q = deque([(k1, 0)])
        seen = {k1}
        while q:
            k, s = q.popleft()
            if k == '123450':
                return s
            i = k.index('0')
            for j in (i+1, i-1, i+m, i-m):
                if 0 <= j < (n*m):
                    if abs(i-j) == 1 and abs(i//m - j//m) == 1: continue
                    karr = [e for e in k]
                    karr[i], karr[j] = karr[j], karr[i]
                    nk = ''.join(karr)
                    if not nk in seen:
                        seen.add(nk)
                        q.append((nk, s+1))
        return -1

if __name__ == '__main__':
    a = Solution()
    a.slidingPuzzle([[1,2,3],[4,0,5]])
    a.slidingPuzzle([[1,2,3],[5,4,0]])
    a.slidingPuzzle([[4,1,2],[5,0,3]])
    a.slidingPuzzle([[3,2,4],[1,5,0]])