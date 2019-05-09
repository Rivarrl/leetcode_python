from algorithm_utils import *

# leetcode 简单题 #2

def calPoints(ops):
    """
    682. 棒球比赛
    你现在是棒球比赛记录员。
    给定一个字符串列表，每个字符串可以是以下四种类型之一：
    1.整数（一轮的得分）：直接表示您在本轮中获得的积分数。
    2. "+"（一轮的得分）：表示本轮获得的得分是前两轮有效 回合得分的总和。
    3. "D"（一轮的得分）：表示本轮获得的得分是前一轮有效 回合得分的两倍。
    4. "C"（一个操作，这不是一个回合的分数）：表示您获得的最后一个有效 回合的分数是无效的，应该被移除。
    每一轮的操作都是永久性的，可能会对前一轮和后一轮产生影响。
    你需要返回你在所有回合中得分的总和。
    示例 1:
    输入: ["5","2","C","D","+"]
    输出: 30
    解释:
    第1轮：你可以得到5分。总和是：5。
    第2轮：你可以得到2分。总和是：7。
    操作1：第2轮的数据无效。总和是：5。
    第3轮：你可以得到10分（第2轮的数据已被删除）。总数是：15。
    第4轮：你可以得到5 + 10 = 15分。总数是：30。
    示例 2:
    输入: ["5","-2","4","C","D","9","+","+"]
    输出: 27
    解释:
    第1轮：你可以得到5分。总和是：5。
    第2轮：你可以得到-2分。总数是：3。
    第3轮：你可以得到4分。总和是：7。
    操作1：第3轮的数据无效。总数是：3。
    第4轮：你可以得到-4分（第三轮的数据已被删除）。总和是：-1。
    第5轮：你可以得到9分。总数是：8。
    第6轮：你可以得到-4 + 9 = 5分。总数是13。
    第7轮：你可以得到9 + 5 = 14分。总数是27。
    注意：
    输入列表的大小将介于1和1000之间。
    列表中的每个整数都将介于-30000和30000之间。
    :param ops: List[str]
    :return: int
    """
    l = len(ops)
    op = []
    for i in range(l):
        if ops[i] == "C":
            op.pop()
        elif ops[i] == "D":
            op.append(op[-1] * 2)
        elif ops[i] == "+":
            op.append(op[-1] + op[-2])
        else:
            op.append(int(ops[i]))
    return sum(op)


def findLengthOfLCIS(nums):
    """
    674. 最长连续递增序列
    给定一个未经排序的整数数组，找到最长且连续的的递增序列。
    示例 1:
    输入: [1,3,5,4,7]
    输出: 3
    解释: 最长连续递增序列是 [1,3,5], 长度为3。
    尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
    示例 2:
    输入: [2,2,2,2,2]
    输出: 1
    解释: 最长连续递增序列是 [2], 长度为1。
    注意：数组长度不会超过10000。
    :param nums: List[int]
    :return: int
    """
    l = len(nums)
    if l == 0: return 0
    ans, memo = 1, 1
    for i in range(1, l):
        if nums[i] > nums[i-1]:
            memo += 1
        else:
            memo = 1
        if memo > ans:
            ans = memo
    return ans


def getIntersectionNode(headA, headB):
    """
    160. 相交链表
    编写一个程序，找到两个单链表相交的起始节点。
    例如: A = [1,2,3,4,5], B = [6,7,3,4,5], return 3 因为[3,4,5]
    :param headA: ListNode
    :param headB: ListNode
    :return: ListNode
    """
    """
    # 把两个链表拼接为AB和BA比较
    if not headA or not headB: return None
    a, b = headA, headB
    while a!=b:
        a = headB if not a else a.next
        b = headA if not b else b.next
    return a
    """
    # 将较长链表去头后再做比较
    pa, pb = headA, headB
    a, b = 0, 0
    while pa:
        pa = pa.next
        a += 1
    while pb:
        pb = pb.next
        b += 1
    pa, pb = headA, headB
    for i in range(abs(a-b)):
        if a > b: pa = pa.next
        if a < b: pb = pb.next
    while pa!=pb:
        pa = pa.next
        pb = pb.next
    return pa


def reverseList(head):
    """
    206. 反转链表
    反转一个单链表。
    示例:
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL
    进阶:
    你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
    :param head: ListNode
    :return: ListNode
    """
    """
    # 迭代
    stk = []
    while head:
        stk.append(head)
        head = head.next
    if stk:
        head = stk.pop()
        p = head
        while stk:
            p.next = stk.pop()
            p.next.next = None
            p = p.next
    print_list_node(head)
    return head    
    """
    """
    # 迭代
    if not head or not head.next: return head
    p, q = head, head
    while head.next:
        r = q
        q = p.next
        p.next = None if not p.next.next else p.next.next
        q.next = r
    return q
    """
    # 递归
    p = head
    if p and p.next:
        head = reverseList(p.next)
        p.next.next, p.next = p, None
    return head


def findSecondMinimumValue(root):
    """
    671. 二叉树中第二小的节点
    给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。
    给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
    示例 1:
    输入:
        2
       / \
      2   5
         / \
        5   7
    输出: 5
    说明: 最小的值是 2 ，第二小的值是 5 。
    示例 2:
    输入:
        2
       / \
      2   2
    输出: -1
    说明: 最小的值是 2, 但是不存在第二小的值。
    :param root: TreeNode
    :return: int
    """
    def inner(root, memo):
        if root:
            if val < root.val < memo:
                memo = root.val
            memo = min(inner(root.left, memo), inner(root.right, memo))
        return memo
    MAX = 0xffffffff
    if root:
        val = root.val
        res = min(inner(root.left, MAX), inner(root.right, MAX))
        return -1 if res == MAX else res


def trimBST(root, L, R):
    """
    669. 修剪二叉搜索树
    给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。
    示例 1:
    输入:
        1
       / \
      0   2
      L = 1
      R = 2
    输出:
        1
          \
           2
    示例 2:
    输入:
        3
       / \
      0   4
       \
        2
       /
      1
      L = 1
      R = 3
    输出:
          3
         /
       2
      /
     1
    :param root: TreeNode
    :param L: int
    :param R: int
    :return: TreeNode
    """
    p = root
    if p:
        if L <= p.val <= R:
            p.left = trimBST(p.left, L, R)
            p.right = trimBST(p.right, L, R)
        elif p.val < L:
            p = trimBST(p.right, L, R)
        else:
            p = trimBST(p.left, L, R)
    root = p
    return root


if __name__ == '__main__':
    # calPoints(["5","2","C","D","+"])
    # findLengthOfLCIS([2,2,2,2,2])
    # a = construct_list_node([1,2,3,4,5])
    # reverseList(a)
    a = construct_tree_node([2,2,5,None,None,5,7])
    print_tree_node(a)
    print(findSecondMinimumValue(a))
    pass