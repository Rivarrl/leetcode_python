# -*- coding: utf-8 -*-
# ======================================
# @File    : 675.py
# @Time    : 2020/12/22 1:03 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [675. 为高尔夫比赛砍树](https://leetcode-cn.com/problems/cut-off-trees-for-golf-event/)
    """
    @timeit
    def cutOffTree(self, forest: List[List[int]]) -> int:
        from collections import deque
        import heapq
        R, C = len(forest), len(forest[0])
        trees = sorted((x, r, c) for r, row in enumerate(forest) for c, x in enumerate(row) if x > 0)
        def bfs(sr, sc, tr, tc):
            q = deque([(sr, sc, 0)])
            seen = {(sr, sc)}
            while q:
                r, c, d = q.popleft()
                if r == tr and c == tc: return d
                for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                    if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in seen and forest[nr][nc] > 0:
                        seen.add((nr, nc))
                        q.append((nr, nc, d+1))
            return -1

        def astar(sr, sc, tr, tc):
            R, C = len(forest), len(forest[0])
            heap = [(0, 0, sr, sc)]
            cost = {(sr, sc): 0}
            while heap:
                f, g, r, c = heapq.heappop(heap)
                if r == tr and c == tc: return g
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                        ncost = g + 1 + abs(nr - tr) + abs(nc - tc)
                        if ncost < cost.get((nr, nc), 9999):
                            cost[nr, nc] = ncost
                            heapq.heappush(heap, (ncost, g + 1, nr, nc))
            return -1

        def hadlocks(forest, sr, sc, tr, tc):
            R, C = len(forest), len(forest[0])
            processed = set()
            q = deque([(0, sr, sc)])
            while q:
                detours, r, c = q.popleft()
                if (r, c) not in processed:
                    processed.add((r, c))
                    if r == tr and c == tc:
                        return abs(sr - tr) + abs(sc - tc) + 2 * detours
                    for nr, nc, closer in ((r - 1, c, r > tr), (r + 1, c, r < tr),
                                           (r, c - 1, c > tc), (r, c + 1, c < tc)):
                        if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                            if closer:
                                q.appendleft((detours, nr, nc))
                            else:
                                q.append((detours + 1, nr, nc))
            return -1

        sr = sc = res = 0
        for _, tr, tc in trees:
            d = bfs(sr, sc, tr, tc)
            if d < 0: return -1
            res += d
            sr, sc = tr, tc
        return res

if __name__ == '__main__':
    a = Solution()
    a.cutOffTree(forest = [[1,2,3],[0,0,4],[7,6,5]])
    a.cutOffTree(forest = [[1,2,3],[0,0,0],[7,6,5]])
    a.cutOffTree(forest = [[2,3,4],[0,0,5],[8,7,6]])