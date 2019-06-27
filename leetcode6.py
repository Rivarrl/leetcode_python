# -*- coding:utf-8 -*-
from algorithm_utils import *

# leetcode 6

def partition(head, x):
    """
    86. 分隔链表
    给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
    你应当保留两个分区中每个节点的初始相对位置。
    示例:
    输入: head = 1->4->3->2->5->2, x = 3
    输出: 1->2->2->4->3->5
    :param head: ListNode
    :param x: int
    :return: ListNode
    """
    p = ListNode(-float("inf"))
    p.next = head
    p2 = p
    q = p
    while p and p.val < x:
        q = p
        p = p.next
    while p and p.next:
        if p.next.val >= x:
            p = p.next
            continue
        r = p.next
        p.next = r.next if r.next else None
        r.next, q.next = q.next, r
        q = q.next if q.next else None
    return p2.next


def kthSmallest(matrix, k):
    """
    378. 有序矩阵中第K小的元素
    给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
    请注意，它是排序后的第k小元素，而不是第k个元素。
    示例:
    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ],
    k = 8,
    返回 13。
    说明:
    你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n2 。
    :param matrix: List[List[int]]
    :param k: int
    :return: int
    """
    """
    # 暴力超时
    n = len(matrix)
    pos = [0] * n
    res = 0
    while k > 0:
        cur, p = float("inf"), 0
        for i, x in enumerate(pos):
            if x < n and matrix[i][x] < cur:
                cur = matrix[i][x]
                p = i
        pos[p] += 1
        k -= 1
        res = cur
    return res
    """
    # 二分查找
    def helper(cur):
        ctr, j = 0, n-1
        for i in range(n):
            while j >= 0 and matrix[i][j] > cur:
                j -= 1
            ctr += j + 1
        return ctr

    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0: return -1
    n = len(matrix)
    l, r = matrix[0][0], matrix[-1][-1]
    while l < r:
        m = l + (r - l >> 1)
        ctr = helper(m)
        if ctr < k:
            l = m + 1
        else:
            r = m
    return l


def postorderTraversal(root):
    """
    145. 二叉树的后序遍历
    给定一个二叉树，返回它的 后序 遍历。
    示例:
    输入: [1,null,2,3]
       1
        \
         2
        /
       3
    输出: [3,2,1]
    进阶: 递归算法很简单，你可以通过迭代算法完成吗？
    :param root: TreeNode
    :return: List[int]
    """
    """
    # 递归
    def helper(p):
        if p:
            helper(p.p)
            helper(p.right)
            res.append(p.val)
    res = []
    helper(root)
    return res
    """
    """
    # 迭代 倒排
    res = []
    if root:
        stk = [root]
        while stk:
            root = stk.pop()
            if root.left:
                stk.append(root.left)
            if root.right:
                stk.append(root.right)
            res.append(root.val)
    return res[::-1]
    """
    # 迭代 记录访问位置
    res = []
    if root:
        stk = []
        p, q = root, None
        while stk or p:
            if p:
                stk.append(p)
                p = p.left
            else:
                p = stk[-1]
                if not p.right or p.right == q:
                    res.append(p.val)
                    q = p
                    stk.pop()
                    p = None
                else:
                    p = p.right
    return res


def findDuplicate(nums):
    """
    287. 寻找重复数
    给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
    示例 1:
    输入: [1,3,4,2,2]
    输出: 2
    示例 2:
    输入: [3,1,3,4,2]
    输出: 3
    说明：
    不能更改原数组（假设数组是只读的）。
    只能使用额外的 O(1) 的空间。
    时间复杂度小于 O(n^2) 。
    数组中只有一个重复的数字，但它可能不止重复出现一次。
    :param nums: List[int]
    :return: int
    """
    # 犯规操作，排序数组了
    n = len(nums)
    for i in range(n):
        while nums[i] < n and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    return nums[-1]


if __name__ == '__main__':
    findDuplicate([1,3,4,2,2])
    # x = construct_tree_node([1,null, 2, null, null, 3, null])
    # print(postorderTraversal(x))
    # x = construct_list_node([-8,-7,7,5,3,-7,-8,-1,9,-2,4,6,-4,-1,3,0,4,-8,-8,-8,8,6,-4,-4])
    # partition(x, 0)
    # kthSmallest(matrix = [
    #    [ 1,  5,  9],
    #    [10, 11, 13],
    #    [12, 13, 15]
    # ],
    # k = 8)
    pass