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


def minSteps(n):
    """
    650. 只有两个键的键盘
    最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：
    Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。
    Paste (粘贴) : 你可以粘贴你上一次复制的字符。
    给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。
    示例 1:
    输入: 3
    输出: 3
    解释:
    最初, 我们只有一个字符 'A'。
    第 1 步, 我们使用 Copy All 操作。
    第 2 步, 我们使用 Paste 操作来获得 'AA'。
    第 3 步, 我们使用 Paste 操作来获得 'AAA'。
    说明:
    n 的取值范围是 [1, 1000] 。
    :param n: int
    :return: int
    """
    if n == 1: return 0
    ans = 0
    i = 2
    while n > 1:
        while n % i == 0:
            ans += i
            n /= i
        i += 1
    return ans


def lastStoneWeightII(stones):
    """
    1049. 最后一块石头的重量 II
    有一堆石头，每块石头的重量都是正整数。
    每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
    如果 x == y，那么两块石头都会被完全粉碎；
    如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
    最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。
    示例：
    输入：[2,7,4,1,8,1]
    输出：1
    解释：
    组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
    组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
    组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
    组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
    提示：
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
    :param stones: List[int]
    :return: int
    """
    pass


if __name__ == '__main__':
    # a = minSteps(100)
    # print(a)
    # x = construct_list_node([1,2,3,4,5])
    # a = reverseBetween(x, 2, 4)
    # print_list_node(a)
    pass