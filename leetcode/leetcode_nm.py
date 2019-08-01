# -*- coding:utf-8 -*-
from algorithm_utils import *
# leetcode 中等题

def reverseBetween(head, m, n):
    """
    92. 反转链表 II
    反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
    说明:
    1 ≤ m ≤ n ≤ 链表长度。
    示例:
    输入: 1->2->3->4->5->NULL, m = 2, n = 4
    输出: 1->4->3->2->5->NULL
    :param head: ListNode
    :param m: int
    :param n: int
    :return: ListNode
    """
    """
    # 78% 定位两个临界点后再降反转部分反转 O(len(head)+n)
    i = 0
    p = ListNode(0)
    p.next, q = head, p
    while i + 1 < m:
        p = p.next
        i += 1
    p1, p2 = p, p.next
    j = i + 1
    while i <= n:
        p = p.next
        i += 1
    p3 = p
    p = p2
    t = None
    i = j
    while i <= n:
        r = p.next
        p.next = t
        t = p
        if r == None or i == n:
            break
        p = r
        i += 1
    p2.next = p3
    p1.next = p
    return q.next
    """
    # O(n)
    p = ListNode(0)
    p.next = head
    pre = p
    for i in range(1, m):
        pre = pre.next
    head = pre.next
    for j in range(m, n):
        q = head.next
        head.next = q.next
        q.next = pre.next
        pre.next = q
    return p.next


if __name__ == '__main__':
    x = construct_list_node([1,2,3,4,5])
    a = reverseBetween(x, 2, 4)
    print_list_node(a)
    pass