# -*- coding: utf-8 -*-
# ======================================
# @File    : 725.py
# @Time    : 2020/12/24 9:48 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [725. 分隔链表](https://leetcode-cn.com/problems/split-linked-list-in-parts/)
    """
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        p = root
        n = 0
        while p:
            n += 1
            p = p.next
        x, y = divmod(n, k)
        res = []
        p = root
        ctr = 0
        while p:
            if ctr % (x + int(y > 0)) == 0:
                if res:
                    t = res[-1]
                    while t.next != p:
                        t = t.next
                    t.next = None
                res.append(p)
                y -= int(ctr > 0)
                ctr = 0
            ctr += 1
            p = p.next
        for i in range(k - len(res)):
            res.append(None)
        return res


if __name__ == '__main__':
    a = Solution()
    x = construct_list_node([1, 2, 3])
    r = a.splitListToParts(x, 5)
    for x in r:
        list_node_print(x)
    x = construct_list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    r = a.splitListToParts(x, 3)
    for x in r:
        list_node_print(x)
