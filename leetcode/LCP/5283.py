# -*- coding: utf-8 -*-
# ======================================
# @File    : 5283.py
# @Time    : 2019/12/15 10:51
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5283. 二进制链表转整数](https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer/)
    """
    @timeit
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = (res << 1) + head.val
            head = head.next
        return res


if __name__ == '__main__':
    a = Solution()
    x= construct_list_node([1,0,1])
    a.getDecimalValue(x)
