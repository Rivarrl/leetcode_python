# -*- coding: utf-8 -*-
# ======================================
# @File    : 218.py
# @Time    : 2019/11/13 10:56
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [218. 天际线问题](https://leetcode-cn.com/problems/the-skyline-problem/)
    """
    @timeit
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        思路：按左右边界分别存储高度并排序，再用一个排序数组来维护当前的高度集合。
        每次遍历时如果出现与上一状态不同的高度时，就说明是一个轮廓点，将它加入结果中。
        """
        import bisect
        if not buildings: return []
        lines = []
        # 用正负区分左右，左负是因为如果某个右边界和右边的楼的左边界重合在x=m处，它们算同一个天际线计算范围。
        # 要让左边界先入数组，这样保证答案里不会出现[m,0]这个不应存在的点
        for x in buildings:
            lines.append([x[0], -x[2]])
            lines.append([x[1], x[2]])
        lines.sort()
        res = []
        # 初始值0，表示底线
        hq = [0]
        # [0,0]点算作第一个点
        last = [0, 0]
        for x in lines:
            # 左边界入数组，右边界出数组
            if x[1] < 0:
                bisect.insort(hq, -x[1])
            else:
                hq.remove(x[1])
            maxh = hq[-1]
            if maxh != last[1]:
                last = [x[0], maxh]
                res.append(last)
        return res


if __name__ == '__main__':
    a = Solution()
    a.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])