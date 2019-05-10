from algorithm_utils import *
from collections import deque


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


def isPowerOfTwo(n):
    """
    231. 2的幂
    给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
    示例 1:
    输入: 1
    输出: true
    解释: 20 = 1
    示例 2:
    输入: 16
    输出: true
    解释: 24 = 16
    示例 3:
    输入: 218
    输出: false
    :param n: int
    :return: bool
    """
    """
    # 转2进制字符串，形同^0b1[0]*$
    import re
    return re.match("^0b1[0]*$", bin(n))
    """
    """
    # 移位运算，利用整型范围内2的幂的最大值1<<30，如果n是2的幂，n就会被该值整除
    return n > 0 and (1<<30) % n == 0
    """
    """
    # 与运算，2^n二进制与(2^n)-1与后为0，其余值均不为0
    return n > 0 and not n & (n-1)
    """
    # 与运算，2^n的二进制只有1位是1，与其相反数的补码（取反+1）做与运算后仍为2^n
    return n > 0 and n & (-n) == n


def hasCycle(head):
    """
    141. 环形链表
    给定一个链表，判断链表中是否有环。
    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
    示例 1：
    输入：head = [3,2,0,-4], pos = 1
    输出：true
    解释：链表中有一个环，其尾部连接到第二个节点。
    示例 2：
    输入：head = [1,2], pos = 0
    输出：true
    解释：链表中有一个环，其尾部连接到第一个节点。
    示例 3：
    输入：head = [1], pos = -1
    输出：false
    解释：链表中没有环。
    进阶：
    你能用 O(1)（即，常量）内存解决此问题吗？
    :param head: ListNode
    :return: bool
    """
    if head:
        p = head
        while p.next:
            q = p.next
            if q == head: return True
            p.next, q.next = q.next, p
    return False


def hasPathSum(root, sum):
    """
    112. 路径总和
    给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
    说明: 叶子节点是指没有子节点的节点。
    示例:
    给定如下二叉树，以及目标和 sum = 22，
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \      \
            7    2      1
    返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
    :param root: TreeNode
    :param sum: int
    :return: bool
    """
    if root:
        sum -= root.val
        if root.left or root.right:
            return hasPathSum(root.left, sum) | hasPathSum(root.right, sum)
        else:
            return sum == 0
    else:
        return False


def isBalanced(root):
    """
    110. 平衡二叉树
    给定一个二叉树，判断它是否是高度平衡的二叉树。
    本题中，一棵高度平衡二叉树定义为：
    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
    示例 1:
    给定二叉树 [3,9,20,null,null,15,7]
        3
       / \
      9  20
        /  \
       15   7
    返回 true 。
    示例 2:
    给定二叉树 [1,2,2,3,3,null,null,4,4]
           1
          / \
         2   2
        / \
       3   3
      / \
     4   4
    返回 false 。
    :param root: TreeNode
    :return: bool
    """
    def depth(root):
        if not root:
            return 0
        dl, dr = depth(root.left), depth(root.right)
        if abs(dl - dr) > 1:
            ans[-1] = False
        return max(dl, dr) + 1
    ans = [True]
    depth(root)
    return ans[-1]


def sortedArrayToBST(nums):
    """
    108. 将有序数组转换为二叉搜索树
    将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
    本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
    示例:
    给定有序数组: [-10,-3,0,5,9],
    一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
          0
         / \
       -3   9
       /   /
     -10  5
    :param nums: List[int]
    :return: TreeNode
    """
    l = len(nums)
    if l == 0: return None
    if l == 1: return TreeNode(nums[0])
    m = (l - 1) // 2
    root = TreeNode(nums[m])
    root.left = sortedArrayToBST(nums[:m])
    root.right = sortedArrayToBST(nums[m+1:])
    return root


def titleToNumber(s):
    """
    171. Excel表列序号
    给定一个Excel表格中的列名称，返回其相应的列序号。
    例如，
        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28
        ...
    示例 1:
    输入: "A"
    输出: 1
    示例 2:
    输入: "AB"
    输出: 28
    示例 3:
    输入: "ZY"
    输出: 701
    :param s: str
    :return: int
    """
    base = ord('A') - 1
    ans = 0
    for c in s:
        ans = ans * 26 + (ord(c) - base)
    return ans


def convertToTitle(n):
    """
    168. Excel表列名称
    给定一个正整数，返回它在 Excel 表中相对应的列名称。
    例如，
        1 -> A
        2 -> B
        3 -> C
        ...
        26 -> Z
        27 -> AA
        28 -> AB
        ...
    示例 1:
    输入: 1
    输出: "A"
    示例 2:
    输入: 28
    输出: "AB"
    示例 3:
    输入: 701
    输出: "ZY"
    :param n: int
    :return: str
    """
    A = ord('A')
    res = ''
    while n > 0:
        if n % 26 > 0:
            res = chr(A + n % 26 - 1) + res
        else:
            res = 'Z' + res
            if n >= 26:
                n -= 1
        n = n // 26
    return res


def deleteDuplicates(head):
    """
    83. 删除排序链表中的重复元素
    给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
    示例 1:
    输入: 1->1->2
    输出: 1->2
    示例 2:
    输入: 1->1->2->3->3
    输出: 1->2->3
    :param head: ListNode
    :return: ListNode
    """
    if head:
        p, q = head, head.next
        while p:
            while q:
                if q.val == p.val:
                    q = q.next
                else:
                    break
            p.next = q
            p = p.next
    return head


def isSameTree(p, q):
    """
    100. 相同的树
    给定两个二叉树，编写一个函数来检验它们是否相同。
    如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
    示例 1:
    输入:       1         1
              / \       / \
             2   3     2   3
            [1,2,3],   [1,2,3]
    输出: true
    示例 2:
    输入:      1          1
              /           \
             2             2
            [1,2],     [1,null,2]
    输出: false
    示例 3:
    输入:       1         1
              / \       / \
             2   1     1   2
            [1,2,1],   [1,1,2]
    输出: false
    :param p: TreeNode
    :param q: TreeNode
    :return: bool
    """
    if p and q:
        return isSameTree(p.left, q.left) & isSameTree(p.right, q.right) & (p.val == q.val)
    elif not p and not q:
        return True
    else:
        return False


def isSymmetric(root):
    """
    101. 对称二叉树
    给定一个二叉树，检查它是否是镜像对称的。
    例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
        1
       / \
      2   2
       \   \
       3    3
    说明:
    如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
    :param root: TreeNode
    :return: bool
    """
    """
    # 递归 慢
    def lfirst(root):
        if root:
            yield root.val
            yield from lfirst(root.left)
            yield from lfirst(root.right)
        else:
            yield ''
    def rfirst(root):
        if root:
            yield from rfirst(root.left)
            yield from rfirst(root.right)
            yield root.val
        else:
            yield ''
    print(list(lfirst(root)))
    print(list(rfirst(root)))
    return list(lfirst(root)) == list(rfirst(root))[::-1]
    """
    """
    # 递归 快
    def inner(p, q):
        if p and q:
            return inner(p.left, q.right) & inner(p.right, q.left) & (p.val == q.val)
        else:
            return not (p or q)
    if root:
        return inner(root.left, root.right)
    return True
    """
    # 迭代
    stk = [root]
    while stk:
        cur = []
        nxt = []
        for p in stk:
            if not p:
                cur.append(None)
                continue
            nxt.append(p.left)
            nxt.append(p.right)
            cur.append(p.val)
        if cur != cur[::-1]: return False
        stk = nxt
    return True


def getRow(rowIndex):
    """
    119. 杨辉三角 II
    给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
    在杨辉三角中，每个数是它左上方和右上方的数的和。
    示例:
    输入: 3
    输出: [1,3,3,1]
    进阶：
    你可以优化你的算法到 O(k) 空间复杂度吗？
    :param rowIndex: int
    :return: List[int]
    """
    """
    # 迭代
    res = [1]
    for i in range(rowIndex):
        res = list(map(lambda x, y: x + y, [0] + res, res + [0]))
    return res
    """
    """
    # 公式 C(n, i) = n! / (i!*(n-i)!)
    res = [0] * (rowIndex + 1)
    cur = 1
    for i in range(rowIndex + 1):
        res[i] = int(cur)
        cur = cur * (rowIndex - i) / (i+1)
    return res
    """
    # 遍历
    res = [0] * (rowIndex + 1)
    for i in range(rowIndex + 1):
        for j in range(i, -1, -1):
            if j == 0 or j == i:
                res[j] = 1
            else:
                res[j] = res[j] + res[j-1]
    return res


def levelOrderBottom(root):
    """
    107. 二叉树的层次遍历 II
    给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
    例如：
    给定二叉树 [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    返回其自底向上的层次遍历为：
    [
      [15,7],
      [9,20],
      [3]
    ]
    :param root: TreeNode
    :return: List[List[int]]
    """
    stk = [root]
    res = []
    while stk:
        cur = []
        nxt = []
        for p in stk:
            if not p:
                continue
            cur.append(p.val)
            if p.left:
                nxt.append(p.left)
            if p.right:
                nxt.append(p.right)
        if cur:
            res.append(cur)
        stk = nxt
    return res[::-1]


def lowestCommonAncestor(root, p, q):
    """
    235. 二叉搜索树的最近公共祖先
    给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
    百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
    例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
    示例 1:
    输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    输出: 6
    解释: 节点 2 和节点 8 的最近公共祖先是 6。
    示例 2:
    输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    输出: 2
    解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
    说明:
    所有节点的值都是唯一的。
    p、q 为不同节点且均存在于给定的二叉搜索树中。
    :param root: TreeNode
    :param p: int
    :param q: int
    :return: int
    """
    pass



if __name__ == '__main__':
    # print(getRow(4))
    # x = construct_tree_node([1,2,2,3,4,4,3])
    # print(isSymmetric(x))
    # p = construct_tree_node([1,2,3])
    # q = construct_tree_node([1,2,3])
    # print(isSameTree(p, q))
    # x = construct_list_node([1,1,2])
    # r = deleteDuplicates(x)
    # print_list_node(r)
    # print(convertToTitle(676))
    # calPoints(["5","2","C","D","+"])
    # findLengthOfLCIS([2,2,2,2,2])
    # a = construct_list_node([1,2,3,4,5])
    # reverseList(a)
    # a = construct_tree_node([2,2,5,None,None,5,7])
    # print_tree_node(a)
    # print(findSecondMinimumValue(a))
    x = construct_tree_node([3,9,20,None,None,15,7])
    levelOrderBottom(x)
    # x = construct_tree_node([1,2])
    # print(hasPathSum(x, 1))
    pass