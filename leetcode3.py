# -*- coding: utf-8 -*-
# ======================================
# @File    : leetcode3.py
# @Time    : 2019/4/27 0:47
# @Author  : Rivarrl
# ======================================

# leetcode3
from algorithm_utils import *


def divide(dividend, divisor):
    """
    29. 两数相除
    给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
    返回被除数 dividend 除以除数 divisor 得到的商。
    示例 1:
    输入: dividend = 10, divisor = 3
    输出: 3
    示例 2:
    输入: dividend = 7, divisor = -3
    输出: -2
    说明:
    被除数和除数均为 32 位有符号整数。
    除数不为 0。
    假设我们的环境只能存储 32 位有符号整数，其数值范围是 [-2**31,  2**31-1]。本题中，如果除法结果溢出，则返回 2**31-1。
    思路:
    用减法会超时，所以使用更快的位运算，<<1 = *2^1, >>1 = /2^1
    :param dividend: int
    :param divisor: int
    :return: int
    """
    inf = 2**31 - 1
    MAX = inf
    MIN = -inf - 1
    if dividend == 0 : return 0
    if divisor == 1: return dividend
    if dividend == MIN and divisor == -1: return MAX
    # 结果符号，两数（符号位）亦或
    f = dividend ^ divisor >= 0
    i, j = 0, 31
    a, b = abs(dividend), abs(divisor)
    res = 0
    while i < j:
        mid = (i + j) >> 1
        x = b << mid
        y = x << 1
        if y > a >= x:
            a -= x
            res += (1 << mid)
            i, j = 0, mid
        elif a < y:
            j = mid
        else:
            i = mid
    return res if f else -res


def pancakeSort(A):
    """
    969. 煎饼排序
    给定数组 A，我们可以对其进行煎饼翻转：我们选择一些正整数 k <= A.length，然后反转 A 的前 k 个元素的顺序。
    我们要执行零次或多次煎饼翻转（按顺序一次接一次地进行）以完成对数组 A 的排序。
    返回能使 A 排序的煎饼翻转操作所对应的 k 值序列。
    任何将数组排序且翻转次数在 10 * A.length 范围内的有效答案都将被判断为正确。
    示例 1：
    输入：[3,2,4,1]
    输出：[4,2,4,3]
    解释：
    我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
    初始状态 A = [3, 2, 4, 1]
    第一次翻转后 (k=4): A = [1, 4, 2, 3]
    第二次翻转后 (k=2): A = [4, 1, 2, 3]
    第三次翻转后 (k=4): A = [3, 2, 1, 4]
    第四次翻转后 (k=3): A = [1, 2, 3, 4]，此时已完成排序。
    示例 2：
    输入：[1,2,3]
    输出：[]
    解释：
    输入已经排序，因此不需要翻转任何内容。
    请注意，其他可能的答案，如[3，3]，也将被接受。
    思路：
    最多每两次翻转完成从后向前的1位的排序，相当于选择排序，每次把当前最大值放到当前队尾
    :param A: List[int]
    :return: List[int]
    """
    l = len(A)
    res = []
    for i in range(l, 0, -1):
        j = A.index(i)
        res.extend([j + 1, i])
        A = A[:j:-1] + A[:j]
    return res


def threeSumClosest(nums, target):
    """
    16. 最接近的三数之和
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
    找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
    例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
    与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
    :param nums: List[int]
    :param target: int
    :return: int
    """
    l = len(nums)
    nums.sort()
    two_sum = [target - x for x in nums]
    resx = 2**31 - 1
    # print(nums)
    # print(two_sum)
    for k in range(l):
        i, j = 0, l - 1
        while i < j:
            if i == k:
                i += 1
                continue
            if j == k:
                j -= 1
                continue
            x = two_sum[k] - nums[i] - nums[j]
            # print(i, j, k, x)
            if x == 0:
                return target
            elif x > 0:
                i += 1
            else:
                j -= 1
            if abs(x) < abs(resx):
                resx = x
    # print(resx)
    return target - resx


def findBottomLeftValue(root):
    """
    513. 找树左下角的值
    给定一个二叉树，在树的最后一行找到最左边的值。
    示例 1:
    输入:
        2
       / \
      1   3
    输出:
    1
    示例 2:
    输入:
            1
           / \
          2   3
         /   / \
        4   5   6
           /
          7
    输出:
    7
    注意: 您可以假设树（即给定的根节点）不为 NULL。
    :param root: TreeNode
    :return: int
    """
    def inner(r, c):
        c += 1
        if r.left and r.right:
            il = inner(r.left, c)
            ir = inner(r.right, c)
            if il[1] < ir[1]:
                return ir
            else:
                return il
        elif r.left:
            return inner(r.left, c)
        elif r.right:
            return inner(r.right, c)
        else:
            return [r, c]
    return inner(root, 0)[0].val


def minimumDeleteSum(s1, s2):
    """
    712. 两个字符串的最小ASCII删除和
    给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。
    示例 1:
    输入: s1 = "sea", s2 = "eat"
    输出: 231
    解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
    在 "eat" 中删除 "t" 并将 116 加入总和。
    结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
    示例 2:
    输入: s1 = "delete", s2 = "leet"
    输出: 403
    解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
    将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
    结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
    如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
    注意:
    0 < s1.length, s2.length <= 1000。
    所有字符串中的字符ASCII值在[97, 122]之间。
    :param s1: str
    :param s2: str
    :return: int
    """
    l1, l2 = len(s1), len(s2)
    dp = [[float('inf') for _ in range(l2+1)] for _ in range(l1+1)]
    dp[0][0] = 0
    for i in range(l1):
        dp[i + 1][0] = dp[i][0] + ord(s1[i])
    for i in range(l2):
        dp[0][i + 1] = dp[0][i] + ord(s2[i])
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
    return dp[-1][-1]


def mergeKLists(lists):
    """
    23. 合并K个排序链表 （内存溢出）
    合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
    示例:
    输入:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    输出: 1->1->2->3->4->4->5->6
    :param lists: List[ListNode]
    :return: ListNode
    """
    def k_append(l):
        lstk = stk.__len__()
        if lstk == 0:
            stk.append(l)
        else:
            if l.val > stk[-1].val:
                stk.append(l)
            else:
                i, j = 0, lstk - 1
                while i <= j:
                    mid = (i + j) // 2
                    if stk[mid].val < l.val:
                        i = mid + 1
                    elif stk[mid].val > l.val:
                        j = mid - 1
                    else:
                        i, j = mid, mid
                        break
                # print(i, j, mid, end='\t')
                # print("stk", end=' ')
                # for s in stk:
                #     print(s.val, end='')
                # print(end='\t')
                # print(l.val)
                stk.insert(i, l)

    stk = []
    for l in lists:
        while l:
            k_append(l)
            l = l.next
    h = ListNode(0)
    p = h
    for s in stk:
        p.next = s
        p = p.next
    #     print(s.val)
    return h.next


def mergeKLists2(lists):
    """
    23. 合并K个排序链表
    :param lists: List[ListNode]
    :return: ListNode
    """
    def merge2Lists(p, q):
        if not p:
            return q
        if not q:
            return p
        res = None
        if p.val <= q.val:
            res = p
            res.next = merge2Lists(p.next, q)
        else:
            res = q
            res.next = merge2Lists(p, q.next)
        return res
    def mergeSLists(lists):
        l = len(lists)
        if l == 1:
            return lists[0]
        else:
            return merge2Lists(mergeSLists(lists[:l//2]), mergeSLists(lists[l//2:]))
    return mergeSLists(lists)


def mergeKLists3(lists):
    """
    23. 合并K个排序链表
    :param lists: List[ListNode]
    :return: ListNode
    """
    res = []
    for l in lists:
        while l:
            res.append(l)
            l = l.next
    res.sort(key=lambda x: x.val)
    h = ListNode(0)
    p = h
    for s in res:
        p.next = s
        p = p.next
    return h.next


def maxCoins(nums):
    """
    312. 戳气球
    有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
    现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。
    这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
    求所能获得硬币的最大数量。
    说明:
    你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
    0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
    示例:
    输入: [3,1,5,8]
    输出: 167
    解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
         coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
    :param nums: List[int]
    :return: int
    """
    l = len(nums)
    if l == 0: return 0
    if l == 1: return nums[0]
    nums = [1] + nums + [1]
    dp = [[0] * (l+2) for _ in range(l+2)]
    for q in range(1, l + 1):
        for i in range(1, l - q + 2):
            j = i + q - 1
            dp[i][j] = max(dp[i][k-1] + dp[k+1][j] + nums[k] * nums[i - 1] * nums[j+1] for k in range(i, j+1))
    # print(dp)
    return dp[1][l]


def numberOfArithmeticSlices(A):
    """
    413. 等差数列划分
    如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。
    例如，以下数列为等差数列:
    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9
    以下数列不是等差数列。
    1, 1, 2, 5, 7
    数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。
    如果满足以下条件，则称子数组(P, Q)为等差数组：
    元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。
    函数要返回数组 A 中所有为等差数组的子数组个数。
    示例:
    A = [1, 2, 3, 4]
    返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。
    :param A: List[int]
    :return: int
    """
    l = len(A)
    dp = [0] * l
    if l < 3: return 0
    size = 0
    for i in range(2, l):
        if A[i - 1] - A[i - 2] == A[i] - A[i - 1]:
            size += 1
            dp[i] = dp[i-1] + size
        else:
            size = 0
            dp[i] = dp[i-1]
    return dp[-1]


def numberOfArithmeticSlicesv2(A):
    """
    446. 等差数列划分 II - 子序列
    如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。
    例如，以下数列为等差数列:
    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9
    以下数列不是等差数列。
    1, 1, 2, 5, 7
    数组 A 包含 N 个数，且索引从 0 开始。该数组子序列将划分为整数序列 (P0, P1, ..., Pk)，P 与 Q 是整数且满足 0 ≤ P0 < P1 < ... < Pk < N。
    如果序列 A[P0]，A[P1]，...，A[Pk-1]，A[Pk] 是等差的，那么数组 A 的子序列 (P0，P1，…，PK) 称为等差序列。值得注意的是，这意味着 k ≥ 2。
    函数要返回数组 A 中所有等差子序列的个数。
    输入包含 N 个整数。每个整数都在 -231 和 231-1 之间，另外 0 ≤ N ≤ 1000。保证输出小于 231-1。
    示例：
    输入：[2, 4, 6, 8, 10]
    输出：7
    解释：
    所有的等差子序列为：
    [2,4,6]
    [4,6,8]
    [6,8,10]
    [2,4,6,8]
    [4,6,8,10]
    [2,4,6,8,10]
    [2,6,10]
    思路：
    将不同步长的结果分别记录到字典中
    :param A: List[int]
    :return: int
    """
    l = len(A)
    ans = 0
    dp = [{} for _ in range(l)]
    for i in range(1, l):
        for j in range(i):
            x = A[i] - A[j]
            if x in dp[i]:
                dp[i][x] += 1
            else:
                dp[i][x] = 1
            if x in dp[j]:
                dp[i][x] += dp[j][x]
                ans += dp[j][x]
    return ans


def mergeStones(stones, K):
    """
    1000. 合并石头的最低成本
    有 N 堆石头排成一排，第 i 堆中有 stones[i] 块石头。
    每次移动（move）需要将连续的 K 堆石头合并为一堆，而这个移动的成本为这 K 堆石头的总数。
    找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。
    示例 1：
    输入：stones = [3,2,4,1], K = 2
    输出：20
    解释：
    从 [3, 2, 4, 1] 开始。
    合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
    合并 [4, 1]，成本为 5，剩下 [5, 5]。
    合并 [5, 5]，成本为 10，剩下 [10]。
    总成本 20，这是可能的最小值。
    示例 2：
    输入：stones = [3,2,4,1], K = 3
    输出：-1
    解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.
    示例 3：
    输入：stones = [3,5,1,2,6], K = 3
    输出：25
    解释：
    从 [3, 5, 1, 2, 6] 开始。
    合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
    合并 [3, 8, 6]，成本为 17，剩下 [17]。
    总成本 25，这是可能的最小值。
    提示：
    1 <= stones.length <= 30
    2 <= K <= 30
    1 <= stones[i] <= 100
    思路：
    利用三维数组dp，dp[i][j][k]表示i-j的子序列合成k堆的最优解（最小值）
    :param stones: List[int]
    :param K: int
    :return: int
    """
    n = len(stones)
    if (n - 1) % (K-1) > 0: return -1
    inf = float('inf')
    dp = [[[inf for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][i][1] = 0
    # 避免重复计算sum
    ss = [0] + [sum(stones[:i]) for i in range(1, n+1)]
    # ln为窗口大小，也就是问题规模，最小为2
    for ln in range(2, n+1):
        # 使l和r在窗口两侧，随窗口值步进
        for l in range(1, n-ln+2):
            r = l + ln - 1
            # 相当于遍历子序列stones[l:r]
            for m in range(l, r):
                # K值，从2依次递增至当前问题规模大小
                for k in range(2, ln+1):
                    dp[l][r][k] = min(dp[l][r][k], dp[l][m][k-1] + dp[m+1][r][1])
            # 把x=K堆合并为1堆，需要dp[l][r][K] + sum(stones[l:r])
            dp[l][r][1] = dp[l][r][K] + ss[r] - ss[l-1]
    print(dp)
    return dp[1][n][1]


def combinationSum(candidates, target):
    """
    39. 组合总和
    给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
    candidates 中的数字可以无限制重复被选取。
    说明：
    所有数字（包括 target）都是正整数。
    解集不能包含重复的组合。
    示例 1:
    输入: candidates = [2,3,6,7], target = 7,
    所求解集为:
    [
      [7],
      [2,2,3]
    ]
    示例 2:
    输入: candidates = [2,3,5], target = 8,
    所求解集为:
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
    ]
    思路:
    回溯法，用filter筛选符合接下来条件的candidates进行回溯(去重)
    :param candidates: List[int]
    :param target: int
    :return: List[List[int]]
    """
    if target == 0:
        return [[]]
    elif not candidates or target < min(candidates):
        return []
    res = []
    for i in candidates:
        for j in combinationSum(list(filter(lambda x: x <= i, candidates)), target - i):
            res.append([i] + j)
    return res


def swapPairs(head):
    """
    24. 两两交换链表中的节点
    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
    你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
    示例:
    给定 1->2->3->4, 你应该返回 2->1->4->3.
    :param head: ListNode
    :return: ListNode
    """
    p = head
    head = p.next
    while p and p.next:
        q = p.next.next
        p.next.next = p
        p.next = q if not (q and q.next) else q.next
        p = q
    return head


def nextPermutation(nums):
    """
    31. 下一个排列
    实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
    如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
    必须原地修改，只允许使用额外常数空间。
    以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
    :param nums: List[int]
    :return: None
    """
    l = len(nums)
    i = 0
    for i in range(l-2, -1, -1):
        if nums[i] < nums[i+1]:
            j = i
            for j in range(i+1, l):
                if nums[j] <= nums[i]:
                    j -= 1
                    break
            nums[i], nums[j] = nums[j], nums[i]
            break
    else:
        nums.sort()
    for j in range(i + 1, l):
        for k in range(j + 1, l):
            if nums[j] > nums[k]:
                nums[k], nums[j] = nums[j], nums[k]
    print(nums)


def removeNthFromEnd(head, n):
    """
    19. 删除链表的倒数第N个节点
    给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
    示例：
    给定一个链表: 1->2->3->4->5, 和 n = 2.
    当删除了倒数第二个节点后，链表变为 1->2->3->5.
    说明：
    给定的 n 保证是有效的。
    进阶：
    你能尝试使用一趟扫描实现吗？
    :param head: ListNode
    :param n: int
    :return: ListNode
    """
    stk = []
    p = head
    while p:
        stk.append(p)
        p = p.next
    if stk.__len__() == n:
        head = head.next
    else:
        stk[-1 - n].next = stk[1-n] if n > 1 else None
    return head


def search(nums, target):
    """
    33. 搜索旋转排序数组
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
    你可以假设数组中不存在重复的元素。
    你的算法时间复杂度必须是 O(log n) 级别。
    示例 1:
    输入: nums = [4,5,6,7,0,1,2], target = 0
    输出: 4
    示例 2:
    输入: nums = [4,5,6,7,0,1,2], target = 3
    输出: -1
    :param nums: List[int]
    :param target: int
    :return: int
    """
    l = len(nums)
    i, j = 0, l - 1
    while i < j:
        m = (i+j) // 2
        print(nums[m])
        if nums[i] == target: return i
        if nums[j] == target: return j
        if nums[m] == target: return m
        # nums[i:j]有序
        if nums[i] < nums[j]:
            if nums[i] > target or nums[j] < target:
                return -1
            else:
                if nums[m] > target:
                    j = m - 1
                else:
                    i = m + 1
        else:
            if nums[i] < nums[m]:
                # 左边是顺序的
                if nums[i] > target or nums[m] < target:
                    # 去右侧找
                    i = m + 1
                else:
                    j = m - 1
            else:
                # 右边是顺序的
                if nums[j] < target or nums[m] > target:
                    j = m - 1
                else:
                    i = m + 1
    return -1 if not nums or nums[i] != target else i


def compareVersion(version1, version2):
    """
    165. 比较版本号
    比较两个版本号 version1 和 version2。
    如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。
    你可以假设版本字符串非空，并且只包含数字和 . 字符。
     . 字符不代表小数点，而是用于分隔数字序列。
    例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。
    你可以假设版本号的每一级的默认修订版号为 0。例如，版本号 3.4 的第一级（大版本）和第二级（小版本）修订号分别为 3 和 4。其第三级和第四级修订号均为 0。
    示例 1:
    输入: version1 = "0.1", version2 = "1.1"
    输出: -1
    示例 2:
    输入: version1 = "1.0.1", version2 = "1"
    输出: 1
    示例 3:
    输入: version1 = "7.5.2.4", version2 = "7.5.3"
    输出: -1
    示例 4：
    输入：version1 = "1.01", version2 = "1.001"
    输出：0
    解释：忽略前导零，“01” 和 “001” 表示相同的数字 “1”。
    示例 5：
    输入：version1 = "1.0", version2 = "1.0.0"
    输出：0
    解释：version1 没有第三级修订号，这意味着它的第三级修订号默认为 “0”。
    提示：
    版本字符串由以点 （.） 分隔的数字字符串组成。这个数字字符串可能有前导零。
    版本字符串不以点开始或结束，并且其中不会有两个连续的点。
    :param version1: str
    :param version2: str
    :return: int
    """
    v1 = [int(x) for x in version1.split('.')]
    v2 = [int(x) for x in version2.split('.')]
    while len(v1) < len(v2):
        v1.append(0)
    while len(v2) < len(v1):
        v2.append(0)
    for i in range(len(v1)):
        if v1[i] != v2[i]:
            return 1 if v1 > v2 else -1
    return 0


def maxPathSum(root):
    """
    124. 二叉树中的最大路径和
    给定一个非空二叉树，返回其最大路径和。
    本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
    示例 1:
    输入: [1,2,3]
           1
          / \
         2   3
    输出: 6
    示例 2:
    输入: [-10,9,20,null,null,15,7]
       -10
       / \
      9  20
        /  \
       15   7
    输出: 42
    :param root: TreeNode
    :return: int
    """
    def helper(root):
        p = MIN
        if root:
            p = root.val
            l = helper(root.left)
            r = helper(root.right)
            cur = max(p, p+l, p+r)
            ans[-1] = max(ans[-1], cur, l, r, p+l+r)
            p = cur
        return p
    MIN = -2**31
    ans = [MIN]
    helper(root)
    return ans[-1]


def sortList(head):
    """
    148. 排序链表
    在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
    示例 1:
    输入: 4->2->1->3
    输出: 1->2->3->4
    示例 2:
    输入: -1->5->3->4->0
    输出: -1->0->3->4->5
    :param head: ListNode
    :return: ListNode
    """
    if not head or not head.next:  # 如果无节点或只有一个节点
        return head
    elif not head.next.next:  # 如果刚好两个结点
        if head.next.val < head.val:  # 更正顺序
            head.next.next = head
            head = head.next
            head.next.next = None
        return head

    slow, fast = head, head  # 快慢指针找中点
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    # 截断并分别递归
    head2 = slow.next
    slow.next = None
    l1 = sortList(head)
    l2 = sortList(head2)

    # 合并
    if not l1 or not l2:
        return l1 or l2
    head = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return head.next


def kthSmallest(root, k):
    """
    230. 二叉搜索树中第K小的元素
    给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
    说明：
    你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
    示例 1:
    输入: root = [3,1,4,null,2], k = 1
       3
      / \
     1   4
      \
       2
    输出: 1
    示例 2:
    输入: root = [5,3,6,2,4,null,null,1], k = 3
           5
          / \
         3   6
        / \
       2   4
      /
     1
    输出: 3
    进阶：
    如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
    :param root: TreeNode
    :param k: int
    :return: int
    """
    def inner(root):
        if root:
            inner(root.left)
            ans.append(root.val)
            inner(root.right)
    ans = []
    inner(root)
    return ans[k-1]


def productExceptSelf(nums):
    """
    238. 除自身以外数组的乘积
    给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
    示例:
    输入: [1,2,3,4]
    输出: [24,12,8,6]
    说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
    进阶：
    你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
    :param nums: List[int]
    :return: List[int]
    """
    """
    # O(n^2)
    from functools import reduce
    l = len(nums)
    res = [0] * l
    d = {}
    f = lambda x, y: x * y
    for i in range(l):
        if nums[i] not in d:
            d[nums[i]] = reduce(f, nums[:i] + nums[i+1:])
        res[i] = d[nums[i]]
    return res
    """
    # O(n) 且空间复杂度常数
    # 从左乘到右，再从右乘到左，每次做乘法的时候错开自身
    left, right, length = 1, 1, len(nums)
    res = [0] * length
    for i in range(length):
        res[i] = left
        left *= nums[i]
    print(res)
    for i in range(length-1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res


def lowestCommonAncestor(root, p, q):
    """
    236. 二叉树的最近公共祖先
    给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
    百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
    例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
    示例 1:
    输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    输出: 3
    解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
    示例 2:
    输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    输出: 5
    解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
    说明:
    所有节点的值都是唯一的。
    p、q 为不同节点且均存在于给定的二叉树中。
    :param root: TreeNode
    :param p: TreeNode
    :param q: TreeNode
    :return: TreeNode
    """
    """
    # 找到+1
    def inner(root, p, q, cur):
        if root:
            cur = inner(root.left, p, q, cur) + inner(root.right, p, q, cur) + int(root == p or root == q)
            if cur == 2:
                ans.append(root)
        return cur
    ans = []
    inner(root, p, q, 0)
    return ans[0]
    """
    if not root: return None
    if root == p or root == q: return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if not left:
        return right
    elif not right:
        return left
    else:
        return root


def detectCycle(head):
    """
    142. 环形链表 II
    给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
    说明：不允许修改给定的链表。
    示例 1：
    输入：head = [3,2,0,-4], pos = 1
    输出：tail connects to node index 1
    解释：链表中有一个环，其尾部连接到第二个节点。
    示例 2：
    输入：head = [1,2], pos = 0
    输出：tail connects to node index 0
    解释：链表中有一个环，其尾部连接到第一个节点。
    示例 3：
    输入：head = [1], pos = -1
    输出：no cycle
    解释：链表中没有环。
    进阶：
    你是否可以不用额外空间解决此题？
    :param head: ListNode
    :return: ListNode
    """
    if head and head.next:
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                res = head
                while res != slow:
                    slow = slow.next
                    res = res.next
                return res
    return None


if __name__ == '__main__':
    pass
    print(productExceptSelf([1, 2, 3, 4]))
    # tree = construct_tree_node([3,1,4,None,2])
    # print(kthSmallest(tree, 2))
    # tree = construct_tree_node([1,-2,-3,1,3,-2,None,-1])
    # maxPathSum(tree)
    # print(search([1,2,3,4,5,6], 4))
    # nextPermutation([1,5,1])
    # print(combinationSum([2, 3, 6, 7], 7))
    # print(numberOfArithmeticSlicesv2([1,2,3,5,6,7]))
    # print(mergeStones([25,68,35,62,52,57,35,83,40,51,30,20,51], 7))
    # print(maxCoins([3,1,5,8]))
    # x = ListNode(1)
    # p = x
    # for y in [2,3,4]:
    #     p.next = ListNode(y)
    #     p = p.next
    # print_list_node(swapPairs(x))
    # y = ListNode(1)
    # q = y
    # for z in [1,2]:
    #     q.next = ListNode(z)
    #     q = q.next
    # a = ListNode(2)
    # a.next = ListNode(6)
    # y.next = z
    # mergeKLists([x,y])
    # print(minimumDeleteSum("delete", "leet"))
    # print(divide(10,2))
    # print(threeSumClosest([1,6,9,14,16,70], 81))
    # x = TreeNode(5)
    # x.left = TreeNode(7)
    # y = TreeNode(3)
    # y.left = x
    # y.right = TreeNode(6)
    # z = TreeNode(2)
    # z.left = TreeNode(4)
    # t = TreeNode(1)
    # t.left = z
    # t.right = y
    # print(findBottomLeftValue(t))