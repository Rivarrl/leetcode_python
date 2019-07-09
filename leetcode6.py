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


def connect(root):
    """
    116. 填充每个节点的下一个右侧节点指针
    给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
    填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
    初始状态下，所有 next 指针都被设置为 NULL。
    :param root: NextNode
    :return: NextNode
    """
    """
    # 层序遍历 慢 适用于Ⅱ
    if root:
        stk = [root]
        while stk:
            cur = []
            stk.append(None)
            for i in range(len(stk)-2, -1, -1):
                stk[i].next = stk[i+1]
                if stk[i].right:
                    cur.insert(0, stk[i].right)
                if stk[i].left:
                    cur.insert(0, stk[i].left)
            stk = cur[:]
    return root
    """
    """
    # 非递归
    if not root:
        return None
    cur = root
    next = cur.left
    while cur.left:
        cur.left.next = cur.right
        if cur.next:
            cur.right.next = cur.next.left
            cur = cur.next
        else:
            cur = next
            next = cur.left
    return root
    """
    # 利用完美二叉树的数据结构
    def helper(root):
        # 完全二叉树没有左子就一定没有右子
        if not root or not root.left:
            return
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        helper(root.left)
        helper(root.right)
    helper(root)
    return root


def connect2(root):
    """
    117. 填充每个节点的下一个右侧节点指针 II
    接上题，完全二叉树变为普通二叉树
    :param root: NextNode
    :return: NextNode
    """

    def helper(root):
        if not root or not (root.left or root.right):
            return
        last = root.right if root.right else root.left
        if last:
            if last == root.right and root.left:
                root.left.next = root.right
            p = root.next
            while p and not (p.left or p.right):
                p = p.next
            if p:
                last.next = p.left if p.left else p.right
        helper(root.right)
        helper(root.left)
    helper(root)
    return root


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
    # 三指针法
    res = [1]
    i2, i3, i5 = 0, 0, 0
    for i in range(n - 1):
        res.append(min(res[i2] * 2, res[i3] * 3, res[i5] * 5))
        if res[-1] == res[i2] * 2:
            i2 += 1
        if res[-1] == res[i3] * 3:
            i3 += 1
        if res[-1] == res[i5] * 5:
            i5 += 1
    return res[-1]


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
    """
    # 找规律的过程
    for i in range(1, 1001):
        dp = [0] * i
        for j in range(1, i+1):
            if j == 1:
                dp = [1] * i
            else:
                for k in range(i):
                    if (k + 1) % j == 0:
                        dp[k] = int(not dp[k])
        print(i, dp.count(1))
    """
    # return int(n**0.5)


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
    """
    # 普通做法，超时
    n = len(nums)
    if n < 2: return False
    for j in range(1, k+1):
        for i in range(n-j):
            if abs(nums[i] - nums[i+j]) <= t:
                return True
    return False
    """
    # 记录位置并排序 20%
    n = len(nums)
    if n < 2: return False
    arr = sorted([[x, i] for i, x in enumerate(nums)])
    for i in range(n):
        for j in range(i+1, n):
            if arr[j][0] - arr[i][0] > t:
                break
            if abs(arr[i][1] - arr[j][1]) <= k:
                return True
    return False


def maxSlidingWindow(nums, k):
    """
    239. 滑动窗口最大值
    给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。
    返回滑动窗口最大值。
    示例:
    输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
    输出: [3,3,5,5,6,7]
    解释:
      滑动窗口的位置                最大值
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7
    注意：
    你可以假设 k 总是有效的，1 ≤ k ≤ 输入数组的大小，且输入数组不为空。
    进阶：
    你能在线性时间复杂度内解决此题吗？
    :param nums: List[int]
    :param k: int
    :return: List[int]
    """
    """
    # 使用cur当作窗口，内部排序 O(k*n) 18%
    n = len(nums)
    res = []
    if n == 0: return res
    cur = sorted(nums[:k])
    res.append(cur[-1])
    for i in range(n-k):
        j = i + k
        cur.remove(nums[i])
        cur.append(nums[j])
        cur.sort()
        res.append(cur[-1])
    print(res)
    return res
    """
    """
    # 使用双向队列的思想，每次队列中只保留对下一步有意义的数(不大于当前值的数) 56%
    n = len(nums)
    if n == 0: return []
    cur, res = [], [0] * (n - k + 1)
    for i in range(n):
        while cur and nums[cur[-1]] <= nums[i]:
            cur.pop()
        cur.append(i)
        if cur[0] <= i - k:
            cur = cur[1:]
        if i - k + 1 >= 0:
            res[i-k+1] = nums[cur[0]]
    return res
    """
    # 直接用max函数 94%
    n = len(nums)
    res = []
    if n == 0: return res
    m = max(nums[:k])
    res.append(m)
    for i in range(n - k):
        j = i + k
        if nums[i] == m:
            m = max(nums[i + 1:j + 1])
        else:
            m = max(m, nums[j])
        res.append(m)
    return res


def canTransform(start, end):
    """
    777. 在LR字符串中交换相邻字符
    在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。
    示例 :
    输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
    输出: True
    解释:
    我们可以通过以下几步将start转换成end:
    RXXLRXRXL ->
    XRXLRXRXL ->
    XRLXRXRXL ->
    XRLXXRRXL ->
    XRLXXRRLX
    注意:
    1 <= len(start) = len(end) <= 10000。
    start和end中的字符串仅限于'L', 'R'和'X'。
    :param start: str
    :param end: str
    :return: bool
    """
    ns, ne = len(start), len(end)
    if ns != ne: return False
    for x in ["R", "L", "X"]:
        if start.count(x) != end.count(x):
            return False
    if start.replace("X", "") != end.replace("X", ""):
        return False
    s, e = 0, 0
    while s < ns and e < ne:
        while s < ns and start[s] == 'X':
            s += 1
        while e < ne and end[e] == 'X':
            e += 1
        if s == ns and e == ne:
            break
        if (start[s] == 'L' and s < e) or (start[s] == 'R' and s > e):
            return False
        s += 1
        e += 1
    return True


def longestIncreasingPath(matrix):
    """
    329. 矩阵中的最长递增路径
    给定一个整数矩阵，找出最长递增路径的长度。
    对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
    示例 1:
    输入: nums =
    [
      [9,9,4],
      [6,6,8],
      [2,1,1]
    ]
    输出: 4
    解释: 最长递增路径为 [1, 2, 6, 9]。
    示例 2:
    输入: nums =
    [
      [3,4,5],
      [3,2,6],
      [2,2,1]
    ]
    输出: 4
    解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
    :param matrix: List[List[int]]
    :return: int
    """
    """
    # 带记录的dfs 90%
    n = len(matrix)
    if n == 0: return 0
    m = len(matrix[0])
    visited = [[0] * m for _ in range(n)]
    xy = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def dfs(i, j):
        if visited[i][j] > 0:
            return visited[i][j]
        cur = 0
        for x, y in xy:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > matrix[i][j]:
                cur = max(cur, dfs(ni, nj))
        visited[i][j] = cur + 1
        return visited[i][j]

    ans = 1
    for i in range(n):
        for j in range(m):
            ans = max(ans, dfs(i, j))
    print(ans)
    return ans
    """
    """
    # 大佬简化版
    matrix = {i + j * 1j: val
              for i, row in enumerate(matrix)
              for j, val in enumerate(row)}
    length = {}

    for z in sorted(matrix, key=matrix.get):
        length[z] = 1 + max([length[Z]
                             for Z in [z + 1, z - 1, z + 1j, z - 1j]
                             if Z in matrix and matrix[z] > matrix[Z]]
                            or [0])
    return max(length.values() or [0])
    """
    # 先排序再动态规划 57%
    if not matrix or not matrix[0]:
        return 0
    n, m = len(matrix), len(matrix[0])
    arr = sorted([[matrix[i][j], i, j] for j in range(m) for i in range(n)], key=lambda x:x[0])
    xy = ((0, 1), (1, 0), (0, -1), (-1, 0))
    dp = [[1] * m for _ in range(n)]
    ans = 1
    for val, i, j in arr:
        for di, dj in xy:
            x, y = i + di, j + dj
            # 这里要用大于，因为从小到大遍历
            if 0 <= x < n and 0 <= y < m and val > matrix[x][y]:
                dp[i][j] = max(dp[x][y] + 1, dp[i][j])
                ans = max(dp[i][j], ans)
    return ans


def candy(ratings):
    """
    135. 分发糖果
    老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
    你需要按照以下要求，帮助老师给这些孩子分发糖果：
    每个孩子至少分配到 1 个糖果。
    相邻的孩子中，评分高的孩子必须获得更多的糖果。
    那么这样下来，老师至少需要准备多少颗糖果呢？
    示例 1:
    输入: [1,0,2]
    输出: 5
    解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
    示例 2:
    输入: [1,2,2]
    输出: 4
    解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
    第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
    :param ratings: List[int]
    :return: int
    """
    """
    # 贪心，正反遍历两次，正序找单增序列，反序找单减序列 20%
    n = len(ratings)
    dp = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            dp[i] = dp[i-1] + 1
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            dp[i] = max(dp[i], dp[i+1] + 1)
    return sum(dp)
    """
    """
    # 利用等差数列求和，保存上一个峰值 94%
    if not ratings:
        return 0
    ratings.append(999999)
    state=1
    start=end=0
    result=1
    last=1
    for i in range(1,len(ratings)):
        if ratings[i]>=ratings[i-1]:
            if state==-1:
                if start !=end:
                    if end-start+1>last:
                        result-=last
                        result+=end-start+1
                    result+=int((end-start+1)*(end-start)/2)
                    last=1
            if ratings[i]>ratings[i-1]:
                result+=last+1
                last+=1
            else:
                result+=1
                last=1
            start=end=i
            state=1
        else:
            end=i
            state=-1
    return result-last
    """
    # 100% 升序累加，降序单独累加，到再次变为升序处加到结果中
    if not ratings:
        return 0
    result = 0
    decreasing_length = 0
    prev_candies = 2
    prev_rating = ratings[0]
    peak_candies = -1
    second_candies = 0
    for rating in ratings:
        if rating < prev_rating:
            if peak_candies == -1:
                peak_candies = prev_candies
            if prev_candies > 1:
                result += 1
                decreasing_length = 1
            else:
                result += decreasing_length + 1
                decreasing_length += 1
            second_candies += 1
            if peak_candies == second_candies + 1:
                decreasing_length += 1
            prev_rating = rating
            prev_candies = 1
        elif rating > prev_rating:
            peak_candies = -1
            second_candies = 0
            result += prev_candies + 1
            prev_candies += 1
            decreasing_length = 1
            prev_rating = rating
        else:
            peak_candies = -1
            second_candies = 0
            result += 1
            prev_candies = 1
            decreasing_length = 1
            prev_rating = rating
    return result


def maximumGap(nums):
    """
    164. 最大间距
    给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
    如果数组元素个数小于 2，则返回 0。
    示例 1:
    输入: [3,6,9,1]
    输出: 3
    解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
    示例 2:
    输入: [10]
    输出: 0
    解释: 数组元素个数小于 2，因此返回 0。
    说明:
    你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
    请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
    :param nums: List[int]
    :return: int
    """
    # 先实现，强行sort后找最大间距  72%
    nums.sort()
    ans = 0
    for i in range(1, len(nums)):
        ans = max(nums[i] - nums[i - 1], ans)
    return ans


def longestConsecutive(nums):
    """
    128. 最长连续序列
    给定一个未排序的整数数组，找出最长连续序列的长度。
    要求算法的时间复杂度为 O(n)。
    示例:
    输入: [100, 4, 200, 1, 3, 2]
    输出: 4
    解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
    :param nums: List[int]
    :return: int
    """
    # 先实现，强行sort后照最长序列  25%
    if not nums: return 0
    nums.sort()
    ans, cur = 1, 1
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == 1:
            cur += 1
        elif nums[i] - nums[i-1] > 1:
            cur = 1
        else:
            continue
        ans = max(cur, ans)
    return ans


if __name__ == '__main__':
    candy([2,3,5,4,6,2,1,0,2,5,3,4])
    # longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
    # print(canTransform("XXXXXLXXXX", "LXXXXXXXXX"))
    # maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
    # print(containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3))
    # bulbSwitch(3)
    # nthUglyNumber(10)
    # x = construct_tree_node([1,null,2,null,null,3])
    # flatten(x)
    # print(deconstruct_tree_node(x))
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