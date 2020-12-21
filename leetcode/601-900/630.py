# -*- coding: utf-8 -*-
# ======================================
# @File    : 630.py
# @Time    : 2020/12/21 7:19 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [630. 课程表 III](https://leetcode-cn.com/problems/course-schedule-iii/)
    """
    @timeit
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # 贪心，按截止时间排序，如果当前的课不能都上，就从已选的课中把时间最长的课取消，用最大堆实现
        import heapq
        courses.sort(key=lambda x: x[1])
        cur = 0
        q = []
        for cost, end in courses:
            cur += cost
            heapq.heappush(q, -cost)
            if cur > end:
                cur += heapq.heappop(q)
        return len(q)

if __name__ == '__main__':
    a = Solution()
    a.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])
    a.scheduleCourse([[5,5],[4,6],[2,6]])