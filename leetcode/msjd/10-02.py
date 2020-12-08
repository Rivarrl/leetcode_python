# -*- coding: utf-8 -*-
# ======================================
# @File    : 10-02.py
# @Time    : 2020/12/8 2:51 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 10.02. 变位词组](https://leetcode-cn.com/problems/group-anagrams-lcci/)
    """
    @timeit
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
        def _sort(s):
            return ''.join(sorted([e for e in s], key=lambda x:ord(x[0])-ord('a')))
        for s in strs:
            c = _sort(s)
            d[c].append(s)
        return list(d.values())

if __name__ == '__main__':
    a = Solution()
    a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])