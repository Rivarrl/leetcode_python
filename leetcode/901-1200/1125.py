# -*- coding: utf-8 -*-
# ======================================
# @File    : 1125.py
# @Time    : 2020/4/20 21:24
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1125. 最小的必要团队](https://leetcode-cn.com/problems/smallest-sufficient-team/)
    """
    @timeit
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # 遍历所有可能
        d = {e:i for i, e in enumerate(req_skills)}
        dp = [[0] * len(people) for _ in range(1 << len(req_skills))]
        dp[0] = []
        for i, sk in enumerate(people):
            pp = 0
            for e in sk:
                pp |= (1 << d[e])
            for k, v in enumerate(dp):
                team = k | pp
                if team != k and len(dp[team]) > len(v) + 1:
                    dp[team] = v + [i]
        return dp[-1]


if __name__ == '__main__':
    a = Solution()
    a.smallestSufficientTeam(req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]])
    a.smallestSufficientTeam(req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]])