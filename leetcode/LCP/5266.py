# -*- coding: utf-8 -*-
# ======================================
# @File    : 5266.py
# @Time    : 2019/11/17 10:56
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    5266. 推箱子
    「推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库中的目标位置。
    游戏地图用大小为 n * m 的网格 grid 表示，其中每个元素可以是墙、地板或者是箱子。
    现在你将作为玩家参与游戏，按规则将箱子 'B' 移动到目标位置 'T' ：
    玩家用字符 'S' 表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。
    地板用字符 '.' 表示，意味着可以自由行走。
    墙用字符 '#' 表示，意味着障碍物，不能通行。
    箱子仅有一个，用字符 'B' 表示。相应地，网格上有一个目标位置 'T'。
    玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。
    玩家无法越过箱子。
    返回将箱子推到目标位置的最小 推动 次数，如果无法做到，请返回 -1。
    示例 1：
    输入：grid = [["#","#","#","#","#","#"],
                 ["#","T","#","#","#","#"],
                 ["#",".",".","B",".","#"],
                 ["#",".","#","#",".","#"],
                 ["#",".",".",".","S","#"],
                 ["#","#","#","#","#","#"]]
    输出：3
    解释：我们只需要返回推箱子的次数。
    示例 2：
    输入：grid = [["#","#","#","#","#","#"],
                 ["#","T","#","#","#","#"],
                 ["#",".",".","B",".","#"],
                 ["#","#","#","#",".","#"],
                 ["#",".",".",".","S","#"],
                 ["#","#","#","#","#","#"]]
    输出：-1
    示例 3：
    输入：grid = [["#","#","#","#","#","#"],
                 ["#","T",".",".","#","#"],
                 ["#",".","#","B",".","#"],
                 ["#",".",".",".",".","#"],
                 ["#",".",".",".","S","#"],
                 ["#","#","#","#","#","#"]]
    输出：5
    解释：向下、向左、向左、向上再向上。
    示例 4：
    输入：grid = [["#","#","#","#","#","#","#"],
                 ["#","S","#",".","B","T","#"],
                 ["#","#","#","#","#","#","#"]]
    输出：-1
    提示：
    1 <= grid.length <= 20
    1 <= grid[i].length <= 20
    grid 仅包含字符 '.', '#',  'S' , 'T', 以及 'B'。
    grid 中 'S', 'B' 和 'T' 各只能出现一个。
    """
    @timeit
    def minPushBox(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        vis = {}
        box = []
        des = []
        start = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'S':
                    start = [(i, j), 0]
                if grid[i][j] == 'B':
                    box = (i, j)
                if grid[i][j] == 'T':
                    des = (i, j)
        stk = [(start, box, 0)]
        dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def near(i, j, bi, bj):
            for dx, dy in dxy:
                a, b = i + dx, j + dy
                if (a, b) == (bi, bj): return dx, dy
        while stk:
            start, box, step = stk.pop()
            if box == des: return step
            vis[(start, box)] = True
            nr = near(*start, *box)
            si, sj = start
            bi, bj = box
            for dx, dy in dxy:
                sx, sy = si + dx, sj + dy
                if nr and (dx, dy) == nr:
                    bx, by = bi + dx, bj + dy
                else:
                    if 0 <= sx < n and 0 <= sy < m and not (sx, sy, bi, bj):
                        stk.insert(0, [(x, y), step + 1])
        return -1


if __name__ == '__main__':
    a = Solution()
    a.minPushBox(grid = [["#","#","#","#","#","#"],
                 ["#","T","#","#","#","#"],
                 ["#",".",".","B",".","#"],
                 ["#","#","#","#",".","#"],
                 ["#",".",".",".","S","#"],
                 ["#","#","#","#","#","#"]])