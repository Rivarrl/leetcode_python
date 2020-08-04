# -*- coding: utf-8 -*-
# ======================================
# @File    : 1224.py
# @Time    : 2019/11/18 11:44
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [1224. 最大相等频率](https://leetcode-cn.com/problems/maximum-equal-frequency/)
    """
    @timeit
    def maxEqualFreq(self, nums: List[int]) -> int:
        """
        思路：满足题意的四种情况：
        1. 一个数出现n次（如：1111）
        2. n个数每个出现1次（如：1234）
        3. 删除了较多（比其他数字次数多1）次数的那个数（如：1122333）
        4. 删除了多余的1次的数（如：1122334）
        需要用两个字典解题，一个用来记录数字的出现频率，另一个用来统计同一频率的个数
        """
        from collections import defaultdict
        # freq[i]: i的频率，tot[n]:频率为n的数有几个
        freq, tot = defaultdict(int), defaultdict(int)
        a = 0
        res = 0
        for i, x in enumerate(nums):
            freq[x] += 1
            tot[freq[x]] += 1
            a = max(a, freq[x])
            # case 1 && case 3 || case 4
            if tot[a] == 1 and tot[a-1] * (a-1) + 1 == i + 1 or tot[a] * a + 1 == i + 1:
                res = i + 1
        # case 2
        if a == 1: return len(nums)
        return res


if __name__ == '__main__':
    a = Solution()
    # case 1
    a.maxEqualFreq([1,1,1,1,1,1,1])
    a.maxEqualFreq([10,2,8,9,3,8,1,5,2,3,7,6])
    a.maxEqualFreq([2,2,1,1,5,3,3,5])
    a.maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5])