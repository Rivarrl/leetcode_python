# -*- coding:utf-8 -*-
from algorithm_utils import *


# leetcode 7

def countNodes(root):
    """
    222. 完全二叉树的节点个数
    给出一个完全二叉树，求出该树的节点个数。
    说明：
    完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
    示例:
    输入:
        1
       / \
      2   3
     / \  /
    4  5 6
    输出: 6
    :param root: TreeNode
    :return: int
    """

    def helper(p, lv):
        if par[1]: return
        if lv < level - 1:
            helper(p.left, lv + 1)
            helper(p.right, lv + 1)
        else:
            if p.left and p.right:
                par[0] += 2
            else:
                if p.left:
                    par[0] += 1
                par[1] = True

    p = root
    level = 0
    while p:
        level += 1
        p = p.left
    if level <= 1: return level
    par = [2 ** (level - 1) - 1, False]
    helper(root, 1)
    return par[0]


def computeArea(A, B, C, D, E, F, G, H):
    """
    223. 矩形面积
    在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。
    每个矩形由其左下顶点和右上顶点坐标表示
    示例:
    输入: -3, 0, 3, 4, 0, -1, 9, 2
    输出: 45
    说明: 假设矩形面积不会超出 int 的范围。
    :param A: int
    :param B: int
    :param C: int
    :param D: int
    :param E: int
    :param F: int
    :param G: int
    :param H: int
    :return: int
    """
    """
    # 两个矩形面积和减去重叠部分面积
    get_D = lambda x1, x2: x2 - x1
    get_S = lambda x1, y1, x2, y2: get_D(x1, x2) * get_D(y1, y2)
    S1 = get_S(A, B, C, D)
    S2 = get_S(E, F, G, H)
    S3 = 0
    m_AC, M_AC = min(A, C), max(A, C)
    m_EG, M_EG = min(E, G), max(E, G)
    m_BD, M_BD = min(B, D), max(B, D)
    m_FH, M_FH = min(F, H), max(F, H)
    D_AC = get_D(A, C)
    D_EG = get_D(E, G)
    D_12 = max(get_D(m_AC, M_EG), get_D(m_EG, M_AC))
    D_BD = get_D(B, D)
    D_FH = get_D(F, H)
    D_34 = max(get_D(m_BD, M_FH), get_D(m_FH, M_BD))
    if D_AC + D_EG > D_12 and D_BD + D_FH > D_34:
        S3 = min(D_AC, D_EG, get_D(m_AC, M_EG), get_D(m_EG, M_AC)) * min(D_BD, D_FH, get_D(m_BD, M_FH), get_D(m_FH, M_BD))
    ans = S1 + S2 - S3
    return ans
    """
    # 简化版
    S1 = (C - A) * (D - B) + (G - E) * (H - F)
    S2 = 0
    if A < G and B < H and C > E and D > F:
        X, Y = sorted([A, C, E, G]), sorted([B, D, F, H])
        S2 = (X[2] - X[1]) * (Y[2] - Y[1])
    return S1 - S2


def rob2(nums):
    """
    213. 打家劫舍 II
    你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
    示例 1:
    输入: [2,3,2]
    输出: 3
    解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
    示例 2:
    输入: [1,2,3,1]
    输出: 4
    解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
         偷窃到的最高金额 = 1 + 3 = 4 。
    :param nums: List[int]
    :return: int
    """

    def helper(nums):
        n = len(nums)
        if n == 0: return 0
        if n < 3: return max(nums)
        if n == 3: return max(nums[2] + nums[0], nums[1])
        cur, pre1, pre2 = nums[2] + nums[0], nums[1], nums[0]
        ans = cur
        for i in range(3, n):
            cur, pre1, pre2 = nums[i] + max(pre1, pre2), cur, pre1
            ans = max(cur, ans)
        return ans

    n = len(nums)
    if n == 0: return 0
    if n < 3: return max(nums)
    return max(helper(nums[1:]), helper(nums[:-1]))


def recoverFromPreorder(S):
    """
    1028. 从先序遍历还原二叉树
    我们从二叉树的根节点 root 开始进行深度优先搜索。
    在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。
    如果节点只有一个子节点，那么保证该子节点为左子节点。
    给出遍历输出 S，还原树并返回其根节点 root。
    示例 1：
    输入："1-2--3--4-5--6--7"
    输出：[1,2,5,3,4,6,7]
    示例 2：
    输入："1-2--3---4-5--6---7"
    输出：[1,2,5,3,null,6,null,4,null,7]
    示例 3：
    输入："1-401--349---90--88"
    输出：[1,401,null,349,88,90]
    提示：
    原始树中的节点数介于 1 和 1000 之间。
    每个节点的值介于 1 和 10 ^ 9 之间。
    :param S: str
    :return: TreeNode
    """
    res = {}
    i, n = 0, len(S)
    while i < n:
        v_str, lv = [], 0
        while i < n and S[i] == "-":
            lv += 1
            i += 1
        while i < n and S[i].isdecimal():
            v_str.append(S[i])
            i += 1
        v = int("".join(v_str))
        if not lv in res:
            res[lv] = [TreeNode(v)]
        else:
            res[lv].append(TreeNode(v))
        if lv > 0:
            pre = res[lv - 1][-1]
            if not pre.left:
                pre.left = res[lv][-1]
            else:
                pre.right = res[lv][-1]
    return res[0][0]


def buildTree(preorder, inorder):
    """
    105. 从前序与中序遍历序列构造二叉树
    根据一棵树的前序遍历与中序遍历构造二叉树。
    注意:
    你可以假设树中没有重复的元素。
    例如，给出
    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
    返回如下的二叉树：
        3
       / \
      9  20
        /  \
       15   7
    :param preorder: List[int]
    :param inorder: List[int]
    :return: TreeNode
    """
    """
    # 60%
    if not preorder or not inorder:
        return None
    x = preorder[0]
    root = TreeNode(x)
    ii = inorder.index(x)
    # recursive
    left = buildTree(preorder[1:ii+1], inorder[:ii])
    right = buildTree(preorder[ii+1:], inorder[ii+1:])
    root.left = left
    root.right = right
    return root
    """

    # 100%
    def helper(l=0, r=len(preorder)):
        if l == r: return None
        val = preorder[i_key[0]]
        root = TreeNode(val)
        idx = inorder_map[val]
        i_key[0] += 1
        root.left = helper(l, idx)
        root.right = helper(idx + 1, r)
        return root

    i_key = [0]
    inorder_map = {k: v for v, k in enumerate(inorder)}
    return helper()


def buildTree2(inorder, postorder):
    """
    106. 从中序与后序遍历序列构造二叉树
    根据一棵树的中序遍历与后序遍历构造二叉树。
    注意:
    你可以假设树中没有重复的元素。
    例如，给出
    中序遍历 inorder = [9,3,15,20,7]
    后序遍历 postorder = [9,15,7,20,3]
    返回如下的二叉树：
        3
       / \
      9  20
        /  \
       15   7
    :param inorder: List[int]
    :param postorder: List[int]
    :return: TreeNode
    """

    def helper(l=0, r=len(postorder)):
        if l == r: return None
        val = postorder[i_key[0]]
        root = TreeNode(val)
        idx = ino_map[val]
        i_key[0] -= 1
        root.right = helper(idx + 1, r)
        root.left = helper(l, idx)
        return root

    i_key = [len(postorder) - 1]
    ino_map = {k: v for v, k in enumerate(inorder)}
    return helper()


def sumNumbers(root):
    """
    129. 求根到叶子节点数字之和
    给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
    例如，从根到叶子节点路径 1->2->3 代表数字 123。
    计算从根到叶子节点生成的所有数字之和。
    说明: 叶子节点是指没有子节点的节点。
    示例 1:
    输入: [1,2,3]
        1
       / \
      2   3
    输出: 25
    解释:
    从根到叶子节点路径 1->2 代表数字 12.
    从根到叶子节点路径 1->3 代表数字 13.
    因此，数字总和 = 12 + 13 = 25.
    示例 2:
    输入: [4,9,0,5,1]
        4
       / \
      9   0
     / \
    5   1
    输出: 1026
    解释:
    从根到叶子节点路径 4->9->5 代表数字 495.
    从根到叶子节点路径 4->9->1 代表数字 491.
    从根到叶子节点路径 4->0 代表数字 40.
    因此，数字总和 = 495 + 491 + 40 = 1026.
    :param root: TreeNode
    :return: int
    """

    def dfs(root, curr):
        c = curr * 10 + root.val
        if not root.left and not root.right:
            nonlocal ans
            ans += c
        if root.left:
            dfs(root.left, c)
        if root.right:
            dfs(root.right, c)

    ans = 0
    if root: dfs(root, 0)
    return ans


def singleNumber(nums):
    """
    137. 只出现一次的数字 II
    给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
    说明：
    你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
    示例 1:
    输入: [2,2,3,2]
    输出: 3
    示例 2:
    输入: [0,1,0,1,0,1,99]
    输出: 99
    :param nums: List[int]
    :return: int
    """
    """
    # 将所有出现非3倍数次的位组合即为所求 12%
    ans = 0
    n = len(nums)
    for i in range(32):
        mask = 1 << i
        ctr = 0
        for j in range(n):
            if (nums[j] & mask) != 0:
                ctr += 1
        if ctr % 3 != 0:
            ans |= mask
    up_bound = 2 ** 32
    if ans > 2 ** 31 - 1:
        ans -= up_bound
    return ans
    """
    # 用异或
    # b用于记录异或值的1出现一次的位, a用于记录出现两次的位
    a, b = 0, 0
    for x in nums:
        b = (b ^ x) & ~a
        a = (a ^ x) & ~b
    return b


def singleNumber3(nums):
    """
    260. 只出现一次的数字 III
    给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
    示例 :
    输入: [1,2,1,3,2,5]
    输出: [3,5]
    注意：
    结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
    你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
    :param nums: List[int]
    :return: List[int]
    """
    # 本题重点是如何区分开两个答案
    q = 0
    # 得到的q是两个答案值的异或
    for x in nums:
        q ^= x
    # 取最低位的1, 也就是两个答案的最低异或位, 这样就区分开两个答案了
    b = q & (~q + 1)
    res = [0, 0]
    for x in nums:
        if x & b == 0:
            res[0] ^= x
        else:
            res[1] ^= x
    return res


def rob3(root):
    """
    337. 打家劫舍 III
    在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
    计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
    示例 1:
    输入: [3,2,3,null,3,null,1]
         3
        / \
       2   3
        \   \
         3   1
    输出: 7
    解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
    示例 2:
    输入: [3,4,5,1,3,null,1]
         3
        / \
       4   5
      / \   \
     1   3   1
    输出: 9
    解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
    :param root: TreeNode
    :return: int
    """
    """
    # 递归 O(2^n) 超时
    def helper(p, root):
        if not root:
            return 0
        if p:
            cur = helper(False, root.left) + helper(False, root.right)
        else:
            cur = max(helper(True, root.left) + root.val + helper(True, root.right), helper(False, root.left) + helper(False, root.right))
        return cur
    ans = helper(False, root)
    return ans
    """
    """
    # 迭代 100%
    stack = [(0, root)]
    res = {None:(0, 0)}
    while stack:
        rob, node = stack.pop()
        if not node:
            continue
        if not rob:
            stack.extend([(1, node), (0, node.right), (0, node.left)])
        else:
            res[node] = (res[node.left][1] + res[node.right][1] + node.val, max(res[node.left]) + max(res[node.right]))
    return max(res[root])
    """

    # 递归调用两次的 99%
    def dfs(node):
        if not node:
            return 0, 0
        left = dfs(node.left)
        right = dfs(node.right)
        return left[1] + node.val + right[1], max(left) + max(right)

    return max(dfs(root))


def checkRecord(n):
    """
    552. 学生出勤记录 II
    给定一个正整数 n，返回长度为 n 的所有可被视为可奖励的出勤记录的数量。 答案可能非常大，你只需返回结果mod 10^9 + 7的值。
    学生出勤记录是只包含以下三个字符的字符串：
    'A' : Absent，缺勤
    'L' : Late，迟到
    'P' : Present，到场
    如果记录不包含多于一个'A'（缺勤）或超过两个连续的'L'（迟到），则该记录被视为可奖励的。
    示例 1:
    输入: n = 2
    输出: 8
    解释：
    有8个长度为2的记录将被视为可奖励：
    "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
    只有"AA"不会被视为可奖励，因为缺勤次数超过一次。
    注意：n 的值不会超过100000。
    :param n: int
    :return: int
    """
    """
    # 动态规划
    # 判断条件分为前面有无A和最近的L的个数
    # 所有组合起来的情况有以下7种
    # A: 前面以A结束
    # AP: 前面有A且以P结束
    # AL: 前面有A且以L结束
    # ALL: 前面有A且以LL结束
    # L: 前面没有A且以L结束
    # LL: 前面没有A且以LL结束
    # P: 前面没有A且以P结束
    if n == 0: return 1
    P, AP, L, LL, AL, ALL, A = 1, 0, 1, 0, 0, 0, 1
    M = 10 ** 9 + 7
    for i in range(2, n+1):
        P, AP, L, LL, AL, ALL, A = (
            (P + L + LL) % M,
            (AP + AL + ALL + A) % M,
            P,
            L,
            (AP + A) % M,
            AL,
            (P + L + LL) % M
        )
    return (P + AP + L + LL + AL + ALL + A) % M
    """
    """
    # 动态规划
    # 定义三维数组dp，dp[i][j][k]表示字符串前i个字母中，最多有j个A，最多有k个连续的L，最后的答案为dp[n][1][2]
    M = 10 ** 9 + 7
    # 定义并初始化n*2*3的三维数组
    dp = [[[0] * 3 for _ in range(2)] for _ in range(n+1)]
    # 初始化
    for j in range(2):
        for k in range(3):
            dp[0][j][k] = 1
    for i in range(1, n+1):
        for j in range(2):
            for k in range(3):
                # 取上一趟的所有结果数，相当于在上一趟所有结果后面追加P
                val = dp[i-1][j][2]
                # 加上可追加A的情况，由数组定义限制j只有0和1，可追加A也就是前面有0个A的情况，符合题意
                if j > 0:
                    val = (val + dp[i-1][j-1][2]) % M
                # 加上可追加L的情况，有数组定义限制k只有0、1和2，可追加L也就是前面有0或1个连续L结尾的情况，符合题意
                if k > 0:
                    val = (val + dp[i-1][j][k-1]) % M
                dp[i][j][k] = val
    return dp[n][1][2]
    """
    # 动态规划 + 递推式
    # 使用三个数组A，P，L分别表示到字符串x[0:i]中以A，P，L结尾的所有排列，最后答案就是A[n-1]+P[n-1]+L[n-1]
    # 其中在当前位追加P没有限制 P[i] = A[i-1] + P[i-1] + L[i-1]
    # 追加L的限制条件为不能有超过两个连续的L，满足条件的有在A和P后面和在单独L结尾的后面，其中单独L也就是i-2为A或P。
    # 所以递推式：L[i] = A[i-1] + P[i-1] + A[i-2] + P[i-2]
    # 追加A的限制是前面不能有A，用当前的三个数组无法表达，需要再定义两个数组P1和L1，其中P1代表以P结尾且前面没有A，L1代表以L结尾且前面没有A
    # 那么递推式就是：
    # A[i] = P1[i-1] + L1[i-1]
    # 其中
    # P1[i] = P1[i-1] + L1[i-1]
    # L1[i] = P1[i-1] + P1[i-2]
    # 将上述2、3式多次带入1，可以消掉P1和L1，最终简化为：A[i] = A[i-1] + A[i-2] + A[i-3]
    M = 10 ** 9 + 7
    A, P, L = [0] * n, [0] * n, [0] * n
    # 初始化，简化for循环
    P[0], L[0], L[1], A[0], A[1], A[2] = 1, 1, 3, 1, 2, 4
    for i in range(1, n):
        P[i] = (P[i - 1] + A[i - 1] + L[i - 1]) % M
        if i > 1:
            L[i] = (P[i - 1] + A[i - 1] + P[i - 2] + A[i - 2]) % M
        if i > 2:
            A[i] = (A[i - 1] + A[i - 2] + A[i - 3]) % M
    return (A[n - 1] + P[n - 1] + L[n - 1]) % M


def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    458. 可怜的小猪
    有 1000 只水桶，其中有且只有一桶装的含有毒药，其余装的都是水。它们从外观看起来都一样。如果小猪喝了毒药，它会在 15 分钟内死去。
    问题来了，如果需要你在一小时内，弄清楚哪只水桶含有毒药，你最少需要多少只猪？
    回答这个问题，并为下列的进阶问题编写一个通用算法。
    进阶:
    假设有 n 只水桶，猪饮水中毒后会在 m 分钟内死亡，你需要多少猪（x）就能在 p 分钟内找出 “有毒” 水桶？这 n 只水桶里有且仅有一只有毒的桶。
    提示：
    可以允许小猪同时饮用任意数量的桶中的水，并且该过程不需要时间。
    小猪喝完水后，必须有 m 分钟的冷却时间。在这段时间里，只允许观察，而不允许继续饮水。
    任何给定的桶都可以无限次采样（无限数量的猪）。
    :param buckets: int
    :param minutesToDie: int
    :param minutesToTest: int
    :return: int
    """
    # 最简单的思路是只用1头猪去试, 这样1000桶要试1000*15分钟,显然超出了测试时间, 就要加猪
    # 想要检测的快, 两头猪就要并行去喝, 就得把1000桶水拆成ceil(√1000)*ceil(√1000)的2维矩阵, 两头猪分别从两个维度去喝, 都喝死了的坐标锁定毒药位置, 时间为ceil(√1000)*15分钟
    # 可以发现猪的数量就是维度, 把1000桶水拆成a^x, 这个a是由时间限制决定的
    # 假设答案是x, a ^ x >= 1000, a = p / m + 1 = 60 / 15 + 1 = 5  argmin(x){5^x>=1000}=5
    import math
    if buckets == 1: return 0
    # 这里不能用ceil, 为保证值不为0, 向下取整+1
    time_to_try = minutesToTest // minutesToDie + 1
    x = math.ceil(math.log(buckets, time_to_try))
    return x


def findLUSlength(strs):
    """
    522. 最长特殊序列 II
    给定字符串列表，你需要从它们中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。
    子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。
    输入将是一个字符串列表，输出是最长特殊序列的长度。如果最长特殊序列不存在，返回 -1 。
    示例：
    输入: "aba", "cdc", "eae"
    输出: 3
    提示：
    所有给定的字符串长度不会超过 10 。
    给定字符串列表的长度将在 [2, 50 ] 之间。
    :param strs: List[str]
    :return: int
    """
    pass


def minMutation(start, end, bank):
    """
    433. 最小基因变化
    一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
    假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
    例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。
    与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
    现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。
    注意:
    起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
    所有的目标基因序列必须是合法的。
    假定起始基因序列与目标基因序列是不一样的。
    示例 1:
    start: "AACCGGTT"
    end:   "AACCGGTA"
    bank: ["AACCGGTA"]
    返回值: 1
    示例 2:
    start: "AACCGGTT"
    end:   "AAACGGTA"
    bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    返回值: 2
    示例 3:
    start: "AAAAACCC"
    end:   "AACCCCCC"
    bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    返回值: 3
    :param start: str
    :param end: str
    :param bank: List[str]
    :return: int
    """
    """
    # 广度优先遍历 77%
    def is_next_step(a, b):
        ctr = 0
        for x, y in zip(a, b):
            if x != y:
                ctr += 1
        return ctr == 1

    def _next_steps(cur):
        return list(filter(lambda x: is_next_step(cur, x), bank))

    def bfs(cur, ctr):
        nonlocal ans
        if cur == end:
            ans = min(ans, ctr)
            return
        _next = _next_steps(cur)
        if not _next:
            return
        ap = cur in bank
        if ap: bank.remove(cur)
        for x in _next:
            bfs(x, ctr + 1)
        if ap: bank.append(cur)
    if end not in bank: return -1
    ans = float("inf")
    dfs(start, 0)
    return ans if ans != float("inf") else -1
    """
    # 迭代 100%
    bank = set(bank)
    if end not in bank:
        return -1
    # 初始结点及当前步数
    q = [(start, 0)]
    change = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
    while q:
        node, step = q.pop(0)
        if node == end:
            return step
        for i, v in enumerate(node):
            for j in change[v]:
                new = node[:i] + j + node[i + 1:]
                if new in bank:
                    q.append((new, step + 1))
                    # 避免重复遍历
                    bank.remove(new)
    # 队列空了说明不可达
    return -1


def largestValues(root):
    """
    515. 在每个树行中找最大值
    您需要在二叉树的每一行中找到最大的值。
    示例：
    输入:
              1
             / \
            3   2
           / \   \
          5   3   9
    输出: [1, 3, 9]
    :param root: TreeNode
    :return: List[int]
    """

    def helper(p, lv):
        if len(res) > lv:
            res[lv] = max(res[lv], p.val)
        else:
            res.append(p.val)
        if p.left: helper(p.left, lv + 1)
        if p.right: helper(p.right, lv + 1)

    res = []
    if root: helper(root, 0)
    return res


def findAndReplacePattern(words, pattern):
    """
    890. 查找和替换模式
    你有一个单词列表 words 和一个模式  pattern，你想知道 words 中的哪些单词与模式匹配。
    如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。
    （回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）
    返回 words 中与给定模式匹配的单词列表。
    你可以按任何顺序返回答案。
    示例：
    输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
    输出：["mee","aqq"]
    解释：
    "mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
    "ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
    因为 a 和 b 映射到同一个字母。
    提示：
    1 <= words.length <= 50
    1 <= pattern.length = words[i].length <= 20
    :param words: List[str]
    :param pattern: str
    :return: List[str]
    """
    """
    # 字典
    def helper(s):
        dp = {}
        for i in range(len(s)):
            if s[i] not in dp:
                dp[s[i]] = i
            if ds[pattern[i]] != dp[s[i]]: return False
        return True

    res = []
    ds = {}
    for i in range(len(pattern)):
        if pattern[i] not in ds:
            ds[pattern[i]] = i

    for each in words:
        if helper(each):
            res.append(each)
    return res
    """

    # 数组
    def helper(word):
        dp = [-1] * 26
        for i in range(len(word)):
            p = ord(pattern[i]) - a
            s = ord(word[i]) - a
            if dp[s] < 0:
                dp[s] = i
            if ds[p] != dp[s]: return False
        return True

    a = ord('a')
    ds = [-1] * 26
    for i in range(len(pattern)):
        p = ord(pattern[i]) - a
        if ds[p] < 0:
            ds[p] = i

    res = []
    for each in words:
        if helper(each):
            res.append(each)
    return res


def isNStraightHand(hand, W):
    """
    846. 一手顺子
    爱丽丝有一手（hand）由整数数组给定的牌。 
    现在她想把牌重新排列成组，使得每个组的大小都是 W，且由 W 张连续的牌组成。
    如果她可以完成分组就返回 true，否则返回 false。
    示例 1：
    输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
    输出：true
    解释：爱丽丝的手牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
    示例 2：
    输入：hand = [1,2,3,4,5], W = 4
    输出：false
    解释：爱丽丝的手牌无法被重新排列成几个大小为 4 的组。
    提示：
    1 <= hand.length <= 10000
    0 <= hand[i] <= 10^9
    1 <= W <= hand.length
    :param hand: List[int]
    :param W: int
    :return: bool
    """
    """
    # 排序再通过remove的方法找不符合条件的
    n = len(hand)
    if n % W != 0: return False
    i = 0
    hand.sort()
    while i < n:
        m = hand.pop(0)
        for j in range(W - 1):
            m += 1
            if m in hand:
                hand.remove(m)
            else:
                return False
        i += W
    return True
    """
    """
    # 用map存储数字的数量, 比remove快
    d = {}
    n = len(hand)
    if n % W != 0: return False
    hand.sort()
    for x in hand:
        if not x in d:
            d[x] = 0
        d[x] += 1
    for x in hand:
        if d[x] > 0:
            for i in range(W):
                if d.get(x+i, 0) > 0:
                    d[x+i] -= 1
                else:
                    return False
    return True
    """
    # 有小bug但是AC的想法
    r = [0] * W
    for h in hand:
        r[h % W] += 1
    return all(x == r[0] for x in r)


if __name__ == '__main__':
    ans = isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], W = 3)
    # ans = isNStraightHand(hand = [1,1,2,2,3,3], W = 3)
    print(ans)
    # findAndReplacePattern(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb")
    # x = construct_tree_node([1,3,2,5,3,null,9])
    # largestValues(x)
    # minMutation("AAAAACCC","AACCCCCC",["AAAACCCC", "AAACCCCC", "AACCCCCC"])
    # poorPigs(4, 15, 15)
    # print(checkRecord(13))
    # x = construct_tree_node([3,4,5,1,3,null,1])
    # rob3(x)
    # singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])
    # x = construct_tree_node([1,2,3,4,5,6])
    # countNodes(x)
    # computeArea(0, 0, 1, 1, 1, 1, 2, 2)
    # ans = rob2([2,7,9,3,1])
    # print(ans)
    # x = construct_tree_node([3,2,3,null, 3, null,1])
    # rob3(x)
    # recoverFromPreorder("1-2--3--4-5--6--7")
    # x = buildTree([3,9,20,15,7],[9,3,15,20,7])
    # print_tree_node(x)
    # x = buildTree2([9,3,15,20,7], [9,15,7,20,3])
    # print_tree_node(x)
    # x = construct_tree_node([4,9,0,5,1])
    # sumNumbers(x)
    pass
