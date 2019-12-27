# -*- coding: utf-8 -*-
# ======================================
# @File    : 1094.py
# @Time    : 2019/12/16 14:32
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1094. 拼车](https://leetcode-cn.com/problems/car-pooling/)
    """
    @timeit
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        同一时刻先下后上，所以把所有时间节点按升序排列，相同时间上车排在下车后
        """
        dtrip = [[0, 0] for _ in range(len(trips) * 2)]
        for i, trip in enumerate(trips):
            p, on, off = trip
            j = len(trips) + i
            dtrip[i][0], dtrip[i][1] = on, p
            dtrip[j][0], dtrip[j][1] = off, -p
        dtrip.sort()
        num = 0
        for o, p in dtrip:
            num += p
            if num > capacity: return False
        return True


if __name__ == '__main__':
    a = Solution()
    a.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4)
    a.carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5)
    a.carPooling(trips = [[2,1,5],[3,5,7]], capacity = 3)
    a.carPooling(trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11)