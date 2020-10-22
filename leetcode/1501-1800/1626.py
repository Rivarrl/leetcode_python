# -*- coding: utf-8 -*-
# ======================================
# @File    : 5545.py
# @Time    : 2020/10/18 11:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1626. 无矛盾的最佳球队](https://leetcode-cn.com/problems/best-team-with-no-conflicts/)
    """
    @timeit
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = [[a, s] for a, s in zip(ages, scores)]
        arr.sort()
        n = len(arr)
        dp = [-1] * n
        dp[0] = 0
        for i in range(n):
            dp[i] = arr[i][1]
            for j in range(i):
                if arr[j][1] <= arr[i][1]:
                    dp[i] = max(dp[i], dp[j] + arr[i][1])
        return max(dp)

if __name__ == '__main__':
    a = Solution()
    a.bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5])
    a.bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1])
    a.bestTeamScore(scores = [1,2,3,5], ages = [8,9,10,1])
    a.bestTeamScore([1,1,1,1,1,1,1,1,1,1], [811,364,124,873,790,656,581,446,885,134])
    a.bestTeamScore([9,2,8,8,2], [4,1,3,3,5])
    a.bestTeamScore([1,3,7,3,2,4,10,7,5], [4,5,2,1,1,2,4,1,4])