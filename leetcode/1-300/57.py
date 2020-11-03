# -*- coding: utf-8 -*-
# ======================================
# @File    : 57.py
# @Time    : 2020/11/4 0:01
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [57. 插入区间](https://leetcode-cn.com/problems/insert-interval/)
    """
    @timeit
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        i = 0
        x, y = newInterval
        while i < n and intervals[i][1] < x:
            res.append(intervals[i])
            i += 1
        if i == n:
            res.append(newInterval)
            return res
        while i < n and intervals[i][0] <= y:
            cur = [min(intervals[i][0], x), max(intervals[i][1], y)]
            if res:
                if res[-1][1] < intervals[i][0]:
                    res.append(cur)
                else:
                    res[-1] = [res[-1][0], max(intervals[i][1], y)]
            else:
                res.append(cur)
            i += 1
        if not res or res[-1][1] < x:
            res.append(newInterval)
        while i < n and intervals[i][0] > y:
            res.append(intervals[i])
            i += 1
        return res

    def insert2(self, intervals, newInterval):
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)

        if not placed:
            ans.append([left, right])
        return ans

if __name__ == '__main__':
    a = Solution()
    a.insert(intervals = [[1,3],[6,9]], newInterval = [2,5])
    a.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8])