# -*- coding: utf-8 -*-
# ======================================
# @File    : 1687.py
# @Time    : 2021/1/15 13:58
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1687. 从仓库到码头运输箱子](https://leetcode-cn.com/problems/delivering-boxes-from-storage-to-ports/)
    """
    @timeit
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:


if __name__ == '__main__':
    a = Solution()
    a.boxDelivering(boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3)
    a.boxDelivering(boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6)
    a.boxDelivering(boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7)
    a.boxDelivering(boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]], portsCount = 5, maxBoxes = 5, maxWeight = 7)