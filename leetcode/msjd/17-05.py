# -*- coding: utf-8 -*-
# ======================================
# @File    : 17-05.py
# @Time    : 2020/11/3 12:41 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 17.05.  字母与数字](https://leetcode-cn.com/problems/find-longest-subarray-lcci/)
    """
    @timeit
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        n = len(array)
        pre = {0:0} # i+1
        res = [0,0]
        c = 0
        for i in range(n):
            c += -1 if array[i].isalpha() else 1
            if c in pre:
                if i + 1 - pre[c] > res[1] - res[0]:
                    res = [pre[c], i+1]
            else:
                pre[c] = i + 1
        return array[res[0]:res[1]]

if __name__ == '__main__':
    a = Solution()
    a.findLongestSubarray(["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"])
    a.findLongestSubarray(["A","A"])
    a.findLongestSubarray(["A","1"])
    a.findLongestSubarray(["1","1","A"])