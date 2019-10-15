# -*- coding: utf-8 -*-
# ======================================
# @File    : leetcode_nm3.py
# @Time    : 2019/10/3 22:54
# @Author  : Rivarrl
# ======================================

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



if __name__ == '__main__':
    a = findPaths(1,3,3,0,1)
    print(a)
    # countNumbersWithUniqueDigits(10)
    # shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1])
    # arr = [10,2]
    # res = largerstNumber(arr)
    # s = "(ed(et(oc))el)"
    # reverseParentheses(s)
    pass