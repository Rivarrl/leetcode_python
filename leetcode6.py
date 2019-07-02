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
    """
    # 犯规操作，排序数组了
    n = len(nums)
    for i in range(n):
        while nums[i] < n and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    return nums[-1]
    """
    # 类比找循环链表的循环位的题
    res, fast, c = 0, 0, 0
    # 快慢指针找相遇点
    while fast != res or fast == 0:
        res = nums[res]
        fast = nums[nums[fast]]
    # c从起点出发，res从相遇点出发，最终会在循环入口相遇
    while res != c:
        res = nums[res]
        c = nums[c]
    return res


def bstFromPreorder(preorder):
    """
    1008. 先序遍历构造二叉树
    返回与给定先序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。
    (回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，值总 < node.val，而 node.right 的任何后代，值总 > node.val。此外，先序遍历首先显示节点的值，然后遍历 node.left，接着遍历 node.right。）
    示例：
    输入：[8,5,1,7,10,12]
    输出：[8,5,10,1,7,null,12]
    :param preorder: List[int]
    :return: TreeNode
    """
    n = len(preorder)
    if n == 0: return None
    base = preorder[0]
    root = TreeNode(base)
    i = 1
    while i < n and preorder[i] < base:
        i += 1
    left = bstFromPreorder(preorder[1:i])
    right = bstFromPreorder(preorder[i:])
    if left: root.left = left
    if right: root.right = right
    return root


def inorderTraversal(root):
    """
    94. 二叉树的中序遍历
    给定一个二叉树，返回它的中序 遍历。
    示例:
    输入: [1,null,2,3]
       1
        \
         2
        /
       3
    输出: [1,3,2]
    进阶: 递归算法很简单，你可以通过迭代算法完成吗？
    :param root: TreeNode
    :return: List[int]
    """
    """
    # 递归
    def helper(p):
        if p:
            helper(p.left)
            res.append(p.val)
            helper(p.right)
    res = []
    helper(root)
    print(res)
    return res
    """
    # 迭代
    res = []
    if root:
        stk, p = [], root
        while stk or p:
            if p:
                stk.append(p)
                p = p.left
            else:
                p = stk.pop()
                res.append(p.val)
                p = p.right
    print(res)
    return res


def containsNearbyAlmostDuplicate(nums, k, t):
    """
    220. 存在重复元素 III
    给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。
    示例 1:
    输入: nums = [1,2,3,1], k = 3, t = 0
    输出: true
    示例 2:
    输入: nums = [1,0,1,1], k = 1, t = 2
    输出: true
    示例 3:
    输入: nums = [1,5,9,1,5,9], k = 2, t = 3
    输出: false
    :param nums: List[int]
    :param k: int
    :param t: int
    :return: bool
    """
    pass


def nthUglyNumber(n):
    """
    264. 丑数 II
    编写一个程序，找出第 n 个丑数。
    丑数就是只包含质因数 2, 3, 5 的正整数。
    示例:
    输入: n = 10
    输出: 12
    解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
    说明:  
    1 是丑数。
    n 不超过1690。
    :param n: int
    :return: int
    """
    pass


def bulbSwitch(n):
    """
    319. 灯泡开关
    初始时有 n 个灯泡关闭。 第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。 第 3 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。第 i 轮，每 i 个灯泡切换一次开关。 对于第 n 轮，你只切换最后一个灯泡的开关。 找出 n 轮后有多少个亮着的灯泡。
    示例:
    输入: 3
    输出: 1
    解释:
    初始时, 灯泡状态 [关闭, 关闭, 关闭].
    第一轮后, 灯泡状态 [开启, 开启, 开启].
    第二轮后, 灯泡状态 [开启, 关闭, 开启].
    第三轮后, 灯泡状态 [开启, 关闭, 关闭].
    你应该返回 1，因为只有一个灯泡还亮着。
    :param n: int
    :return: int
    """
    pass


def maximalSquare(matrix):
    """
    221. 最大正方形
    在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
    示例:
    输入:
    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0
    输出: 4
    :param matrix: List[List[str]]
    :return: int
    """
    """
    # 暴力迭代 5%
    a = 0
    n = len(matrix)
    if n == 0: return 0
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            matrix[i][j] = int(matrix[i][j])
            if matrix[i][j] == 1:
                a = 1
    if a == 0: return 0
    flag = True
    while flag:
        flag = False
        for i in range(n-a):
            for j in range(m-a):
                matrix[i][j] *= (matrix[i+1][j] * matrix[i][j+1] * matrix[i+1][j+1])
                if matrix[i][j] == 1:
                    flag = True
        a += 1
    return (a-1) ** 2
    """
    # 动态规划
    n = len(matrix)
    if n == 0: return 0
    m = len(matrix[0])
    dp = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '1':
                dp[i][j] = 1
                ans = 1
            else:
                dp[i][j] = 0
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                ans = max(ans,  dp[i][j])
    print(ans)
    return ans ** 2


def allPossibleFBT(N):
    """
    894. 所有可能的满二叉树
    满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。
    返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。
    答案中每个树的每个结点都必须有 node.val=0。
    你可以按任何顺序返回树的最终列表。
    示例：
    输入：7
    输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
    :param N: int
    :return: List[TreeNode]
    """
    """
    # 回溯法 较慢 36%
    def dfs(N):
        if N % 2 == 0: return []
        if N == 1: return [TreeNode(0)]
        res = []
        for i in range(1, N):
            if i % 2 == 1:
                j = N - i - 1
                for l in dfs(i):
                    for r in dfs(j):
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        res.append(root)
        return res
    return dfs(N)
    """
    # 动态规划 T(7) = [left(5) + right(1)] + [left(3) + right(3)]
    # 由题意，N<=20
    def dfs(N):
        if res[N]:
            return res[N]
        if N == 1:
            root = TreeNode(0)
            res[N] = [root]
        elif N % 2 == 1:
            for l in range(1, N):
                if l % 2 == 1:
                    r = N - l - 1
                    for left in dfs(l):
                        for right in dfs(r):
                            root = TreeNode(0)
                            root.left = left
                            root.right = right
                            if res[N] == 0:
                                res[N] = []
                            res[N].append(root)
        return res[N]
    if N % 2 == 0: return []
    res = [0] * 21
    dfs(N)
    return res[N]


def flatten(root):
    """
    114. 二叉树展开为链表
    给定一个二叉树，原地将它展开为链表。
    例如，给定二叉树
        1
       / \
      2   5
     / \   \
    3   4   6
    将其展开为：
    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
    :param root: TreeNode
    :return: None
    """
    if root:
        temp = root.right
        flatten(root.left)
        flatten(root.right)
        root.right, root.left = root.left, None
        if temp:
            while root.right:
                root = root.right
            root.right = temp


if __name__ == '__main__':
    x = construct_tree_node([1,null,2,null,null,3])
    flatten(x)
    print(deconstruct_tree_node(x))
    # allPossibleFBT(7)
    # maximalSquare([["1", "1", "1", "1", "0"],
    #                ["1", "1", "1", "1", "1"],
    #                ["1", "1", "1", "1", "1"],
    #                ["1", "1", "1", "1", "1"]])
    # x = construct_tree_node([1, null, 2, null, null, 3, null])
    # inorderTraversal(x)
    # findDuplicate([1,3,4,2,2])
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