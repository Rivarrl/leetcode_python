# -*- coding: utf-8 -*-
# ======================================
# @File    : 421.py
# @Time    : 2019/11/15 10:30
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [421. 数组中两个数的最大异或值](https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array)
    """
    @timeit
    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        思路：贪心算法，从高位到低位
        先把1作为当前位的答案，再用当前前缀的数值和其他nums中的前缀数做异或，能在前缀表中找到异或结果的话，说明这一位可以是1
        """
        mask = res = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            pre = set()
            for x in nums:
                pre.add(mask & x)
            # res的每一位都先假设是1
            tmp = res | (1 << i)
            for x in pre:
                # 利用性质：a^b=c, a^c=b, b^c=a
                if x ^ tmp in pre:
                    res = tmp
                    break
        return res


if __name__ == '__main__':
    a = Solution()
    x = [3, 10, 5, 25, 2, 8]
    a.findMaximumXOR(x)