# -*- coding: utf-8 -*-
# ======================================
# @File    : leetcode_nm3.py
# @Time    : 2019/10/3 22:54
# @Author  : Rivarrl
# ======================================
from typing import List

from algorithm_utils import *

def findPeakElement(nums):
    """
    162. 寻找峰值
    峰值元素是指其值大于左右相邻值的元素。
    给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
    数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
    你可以假设 nums[-1] = nums[n] = -∞。
    示例 1:
    输入: nums = [1,2,3,1]
    输出: 2
    解释: 3 是峰值元素，你的函数应该返回其索引 2。
    示例 2:
    输入: nums = [1,2,1,3,5,6,4]
    输出: 1 或 5
    解释: 你的函数可以返回索引 1，其峰值元素为 2；
         或者返回索引 5， 其峰值元素为 6。
    说明:
    你的解法应该是 O(logN) 时间复杂度的。
    :param nums: List[int]
    :return: int
    """
    """
    # 暴力
    nums.insert(0, -float('inf'))
    nums.append(-float('inf'))
    n = len(nums)
    for i in range(1, n - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            return i - 1
    """
    # 二分查找
    l, r = 0, len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        if nums[m] > nums[m+1]:
            r = m
        else:
            l = m + 1
    return l


def largerstNumber(nums):
    """
    179. 最大数
    给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
    示例 1:
    输入: [10,2]
    输出: 210
    示例 2:
    输入: [3,30,34,5,9]
    输出: 9534330
    说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
    :param nums: List[int]
    :return: str
    """
    # 冒泡排序
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                nums[i], nums[j] = nums[j], nums[i]
    return str(int("".join([str(i) for i in nums])))


def reverseParentheses(s):
    """
    1190. 反转每对括号间的子串
    给出一个字符串 s（仅含有小写英文字母和括号）。
    请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
    注意，您的结果中 不应 包含任何括号。
    示例 1：
    输入：s = "(abcd)"
    输出："dcba"
    示例 2：
    输入：s = "(u(love)i)"
    输出："iloveu"
    示例 3：
    输入：s = "(ed(et(oc))el)"
    输出："leetcode"
    示例 4：
    输入：s = "a(bcdefghijkl(mno)p)q"
    输出："apmnolkjihgfedcbq"
    提示：
    0 <= s.length <= 2000
    s 中只有小写英文字母和括号
    我们确保所有括号都是成对出现的
    :param s: str
    :return: str
    """
    n = len(s)
    stk = []
    i = 0
    while i < n:
        if s[i] == '(':
            stk.append(i)
        elif s[i] == ')':
            j = stk.pop()
            s = s[:j] + s[j+1:i][::-1] + s[i+1:]
            i -= 2
            n -= 2
        i += 1
    return s


def kConcatenationMaxSum(arr, k):
    """
    1191. K 次串联后最大子数组之和
    给你一个整数数组 arr 和一个整数 k。
    首先，我们要对该数组进行修改，即把原数组 arr 重复 k 次。
    举个例子，如果 arr = [1, 2] 且 k = 3，那么修改后的数组就是 [1, 2, 1, 2, 1, 2]。
    然后，请你返回修改后的数组中的最大的子数组之和。
    注意，子数组长度可以是 0，在这种情况下它的总和也是 0。
    由于 结果可能会很大，所以需要 模（mod） 10^9 + 7 后再返回。 
    示例 1：
    输入：arr = [1,2], k = 3
    输出：9
    示例 2：
    输入：arr = [1,-2,1], k = 5
    输出：2
    示例 3：
    输入：arr = [-1,-2], k = 7
    输出：0
    提示：
    1 <= arr.length <= 10^5
    1 <= k <= 10^5
    -10^4 <= arr[i] <= 10^4
    :param arr: List[int]
    :param k: int
    :return: int
    """
    mod = 10 ** 9 + 7
    s, maxs = 0, 0
    for a in arr * min(2, k):
        s = a if s < 0 else s + a  # 连续和
        if s > maxs:
            maxs = s  # 最大连续和
    if k <= 2:
        return maxs  # 两个周期以内之间返回最大连续和
    return (max(sum(arr), 0) * (k - 2) + maxs) % mod


def sortArray(nums):
    """
    912. 排序数组
    给定一个整数数组 nums，将该数组升序排列。
    示例 1：
    输入：[5,2,3,1]
    输出：[1,2,3,5]
    示例 2：
    输入：[5,1,1,2,0,0]
    输出：[0,0,1,1,2,5]
    提示：
    1 <= A.length <= 10000
    -50000 <= A[i] <= 50000
    :param nums: List[int]
    :return: List[int]
    """
    def sort(l, r, arr):
        if l >= r: return
        base = arr[l]
        i, j = l, r - 1
        while i < j:
            while i <= j and arr[i] <= base:
                i += 1
            while i <= j and arr[j] >= base:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[i] = arr[i], arr[l]
        sort(l, i, arr)
        sort(i+1, r, arr)
    sort(0, len(nums), nums)
    return nums


def sumSubarrayMins(A):
    """
    907. 子数组的最小值之和
    给定一个整数数组 A，找到 min(B) 的总和，其中 B 的范围为 A 的每个（连续）子数组。
    由于答案可能很大，因此返回答案模 10^9 + 7。
    示例：
    输入：[3,1,2,4]
    输出：17
    解释：
    子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
    最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
    提示：
    1 <= A <= 30000
    1 <= A[i] <= 30000
    :param A: List[int]
    :return: int
    """
    len_A = len(A)
    if len_A == 0:
        return 0
    if len_A == 1:
        return A[0]

    ans = 0
    left = [0] * len_A
    right = [0] * len_A

    stack = []
    for i in range(len_A):
        while stack and A[stack[-1]] > A[i]:
            stack.pop()
        if not stack:
            left[i] = -1
        else:
            left[i] = stack[-1]
        stack.append(i)

    stack = []
    for i in range(len_A - 1, -1, -1):
        while stack and A[stack[-1]] >= A[i]:
            stack.pop()
        if not stack:
            right[i] = len_A
        else:
            right[i] = stack[-1]
        stack.append(i)

    for i in range(len_A):
        ans += (i - left[i]) * (right[i] - i) * A[i]
        ans %= 1000000007
    return ans


def shoppingOffers(price, special, needs):
    """
    638. 大礼包
    在LeetCode商店中， 有许多在售的物品。
    然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。
    现给定每个物品的价格，每个大礼包包含物品的清单，以及待购物品清单。请输出确切完成待购清单的最低花费。
    每个大礼包的由一个数组中的一组数据描述，最后一个数字代表大礼包的价格，其他数字分别表示内含的其他种类物品的数量。
    任意大礼包可无限次购买。
    示例 1:
    输入: [2,5], [[3,0,5],[1,2,10]], [3,2]
    输出: 14
    解释:
    有A和B两种物品，价格分别为¥2和¥5。
    大礼包1，你可以以¥5的价格购买3A和0B。
    大礼包2，你可以以¥10的价格购买1A和2B。
    你需要购买3个A和2个B， 所以你付了¥10购买了1A和2B（大礼包2），以及¥4购买2A。
    示例 2:
    输入: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
    输出: 11
    解释:
    A，B，C的价格分别为¥2，¥3，¥4.
    你可以用¥4购买1A和1B，也可以用¥9购买2A，2B和1C。
    你需要买1A，2B和1C，所以你付了¥4买了1A和1B（大礼包1），以及¥3购买1B， ¥4购买1C。
    你不可以购买超出待购清单的物品，尽管购买大礼包2更加便宜。
    说明:
    最多6种物品， 100种大礼包。
    每种物品，你最多只需要购买6个。
    你不可以购买超出待购清单的物品，即使更便宜。
    :param price: List[int]
    :param special: List[List[int]]
    :param needs: List[int]
    :return: int
    """
    # 回溯
    def shopping(special, needs):  # 从special里刚好购买needs所需的最低花费
        if not sum(needs):  # needs已没有
            return 0
        # 先过滤掉special里已经有某一种物品超过了needs的礼包
        special = list(filter(lambda x: all(x[i] <= needs[i] for i in range(l)), special))
        if not special:  # 如果过滤后为空，那么返回直接以单品购买needs的价格
            return sum(needs[i] * price[i] for i in range(l))
        res = []
        for pac in special:  # 回溯，收集本次购买每种礼包的花费加上若购买该礼包后剩余needs递归的最低花费
            res.append(pac[-1] + shopping(special, [needs[i] - pac[i] for i in range(l)]))
        return min(res)  # 返回本次购买的几种选择中的最低花费

    l = len(price)
    # 先过滤掉不比原价买划算的礼包
    special = list(filter(lambda x: x[-1] < sum(x[i] * price[i] for i in range(l)), special))
    return shopping(special, needs)


def countNumbersWithUniqueDigits(n):
    """
    357. 计算各个位数不同的数字个数
    给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。
    示例:
    输入: 2
    输出: 91
    解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
    :param n: int
    :return: int
    """
    n = min(10, n)
    dp = [0] * (n+1)
    dp[0] = 1
    q = [1, 9] + [i for i in range(9, 0, -1)]
    c = 1
    for i in range(1, n+1):
        c *= q[i]
        dp[i] = c + dp[i-1]
    print(dp)
    return dp[n]


def findPaths(m, n, N, i, j):
    """
    576. 出界的路径数
    给定一个 m × n 的网格和一个球。球的起始坐标为 (i,j) ，你可以将球移到相邻的单元格内，或者往上、下、左、右四个方向上移动使球穿过网格边界。但是，你最多可以移动 N 次。找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 109 + 7 的值。
    示例 1：
    输入: m = 2, n = 2, N = 2, i = 0, j = 0
    输出: 6
    说明:
    球一旦出界，就不能再被移动回网格内。
    网格的长度和高度在 [1,50] 的范围内。
    N 在 [0,50] 的范围内。
    :param m: int
    :param n: int
    :param N: int
    :param i: int
    :param j: int
    :return: int
    """
    """
    # memo
    def bfs(i, j, step):
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1
        if step == N:
            return 0
        if memo[i][j][step] >= 0:
            return memo[i][j][step]
        cur = 0
        cur += bfs(i-1, j, step+1)
        cur %= mod
        cur += bfs(i+1, j, step+1)
        cur %= mod
        cur += bfs(i, j-1, step+1)
        cur %= mod
        cur += bfs(i, j+1, step+1)
        cur %= mod
        memo[i][j][step] = cur
        return cur
    mod = 10 ** 9 + 7
    memo = [[[-1] * N for _ in range(n)] for _ in range(m)]
    return bfs(i, j, 0)
    """
    # dp
    if N == 0: return 0
    mod = 10 ** 9 + 7
    dp = [[[0] * (N) for _ in range(n+2)] for _ in range(m+2)]
    res = 0
    dp[i+1][j+1][0] = 1
    if i == 0: res += 1
    if i == m - 1: res += 1
    if j == 0: res += 1
    if j == n - 1: res += 1
    for step in range(1, N):
        for a in range(1, m+1):
            for b in range(1, n+1):
                dp[a][b][step] += dp[a-1][b][step-1] + dp[a][b-1][step-1] + dp[a+1][b][step-1] + dp[a][b+1][step-1]
                dp[a][b][step] %= mod
                if a == 1: res += dp[a][b][step]
                if a == m: res += dp[a][b][step]
                if b == 1: res += dp[a][b][step]
                if b == n: res += dp[a][b][step]
                res %= mod
    return res


def triangleNumber(nums):
    """
    611. 有效三角形的个数
    给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
    示例 1:
    输入: [2,2,3,4]
    输出: 3
    解释:
    有效的组合是:
    2,3,4 (使用第一个 2)
    2,3,4 (使用第二个 2)
    2,2,3
    注意:
    数组长度不超过1000。
    数组里整数的范围为 [0, 1000]。
    :param nums: List[int]
    :return: int
    """
    nums.sort()
    res = 0
    for k in range(2, len(nums)):
        i, j = 0, k-1
        while i < j:
            if nums[i] + nums[j] > nums[k]:
                res += j - i
                j -= 1
            else:
                i += 1
    return res


def validSquare(p1, p2, p3, p4):
    """
    593. 有效的正方形
    给定二维空间中四点的坐标，返回四点是否可以构造一个正方形。
    一个点的坐标（x，y）由一个有两个整数的整数数组表示。
    示例:
    输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
    输出: True
    注意:
    所有输入整数都在 [-10000，10000] 范围内。
    一个有效的正方形有四个等长的正长和四个等角（90度角）。
    输入点没有顺序。
    :param p1: List[int]
    :param p2: List[int]
    :param p3: List[int]
    :param p4: List[int]
    :return: bool
    """
    arr = [tuple(p1), tuple(p2), tuple(p3), tuple(p4)]
    if len(set(arr)) != 4: return False
    dis = lambda p1, p2: (p1[0]-p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    s = set()
    for i in range(1, 4):
        for j in range(i):
            d = dis(arr[i], arr[j])
            if not d in s:
                s.add(d)
    return len(s) == 2


def minDistance(word1, word2):
    """
    583. 两个字符串的删除操作
    给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，
    每步可以删除任意一个字符串中的一个字符。
    示例 1:
    输入: "sea", "eat"
    输出: 2
    解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
    说明:
    给定单词的长度不超过500。
    给定单词中的字符只含有小写字母。
    :param word1: str
    :param word2: str
    :return: int
    """
    """
    # 方法一
    # 当作 72 编辑距离 题做
    n1, n2 = len(word1), len(word2)
    dp = [[0] * (n2+1) for _ in range(n1+1)]
    for i in range(n1+1):
        dp[i][0] = i
    for j in range(n2+1):
        dp[0][j] = j
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
    return dp[n1][n2]
    """
    """
    # 方法二
    # 当作最长公共子串 lcs 做 (超时)
    def lcs(k1, k2):
        # 返回word1(0-k1) 和 word2(0-k2)的lcs长度
        if k1 == 0 or k2 == 0:
            return 0
        if memo[k1][k2] > 0:
            return memo[k1][k2]
        if word1[k1-1] == word2[k2-1]:
            memo[k1][k2] = 1 + lcs(k1-1, k2-1)
        else:
            memo[k1][k2] = max(lcs(k1-1, k2), lcs(k1, k2-1))
        return memo[k1][k2]

    n1, n2 = len(word1), len(word2)
    memo = [[0] * (n2+1) for _ in range(n1+1)]
    return n1 + n2 - 2 * lcs(n1, n2)
    """
    # 方法二，用自底向上的动态规划做
    n1, n2 = len(word1), len(word2)
    dp = [[0] * (n2+1) for _ in range(n1+1)]
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return n1 + n2 - 2 * dp[n1][n2]


def removeDuplicates(nums):
    """
    80. 删除排序数组中的重复项 II
    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
    示例 1:
    给定 nums = [1,1,1,2,2,3],
    函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
    你不需要考虑数组中超出新长度后面的元素。
    示例 2:
    给定 nums = [0,0,1,1,1,1,2,3,3],
    函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
    你不需要考虑数组中超出新长度后面的元素。
    :param nums: List[int]
    :return: int
    """
    """
    # pop 50%
    c = 0
    for i in range(len(nums)-2, -1, -1):
        if nums[i] == nums[i+1]:
            c += 1
        else:
            c = 0
        if c >= 2:
            nums.pop(i)
    print(nums)
    return len(nums)
    """
    # swap 90%
    i = 0
    for e in nums:
        if i < 2 or e != nums[i-2]:
            nums[i] = e
            i += 1
    return i


def deleteDuplicates(head):
    """
    82. 删除排序链表中的重复元素 II
    给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
    示例 1:
    输入: 1->2->3->3->4->4->5
    输出: 1->2->5
    示例 2:
    输入: 1->1->1->2->3
    输出: 2->3
    :param head: ListNode
    :return: ListNode
    """
    p, q = head, ListNode(0.0)
    res = q
    while p:
        if p.next == None:
            q.next = p
            q = q.next
            break
        if p.val == p.next.val:
            while p.next and p.val == p.next.val:
                p = p.next
        else:
            q.next = p
            q = q.next
        p = p.next
    q.next = None
    return res.next


def search(nums, target):
    """
    81. 搜索旋转排序数组 II
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
    编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
    示例 1:
    输入: nums = [2,5,6,0,0,1,2], target = 0
    输出: true
    示例 2:
    输入: nums = [2,5,6,0,0,1,2], target = 3
    输出: false
    进阶:
    这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
    这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
    :param nums: List[int]
    :param target: int
    :return: bool
    """
    i, j = 0, len(nums) - 1
    while i <= j:
        m = i + (j - i) // 2
        if nums[m] == target: return True
        if nums[m] == nums[i] == nums[j]:
            i += 1
            j -= 1
        elif nums[i] <= nums[m]:
            if nums[i] <= target < nums[m]:
                j = m - 1
            else:
                i = m + 1
        else:
            if nums[m] < target <= nums[j]:
                i = m + 1
            else:
                j = m - 1
    return False


def minAvailableDuration(slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    """
    5089. 安排会议日程
    你是一名行政助理，手里有两位客户的空闲时间表：slots1 和 slots2，以及会议的预计持续时间 duration，请你为他们安排合适的会议时间。
    「会议时间」是两位客户都有空参加，并且持续时间能够满足预计时间 duration 的 最早的时间间隔。
    如果没有满足要求的会议时间，就请返回一个 空数组。
    「空闲时间」的格式是 [start, end]，由开始时间 start 和结束时间 end 组成，表示从 start 开始，到 end 结束。 
    题目保证数据有效：同一个人的空闲时间不会出现交叠的情况，
    也就是说，对于同一个人的两个空闲时间 [start1, end1] 和 [start2, end2]，要么 start1 > end2，要么 start2 > end1。
    示例 1：
    输入：slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
    输出：[60,68]
    示例 2：
    输入：slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
    输出：[]
    提示：
    1 <= slots1.length, slots2.length <= 10^4
    slots1[i].length, slots2[i].length == 2
    slots1[i][0] < slots1[i][1]
    slots2[i][0] < slots2[i][1]
    0 <= slots1[i][j], slots2[i][j] <= 10^9
    1 <= duration <= 10^6 
    """
    def crossrange(e1, e2, duration):
        m1, m2 = max(e1[0], e2[0]), min(e1[1], e2[1])
        if m2 - m1 >= duration:
            return [m1, m1+duration]
    import heapq
    q1, q2 = [], []
    for s1 in slots1:
        heapq.heappush(q1, tuple(s1))
    for s2 in slots2:
        heapq.heappush(q2, tuple(s2))
    e1, e2 = None, None
    while (q1 or e1) and (q2 or e2):
        if e1 == None: e1 = heapq.heappop(q1)
        if e2 == None: e2 = heapq.heappop(q2)
        print(e1, e2)
        c = crossrange(e1, e2, duration)
        if c != None: return c
        if e1[1] == e2[1]: e1, e2 = None, None
        elif e1[1] < e2[1]: e1 = None
        else: e2 = None
    return []


def probabilityOfHeads(prob: List[float], target: int) -> float:
    """
    5090. 抛掷硬币
    有一些不规则的硬币。在这些硬币中，prob[i] 表示第 i 枚硬币正面朝上的概率。
    请对每一枚硬币抛掷 一次，然后返回正面朝上的硬币数等于 target 的概率。
    示例 1：
    输入：prob = [0.4], target = 1
    输出：0.40000
    示例 2：
    输入：prob = [0.5,0.5,0.5,0.5,0.5], target = 0
    输出：0.03125
    提示：
    1 <= prob.length <= 1000
    0 <= prob[i] <= 1
    0 <= target <= prob.length
    如果答案与标准答案的误差在 10^-5 内，则被视为正确答案。
    """
    n = len(prob)
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[0][0] = dp[0][1] = 1.0
    for i in range(1, n+1):
        k = min(target, i)
        for j in range(k+1):
            if j > 0:
                dp[i][j] += dp[i-1][j-1] * prob[i-1]
            if j < i:
                dp[i][j] += dp[i-1][j] * (1-prob[i-1])
    print(dp)
    return dp[n][target]


def removeSubfolders(folder: List[str]) -> List[str]:
    """
    5231. 删除子文件夹
    你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有 子文件夹，并以 任意顺序 返回剩下的文件夹。
    我们这样定义「子文件夹」：
    如果文件夹 folder[i] 位于另一个文件夹 folder[j] 下，那么 folder[i] 就是 folder[j] 的子文件夹。
    文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：
    / 后跟一个或者多个小写英文字母。
    例如，/leetcode 和 /leetcode/problems 都是有效的路径，而空字符串和 / 不是。
    示例 1：
    输入：folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
    输出：["/a","/c/d","/c/f"]
    解释："/a/b/" 是 "/a" 的子文件夹，而 "/c/d/e" 是 "/c/d" 的子文件夹。
    示例 2：
    输入：folder = ["/a","/a/b/c","/a/b/d"]
    输出：["/a"]
    解释：文件夹 "/a/b/c" 和 "/a/b/d/" 都会被删除，因为它们都是 "/a" 的子文件夹。
    示例 3：
    输入：folder = ["/a/b/c","/a/b/d","/a/b/ca"]
    输出：["/a/b/c","/a/b/ca","/a/b/d"]
    提示：
    1 <= folder.length <= 4 * 10^4
    2 <= folder[i].length <= 100
    folder[i] 只包含小写字母和 /
    folder[i] 总是以字符 / 起始
    每个文件夹名都是唯一的
    """
    folder.sort(key=lambda x:len(x))
    parent = []
    for f in folder:
        isc = False
        for p in parent:
            idx = f.find(p)
            if idx >= 0 and f[idx+len(p)] == '/':
                isc = True
                break
        if not isc: parent.append(f)
    print(parent)
    return parent


def balancedString(s: str) -> int:
    """
    5232. 替换子串得到平衡字符串
    有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。
    假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。
    给你一个这样的字符串 s，请通过「替换子串」的方式，使原字符串 s 变成一个「平衡字符串」。
    你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
    请返回待替换子串的最小可能长度。
    如果原字符串自身就是一个平衡字符串，则返回 0。
    示例 1：
    输入：s = "QWER"
    输出：0
    解释：s 已经是平衡的了。
    示例 2：
    输入：s = "QQWE"
    输出：1
    解释：我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。
    示例 3：
    输入：s = "QQQW"
    输出：2
    解释：我们可以把前面的 "QQ" 替换成 "ER"。
    示例 4：
    输入：s = "QQQQ"
    输出：3
    解释：我们可以替换后 3 个 'Q'，使 s = "QWER"。
    提示：
    1 <= s.length <= 10^5
    s.length 是 4 的倍数
    s 中只含有 'Q', 'W', 'E', 'R' 四种字符
    """
    def ok(l, r):
        for i in range(4):
            if A[-1][i] + A[l][i] - A[r][i] > avg:
                return False
        return True
    ctr = [0] * 4
    A = [tuple(ctr)]
    for c in s:
        ctr['QWER'.index(c)] += 1
        A.append(tuple(ctr))
    n = len(s)
    avg = n // 4
    if max(ctr) == avg: return 0
    l, r = 0, n - 1
    while r <= n:
        if ok(l, r):
            r -= 1
        else:
            l += 1
            r += 1
    return r - l + 1


def longestSubsequence(arr: List[int], difference: int) -> int:
    """
    1218. 最长定差子序列
    给你一个整数数组 arr 和一个整数 difference，请你找出 arr 中所有相邻元素之间的差等于给定 difference 的等差子序列，并返回其中最长的等差子序列的长度。
    示例 1：
    输入：arr = [1,2,3,4], difference = 1
    输出：4
    解释：最长的等差子序列是 [1,2,3,4]。
    示例 2：
    输入：arr = [1,3,5,7], difference = 1
    输出：1
    解释：最长的等差子序列是任意单个元素。
    示例 3：
    输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
    输出：4
    解释：最长的等差子序列是 [7,5,3,1]。
    提示：
    1 <= arr.length <= 10^5
    -10^4 <= arr[i], difference <= 10^4
    """
    d = {}
    for e in arr:
        if not e in d:
            d[e] = int(bool(difference))
        if e - difference in d:
            d[e] = max(d[e], d[e-difference] + 1)
    return max(d.values())


def getMaximumGold(grid: List[List[int]]) -> int:
    """
    1219. 黄金矿工
    你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。
    为了使收益最大化，矿工需要按以下规则来开采黄金：
    每当矿工进入一个单元，就会收集该单元格中的所有黄金。
    矿工每次可以从当前位置向上下左右四个方向走。
    每个单元格只能被开采（进入）一次。
    不得开采（进入）黄金数目为 0 的单元格。
    矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。
    示例 1：
    输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
    输出：24
    解释：
    [[0,6,0],
     [5,8,7],
     [0,9,0]]
    一种收集最多黄金的路线是：9 -> 8 -> 7。
    示例 2：
    输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    输出：28
    解释：
    [[1,0,7],
     [2,0,6],
     [3,4,5],
     [0,3,0],
     [9,0,20]]
    一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。
    提示：
    1 <= grid.length, grid[i].length <= 15
    0 <= grid[i][j] <= 100
    最多 25 个单元格中有黄金。
    """
    def dfs(i, j):
        if i < 0 or i == n or j < 0 or j == m or grid[i][j] == 0 or vis[i][j]:
            return 0
        vis[i][j] = True
        res = grid[i][j]
        ma = 0
        for dx, dy in d:
            x, y = i + dx, j + dy
            ma = max(dfs(x, y), ma)
        res += ma
        vis[i][j] = False
        return res

    n = len(grid)
    m = len(grid[0])
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))
    res = 0
    for i in range(n):
        for j in range(m):
            vis = [[False] * m for _ in range(n)]
            res = max(dfs(i, j), res)
    # print(res)
    return res


def removeNearDuplicates(s: str, k: int) -> str:
    """
    1209. 删除字符串中的所有相邻重复项 II
    给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。
    你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。
    在执行完所有删除操作后，返回最终得到的字符串。
    本题答案保证唯一。
    示例 1：
    输入：s = "abcd", k = 2
    输出："abcd"
    解释：没有要删除的内容。
    示例 2：
    输入：s = "deeedbbcccbdaa", k = 3
    输出："aa"
    解释：
    先删除 "eee" 和 "ccc"，得到 "ddbbbdaa"
    再删除 "bbb"，得到 "dddaa"
    最后删除 "ddd"，得到 "aa"
    示例 3：
    输入：s = "pbbcggttciiippooaais", k = 2
    输出："ps"
    提示：
    1 <= s.length <= 10^5
    2 <= k <= 10^4
    s 中只含有小写英文字母。
    """
    """
    # 递归
    def helper(s, k):
        if not s: return s
        last = s[0]
        sign = False
        ctr = 1
        i, n = 1, len(s)
        while i < n:
            if last == s[i]:
                ctr += 1
            else:
                last = s[i]
                ctr = 1
            i += 1
            if ctr == k:
                sign = True
                s = s[:i - ctr] + s[i:]
                i -= ctr
                n -= ctr
        return helper(s, k) if sign else s
    return helper(s, k)
    """
    # 栈
    stk = []
    for c in s:
        if not stk or stk[-1][0] != c:
            stk.append([c, 1])
        else:
            stk[-1][1] += 1
            if stk[-1][1] == k:
                stk.pop()
    return ''.join(e[0]*e[1] for e in stk)


if __name__ == '__main__':
    res = removeNearDuplicates("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4)
    print(res)
    # getMaximumGold([[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]])
    # longestSubsequence([4,12,10,0,-2,7,-8,9,-9,-12,-12,8,8], 0)
    # removeSubfolders(["/a/b/c","/a/b/d","/a/b/ca","/a/b/d/c"])
    # res = probabilityOfHeads([0.5], 0)
    # print(res)
    # res = minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8)
    # print(res)
    # b = search([1,3,1,1,1], 3)
    # print(b)
    # x = construct_list_node([1,1,2,3,3,4,5,5])
    # deleteDuplicates(x)
    # removeDuplicates([0,0,1,1,1,1,2,3,3,3])
    # a = minDistance("sea", "eat")
    # print(a)
    # triangleNumber([2,2,3,4])
    # a = findPaths(1,3,3,0,1)
    # print(a)
    # countNumbersWithUniqueDigits(10)
    # shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1])
    # arr = [10,2]
    # res = largerstNumber(arr)
    # s = "(ed(et(oc))el)"
    # reverseParentheses(s)
    pass