# -*- coding: utf-8 -*-
# ======================================
# @File    : 649.py
# @Time    : 2020/12/11 0:10
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [649. Dota2 参议院](https://leetcode-cn.com/problems/dota2-senate/)
    """
    @timeit
    def predictPartyVictory(self, senate: str) -> str:
        if len(set(senate)) == 1: return {"R":"Radiant", "D":"Dire"}[senate[0]]
        r = d = 0 # 分别给对手记着需要被踢掉几个人
        nxt = ''
        for x in senate:
            if x == 'R':
                if r == 0:
                    d += 1
                    nxt += x
                else:
                    r -= 1
            else:
                if d == 0:
                    r += 1
                    nxt += x
                else:
                    d -= 1
        i = 0
        while r > 0:
            while i < len(nxt) and nxt[i] != 'R':
                i += 1
            nxt = nxt[:i] + nxt[i+1:]
            r -= 1
        j = 0
        while d > 0:
            while j < len(nxt) and nxt[j] != 'D':
                j += 1
            nxt = nxt[:j] + nxt[j+1:]
            d -= 1
        return self.predictPartyVictory(nxt)


if __name__ == '__main__':
    a = Solution()
    a.predictPartyVictory("RD")
    a.predictPartyVictory("RDD")
    a.predictPartyVictory("RRR")
    a.predictPartyVictory("RDR")