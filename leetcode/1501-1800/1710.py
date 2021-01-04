# -*- coding: utf-8 -*-
# ======================================
# @File    : 1710.py
# @Time    : 2021/1/4 22:33
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1710. 卡车上的最大单元数](https://leetcode-cn.com/problems/maximum-units-on-a-truck/)
    """
    @timeit
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        res = 0
        for box, unit in boxTypes:
            if truckSize - box >= 0:
                truckSize -= box
                res += box * unit
            else:
                res += truckSize * unit
                break
        return res


if __name__ == '__main__':
    a = Solution()
    a.maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4)
    a.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10)