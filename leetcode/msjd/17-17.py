# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-17.py
# @Time    : 2020/11/16 1:36 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.17. 多次搜索](https://leetcode-cn.com/problems/multi-search-lcci)
    """
    @timeit
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        trie = {}
        for i in range(len(big)):
            d = trie
            for c in big[i:]:
                if c not in d:
                    d[c] = [{}, [i]]
                else:
                    d[c][1].append(i)
                d = d[c][0]
        res = [[] for _ in range(len(smalls))]
        for j, small in enumerate(smalls):
            d = trie
            for i, c in enumerate(small):
                if c not in d:
                    break
                if i == len(small) - 1:
                    res[j].extend(d[c][1])
                d = d[c][0]
        return res

if __name__ == '__main__':
    a = Solution()
    a.multiSearch(big = "mississippi", smalls = ["is","ppi","hi","sis","i","ssippi"])