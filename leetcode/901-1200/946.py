# -*- coding: utf-8 -*-
# ======================================
# @File    : 946.py
# @Time    : 2020/5/7 12:45
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [946. 验证栈序列](https://leetcode-cn.com/problems/validate-stack-sequences/)
    """
    @timeit
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(popped)
        j = 0
        stk = []
        for i in range(n):
            if stk and stk[-1] == popped[i]:
                stk.pop()
            else:
                while j < n and pushed[j] != popped[i]:
                    stk.append(pushed[j])
                    j += 1
                j += 1
        return len(stk) == 0

    @timeit
    def validateStackSequences2(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        j = 0
        for x in pushed:
            stk.append(x)
            while stk and stk[-1] == popped[j]:
                stk.pop()
                j += 1
        return not stk

if __name__ == '__main__':
    a = Solution()
    a.validateStackSequences2(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1])
    a.validateStackSequences2(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2])