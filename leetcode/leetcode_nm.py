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


def nthSuperUglyNumber(n, primes):
    """
    313. 超级丑数
    编写一段程序来查找第 n 个超级丑数。
    超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。
    示例:
    输入: n = 12, primes = [2,7,13,19]
    输出: 32
    解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
    说明:
    1 是任何给定 primes 的超级丑数。
     给定 primes 中的数字以升序排列。
    0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000 。
    第 n 个超级丑数确保在 32 位有符整数范围内。
    :param n: int
    :param primes: List[int]
    :return: int
    """
    """
    # 多指针法 40%
    m = len(primes)
    rec = [0] * m
    res = [1]
    for i in range(n-1):
        res.append(min(primes[j] * res[rec[j]] for j in range(m)))
        for j in range(m):
            if primes[j] * res[rec[j]] == res[-1]:
                rec[j] += 1
    print(res)
    return res[-1]
    """
    # 优先队列 100%
    import heapq
    heap, res, idx, ugly_by_last_prime = [], [0] * n, [0] * len(primes), [0] * n
    res[0] = 1
    for index, val in enumerate(primes):
        heapq.heappush(heap, (val, index))
    for i in range(1, n):
        res[i], k = heapq.heappop(heap)
        ugly_by_last_prime[i] = k
        idx[k] += 1
        while ugly_by_last_prime[idx[k]] > k:
            idx[k] += 1
        heapq.heappush(heap, (primes[k] * res[idx[k]], k))
    return res[-1]


def pathSum(root, sum):
    """
    113. 路径总和 II
    给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
    说明: 叶子节点是指没有子节点的节点。
    示例:
    给定如下二叉树，以及目标和 sum = 22，
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \    / \
            7    2  5   1
    返回:
    [
       [5,4,11,2],
       [5,8,4,5]
    ]
    :param root: TreeNode
    :param sum: int
    :return: List[List[int]]
    """
    def dfs(node, cur, path):
        if not node: return
        if not node.left and not node.right:
            if cur == node.val:
                nonlocal res
                res.append(path + [node.val])
                return
        if node.left:
            dfs(node.left, cur - node.val, path + [node.val])
        if node.right:
            dfs(node.right, cur - node.val, path + [node.val])

    res = []
    dfs(root, sum, [])
    return res


def sortedListToBST(head):
    """
    109. 有序链表转换二叉搜索树
    给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
    本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
    示例:
    给定的有序链表： [-10, -3, 0, 5, 9],
    一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
          0
         / \
       -3   9
       /   /
     -10  5
    :param head: ListNode
    :return: TreeNode
    """
    # 由于链表查找中点的复杂度比数组高, 可以转成数组再操作
    # 快慢指针找中点
    def helper(node):
        if not node: return None
        if not node.next: return TreeNode(node.val)
        last, slow, fast = node, node.next, node.next.next
        while fast and fast.next:
            last, slow, fast = last.next, slow.next, fast.next.next
        last.next = None
        root = TreeNode(slow.val)
        root.left = helper(node)
        root.right = helper(slow.next)
        return root

    return helper(head)


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
    x = construct_list_node([-10,-3,0,5,9])
    y = sortedListToBST(x)
    print(deconstruct_tree_node(y))
    # x = construct_tree_node([5,4,8,11,null,13,4,7,2,null,null,null,null,5,1])
    # pathSum(x, 22)
    # nthSuperUglyNumber(12,[2,7,13,19])
    # a = minSteps(100)
    # print(a)
    # x = construct_list_node([1,2,3,4,5])
    # a = reverseBetween(x, 2, 4)
    # print_list_node(a)
    pass