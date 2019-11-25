# -*- coding: utf-8 -*-
# ======================================
# @File    : 382.py
# @Time    : 2019/11/25 23:58
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import random

class Solution:
    """
    [382. 链表随机节点](https://leetcode-cn.com/problems/linked-list-random-node)
    思路：蓄水池抽样算法
    题目意思：在总长度为N，值很大却不知道总长度的情况下，需要每次随机取值概率均为1/N
    假设在最后一次取值的时候，我们用随机函数randint(1, N)会在[1,N]范围随机取值，每个值的取值概率为1/N
    退到倒数第二次取值，由于取不到最后一个值，也就是在剩余的[1,N-1]的概率的前提下在[1,N-1]中随机取值的概率为
    (1-1/N)*(1/(N-1))=((N-1)/N)*(1/(N-1))= 1/N
    """
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        res = self.head.val
        p = self.head.next
        i = 2
        while p:
            if random.randint(1, i) == 0:
                res = p.val
            i += 1
            p = p.next
        return res

if __name__ == '__main__':
    # Your Solution object will be instantiated and called as such:
    head = construct_list_node([1,2,3])
    obj = Solution(head)
    param_1 = obj.getRandom()
    print(param_1)
