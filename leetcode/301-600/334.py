# -*- coding: utf-8 -*-
# ======================================
# @File    : 334.py
# @Time    : 2019/11/26 0:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [334. 递增的三元子序列](https://leetcode-cn.com/problems/increasing-triplet-subsequence/)
    """
    @timeit
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        思路：单调栈，递增，每次遇到比栈中的元素（0或1位）还小的值就将对应元素替换为该值
        """
        stk = []
        for x in nums:
            if not stk or stk[-1] < x:
                stk.append(x)
            else:
                last = -float('inf')
                for i in range(len(stk)):
                    if stk[i] > x > last:
                        stk[i] = x
                        break
                    last = stk[i]
            if len(stk) == 3: return True
        return False


    def increasingTriplet2(self, nums: List[int]) -> bool:
        """
        思路：上面的思路可以发现，过程可以简化成这样：如果新的数来了比最小值小，就替换成最小值，否则去和倒数第二小比，还比它大就返回True
        """
        s1 = s2 = float('inf')
        for x in nums:
            if x <= s1:
                s1 = x
            elif x <= s2:
                s2 = x
            else:
                return True
        return False


if __name__ == '__main__':
    a = Solution()
    a.increasingTriplet([1,2,3,4,5])
    a.increasingTriplet([1,2,1,2,1,2,1,2,1,2])
