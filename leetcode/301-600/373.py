# -*- coding: utf-8 -*-
# ======================================
# @File    : 373.py
# @Time    : 2020/4/21 22:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    @timeit
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 最大堆或最小堆实现
        # 1 容量为k的最大堆，遍历所有之后得到答案
        # 2 如果将两个数组的笛卡尔积摊开成二维数组，那么答案一定是从左上角向右下角扩散得到
        #   使用最小堆+广度优先搜索
        import heapq
        n, m = len(nums1), len(nums2)
        if n == 0 or m == 0 or k == 0: return []
        q, res = [], []
        heapq.heappush(q, (nums1[0]+nums2[0], (0, 0)))
        vis = [[0] * m for _ in range(n)]
        while q and len(res) < k:
            _, (i, j) = heapq.heappop(q)
            res.append([nums1[i], nums2[j]])
            if i + 1 < n and vis[i+1][j] == 0:
                vis[i+1][j] = 1
                heapq.heappush(q, (nums1[i+1] + nums2[j], (i+1, j)))
            if j + 1 < m and vis[i][j+1] == 0:
                vis[i][j+1] = 1
                heapq.heappush(q, (nums1[i] + nums2[j+1], (i, j+1)))
        return res


if __name__ == '__main__':
    a = Solution()
    a.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3)
    a.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2)
    a.kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3)
    a.kSmallestPairs([1,1,2], [1,2,3], 10)