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
    inorder_map = {k:v for v, k in enumerate(inorder)}
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
        root.right = helper(idx+1, r)
        root.left = helper(l, idx)
        return root

    i_key = [len(postorder)-1]
    ino_map = {k:v for v, k in enumerate(inorder)}
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
    # b用于记录数字出现一次的时候的值, a用于记录数字出现两次的值
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


if __name__ == '__main__':
    x = construct_tree_node([3,4,5,1,3,null,1])
    rob3(x)
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
