# -*- coding: utf-8 -*-
# ======================================
# @File    : 1024.py
# @Time    : 2020/10/24 16:58
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1024. 视频拼接](https://leetcode-cn.com/problems/video-stitching/)
    """
    @timeit
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # 贪心
        d = {}
        for x, y in clips:
            d[x] = max(d.get(x, 0), y)
        ks = sorted(d.keys())
        if d[ks[-1]] < T: return -1
        left = right = res = 0
        while right < T:
            l, r = left, right
            for pos in range(left, right+1):
                if pos in d and d[pos] > r:
                    r = d[pos]
                    l = pos
            if l == left and r == right: return -1
            left, right = l, r
            res += 1
        return res


    @timeit
    def videoStitching2(self, clips: List[List[int]], T: int) -> int:
        # dp
        dp = [T+1] * (T+1)
        dp[0] = 0
        for i in range(T+1):
            for l, r in clips:
                if l <= i < r:
                    ri = min(r, T)
                    dp[ri] = min(dp[ri], dp[i] + 1)
        return -1 if dp[T] == T+1 else dp[T]


if __name__ == '__main__':
    a = Solution()
    a.videoStitching2(clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10)
    a.videoStitching2(clips = [[0,1],[1,2]], T = 5)
    a.videoStitching2(clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9)
    a.videoStitching2(clips = [[0,4],[2,8]], T = 5)
    a.videoStitching2([[0, 2], [4, 8]], 5)