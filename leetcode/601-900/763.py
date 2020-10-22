# -*- coding: utf-8 -*-
# ======================================
# @File    : 763.py
# @Time    : 2020/10/22 1:32 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [763. 划分字母区间](https://leetcode-cn.com/problems/partition-labels/)
    """
    @timeit
    def partitionLabels(self, S: str) -> List[int]:
        from collections import defaultdict
        d = defaultdict(list)
        for i, c in enumerate(S):
            if c not in d or len(d[c]) == 1:
                d[c].append(i)
            else:
                d[c][-1] = i
        for k, v in d.items():
            if len(v) == 1:
                v.extend(v)
        stk = []
        res = []
        j = -1
        for i, c in enumerate(S):
            if i == d[c][0]:
                stk.append(S[i])
            if i == d[S[i]][1]:
                stk.pop()
                if len(stk) == 0:
                    res.append(i-j)
                    j = i
        return res

if __name__ == '__main__':
    a = Solution()
    a.partitionLabels("ababcbacadefegdehijhklij")