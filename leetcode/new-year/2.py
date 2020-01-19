# -*- coding: utf-8 -*-
# ======================================
# @File    : 2.py
# @Time    : 1/18/20 12:59 PM
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    def canVillagersWin(self, players: List[str], credibility: List[int]) -> bool:
        stk = sorted([[credibility[i], i] for i in range(len(credibility))])
