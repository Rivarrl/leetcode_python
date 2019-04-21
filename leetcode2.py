# -*-coding:utf-8-*-
import algorithm_utils as alg
from algorithm_utils import ListNode

# leetcode.py 内容太杂了，新起一个leetcode2.py

# 数数字，1->11->21->1211->.....
# 1 -> 11(1个1)
# 11 -> 21(2个1)
def countAndSay(n):
    """
    LC38
    报数
    报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 被读作  "one 1"  ("一个一") , 即 11。
    11 被读作 "two 1s" ("两个一"）, 即 21。
    21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
    给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
    注意：整数顺序将表示为一个字符串。
    :param n: int
    :return: str
    """
    def inner(num):
        l = num.__len__()
        res = ""
        i = 0
        while i < l:
            j = i
            count = 0
            while num[j] == num[i]:
                j += 1
                count += 1
                if j == l:
                    break
            res += str(count) + num[i]
            i = j
        return res

    result = "1"
    for _ in range(n - 1):
        result = inner(result)
    return result


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = nums.__len__()
    if l <= 1:
        return l
    i = 0
    while i < l - 1:
        if nums[i] == nums[i + 1]:
            nums.remove(nums[i + 1])
            l -= 1
        else:
            i += 1
    return l


def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    int_max = 2 ** 31 - 1
    int_min = -2 ** 31
    ls = str.strip('"').lstrip()
    i, k = 0, 0
    if ls.__len__() == 0 or (ls.__len__() == 1 and ls[0] == '-'):
        return 0
    try:
        _ = int(ls[0])
    except:
        if ls[0] == '-':
            i, k = 1, 1
        elif ls[0] == '+':
            i, k = 1, 2
        else:
            return 0
    while i < ls.__len__():
        if isint(ls[i]):
            i += 1
        else:
            # i -= 1
            break
    if i == 0:
        if k == 1 or k == 2:
            return 0
        else:
            return int(ls[0])
    res = ls[1:i] if k == 2 else ls[:i]
    if isint(res):
        if int(res) < int_min:
            return int_min
        elif int(res) > int_max:
            return int_max
        else:
            if res.rstrip('0') == '-':
                return 0
            return int(res)
    return 0


def isint(i):
    try:
        _ = int(i)
        return True
    except:
        return False


def countBits(num):
    """
    LC338
    比特位计数
    给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
    输入: 5
    输出: [0,1,1,2,1,2]
    进阶:
    给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
    要求算法的空间复杂度为O(n)。
    你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数
    思路:
    动态规划，选用的思路1
    1) ans[i] = ans[i >> 1] + (i & 1)   # 取右移后的数一定比当前值小
    2) ans[i] = ans[i & (i - 1)] + 1    # i & (i - 1) < i
    3) ans[i*2] = ans[i]                # 注意越界问题
       ans[i*2+1] = ans[i] + 1
    :param num: int
    :return: List[int]
    """
    ans = [0 for _ in range(num + 1)]
    for i in range(1, num + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


def minPathSum(grid):
    """
    LC64
    最小路径和
    给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
    说明：每次只能向下或者向右移动一步。
    输入: [[1,3,1],
          [1,5,1],
          [4,2,1]]
    输出: 7
    解释: 因为路径 1→3→1→1→1 的总和最小。
    :param grid: List[List[int]]
    :return: int
    """
    row = grid.__len__()
    if row == 0:
        return 0
    col = grid[0].__len__()
    dp = [[0 for _ in range(col)] for _ in range(row)]
    r_sum, c_sum = 0, 0
    for i in range(row):
        for j in range(col):
            if i == 0 or j == 0:
                if i == 0:
                    r_sum += grid[i][j]
                    dp[i][j] = r_sum
                if j == 0:
                    c_sum += grid[i][j]
                    dp[i][j] = c_sum
            else:
                dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])
    return dp[-1][-1]


def countSubstrings(s):
    """
    LC647
    回文子串数
    给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
    具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
    示例:
    1.
    输入: "abc"
    输出: 3
    解释: 三个回文子串: "a", "b", "c".
    2.
    输入: "aaa"
    输出: 6
    说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
    :param s: str
    :return: int
    """
    l = len(s)
    dp = [[0] * l for _ in range(l)]
    ans = 0
    for i in range(l):
        for j in range(i, -1, -1):
            if s[i] == s[j] and (i - j + 1 <= 2 or dp[i - 1][j + 1]):
                dp[i][j] = 1
                ans += 1
    return ans


def countSubstrings2(s):
    """
    LC647
    44ms
    :param s:
    :return:
    """
    num = 0
    n, i = len(s), 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        d = j - i
        num += d * (d + 1) // 2
        il, ir = i - 1, j
        while il >= 0 and ir < n and s[il] == s[ir]:
            num += 1
            il, ir = il - 1, ir + 1
        i = j
    return num


def numDecodings(s):
    """
    LC91
    解码方法
    一条包含字母 A-Z 的消息通过以下方式进行了编码：
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    给定一个只包含数字的非空字符串，请计算解码方法的总数。
    示例:
    输入: "12"
    输出: 2
    解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
    思路: 举例找规律发现，题目类似于带有限制条件的Fibonacci数列
    :param s: str
    :return: int
    """
    l = len(s)
    dp = [0] * (l + 1)
    dp[0] = 1
    for i in range(l):
        dp[i + 1] = 0 if s[i] == '0' else dp[i]
        if i == 0:
            continue
        if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
            dp[i + 1] += dp[i - 1]
    return dp[-1]


def minimumTotal(triangle):
    """
    LC120
    三角形最小路径和
    给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
    例如，给定三角形：
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
    :param triangle:
    :return:
    """
    l = len(triangle)
    if l == 0: return 0
    i, j = 0, l - 2
    while j >= 0:
        triangle[j][i] += min(triangle[j + 1][i], triangle[j + 1][i + 1])
        i += 1
        if i > j:
            j -= 1
            i = 0
    return triangle[0][0]


def numSquares(n):
    """
    LC279
    完全平方数 (超时)
    给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
    输入: n = 12
    输出: 3
    解释: 12 = 4 + 4 + 4.
    输入: n = 13
    输出: 2
    解释: 13 = 4 + 9.
    :param n: int
    :return: int
    """
    if not n: return n
    inf = 2 ** 31
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        j, j2, m = 1, 1, inf
        while j2 <= i:
            m = min(dp[i - j2], m)
            j += 1
            j2 = j ** 2
        dp[i] = m + 1
    return dp[-1]


def numSquares2(n):
    """
    LC279
    完全平方数
    思路:
    四平方定理:
    任何一个正整数都可以表示成不超过四个整数的平方之和。
    推论: 满足四数平方和定理的数n(四个整数的情况), 必定满足 n=4^a(8b+7)
    :param n: int
    :return: int
    """
    while n % 4 == 0:
        n /= 4
    if n % 8 == 7:
        return 4
    a = 0
    while a ** 2 <= n:
        b = int((n - a ** 2) ** 0.5)
        if a ** 2 + b ** 2 == n:
            return (not not a) + (not not b)
        a += 1
    return 3


def mySqrt(x):
    """
    LC69
    x的平方根
    手写sqrt函数
    思路:
    牛顿迭代法求平方根下限整数
    https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division
    :param x:
    :return:
    """
    if x <= 1:
        return x
    r = x
    while r > x / r:
        r = (r + x / r) // 2
    return int(r)


def twoSum(numbers, target):
    """
    LC167
    给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
    函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
    说明:
    返回的下标值（index1 和 index2）不是从零开始的。
    你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
    示例:
    输入: numbers = [2, 7, 11, 15], target = 9
    输出: [1,2]
    解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
    :param numbers: List[int]
    :param target: int
    :return: List[int]
    """
    l = len(numbers)
    d = {}
    for i in range(l):
        tgt = target - numbers[i]
        if tgt in d:
            return [d[tgt] + 1, i + 1]
        d[numbers[i]] = i



def maxProfit(prices):
    """
    LC309
    给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
    设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
    你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
    示例:
    输入: [1,2,3,0,2]
    输出: 3
    解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
    :param prices: List[int]
    :return: int
    """
    l = len(prices)
    dp = [0] * l
    m = [0] * l
    n = 0
    if l < 2: return 0
    for i in range(1, l):
        c = prices[i] - prices[i - 1]
        if i < 3:
            dp[i] = max(dp[i-1] + c, 0)
        else:
            if c > 0:
                dp[i] = max(m[i-3], dp[i-1]) + c
            else:
                dp[i] = max(dp[i-1] + c, 0)
        n = max(n, dp[i])
        m[i] = n
    return n


def threeSum(nums):
    """
    LC15
    三数之和 (超时) O(n^3)
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
    注意：答案中不可以包含重复的三元组。
    例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
    满足要求的三元组集合为：
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
    :param nums: List[int]
    :return: List[List[int]]
    """
    l = len(nums)
    if l == 0: return []
    nums.sort()
    res = []
    for k in range(l):
        for j in range(k+1, l):
            for i in range(j+1, l):
                if nums[k] + nums[j] + nums[i] == 0:
                    b = sorted([nums[k], nums[j], nums[i]])
                    if not b in res:
                        res.append(b)
                    break
    return res


def threeSum2(nums):
    """
    LC15
    三数之和 (双指针法) O(n^2)
    :param nums: List[int]
    :return: List[List[int]]
    """
    nums.sort()
    l = len(nums)
    res = []
    k = 0
    while k < l:
        i, j = k + 1, l - 1
        s = nums[k]
        while i < j:
            if nums[i] + nums[j] == -s:
                res.append([nums[i], nums[j], s])
                i += 1
                j -= 1
                while nums[i] == nums[i-1]:
                    i += 1
                    if i >= j:
                        break
                while nums[j] == nums[j+1]:
                    j -= 1
                    if j <= i:
                        break
            elif nums[i] + nums[j] < -s:
                i += 1
            else:
                j -= 1
        while k + 1 < l and nums[k+1] == s:
            k += 1
        k += 1
    return res


def strStr(haystack, needle):
    """
    LC28
    实现strStr() (O(n*p))
    给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
    输入: haystack = "hello", needle = "ll"
    输出: 2
    输入: haystack = "aaaaa", needle = "bba"
    输出: -1
    :param haystack: str
    :param needle: str
    :return: int
    """
    h = 0
    l = len(haystack)
    nl = len(needle)
    if nl > l: return -1
    if haystack == needle: return 0
    if nl == 0: return 0
    while h < l:
        i = 0
        t = h
        while haystack[t] == needle[i]:
            t += 1
            i += 1
            if i == nl:
                return h
            if t == l:
                return -1
        h += 1
    return -1


def strStr2(haystack, needle):
    """
    LC28
    实现strStr() (O(n+p))
    KMP算法
    :param haystack:
    :param needle:
    :return:
    """
    l = len(haystack)
    nl = len(needle)
    if nl > l: return -1
    if haystack == needle: return 0
    if nl == 0: return 0
    f = [-1] * nl
    k = -1
    for j in range(1, nl):
        while k > -1 and needle[k + 1] != needle[j]:
            k = f[k]
        if needle[k + 1] == needle[j]:
            k += 1
        f[j] = k
    i, j = 0, 0
    while i < l and j < nl:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = f[j-1] + 1
    return i - nl if j == nl else -1


def mergeTwoLists(l1, l2):
    """
    LC21
    合并两个有序链表
    将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
    :param l1: ListNode
    :param l2: ListNode
    :return: ListNode
    """
    if not l1: return l2
    if not l2: return l1
    res = ListNode(0)
    p = res
    while l1 and l2:
        if l1.val <= l2.val:
            p.next = l1
            p = p.next
            l1 = l1.next
        else:
            p.next = l2
            p = p.next
            l2 = l2.next
    if l1:
        p.next = l1
        p = p.next
    if l2:
        p.next = l2
        p = p.next
    return res.next


def fourSum(nums, target):
    """
    LC18
    四数之和
    给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
    答案中不可以包含重复的四元组。
    给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
    满足要求的四元组集合为：
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]
    :param nums:
    :param target:
    :return:
    """
    def check(rs):
        xd = {}
        for r in rs:
            if not r in xd:
                xd[r] = 0
            xd[r] += 1
            if xd[r] > c[r]:
                return False
        return True
    d = {}
    c = {}
    m = []
    res = []
    l = len(nums)
    if l < 4: return res
    for i in range(l):
        if not nums[i] in c:
            c[nums[i]] = 0
        c[nums[i]] += 1
    if target == 0 and 0 in c and c[0] >= 4:
        res.append([0,0,0,0])
    for i in range(l):
        for j in range(i + 1, l):
            s = nums[i] + nums[j]
            sr = sorted([nums[i], nums[j]])
            if not s in d:
                d[s] = [sr]
                m.append(s)
            else:
                if not sr in d[s]:
                    d[s].append(sr)
    lm = len(m)
    m.sort()
    print(d)
    print(m)
    print(c)
    i, j = 0, lm - 1
    while i <= j:
        if m[i] + m[j] == target:
            if i == j:
                li = len(d[m[i]])
                for ii in range(li):
                    for jj in range(ii, li):
                        [xi, yi], [xj, yj] = d[m[i]][ii], d[m[i]][jj]
                        rs = sorted([xi, yi, xj, yj])
                        if not rs in res and check(rs):
                            res.append(rs)
            else:
                for xi, yi in d[m[i]]:
                    for xj, yj in d[m[j]]:
                        rs = sorted([xi, yi, xj, yj])
                        if not rs in res and check(rs):
                            res.append(rs)
            i += 1
            j -= 1
        elif m[i] + m[j] > target:
            j -= 1
        else:
            i += 1
    return res


def fourSumCount(A, B, C, D):
    """
    LC454
    四数相加Ⅱ
    给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
    为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1。
    输入:
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    输出:
    2
    解释:
    两个元组如下:
    1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
    2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
    :param A: List[int]
    :param B: List[int]
    :param C: List[int]
    :param D: List[int]
    :return: int
    """
    n = 0
    e = dict()
    for a in A:
        for b in B:
            e[a + b] = e.get(a + b, 0) + 1
    for c in C:
        for d in D:
            s = -(c + d)
            if s in e:
                n += e[s]
    return n


def searchInsert(nums, target):
    """
    LC35
    搜索插入位置
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    你可以假设数组中无重复元素。
    输入: [1,3,5,6], 5
    输出: 2
    :param nums: List[int]
    :param target: int
    :return: int
    """
    l = len(nums)
    i, j = 0, l - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] < target:
            i = mid + 1
        elif nums[mid] > target:
            j = mid - 1
        else:
            return mid
    return i


def myPow(x, n):
    """
    LC50
    Pow(x,n)
    实现 pow(x, n) ，即计算 x 的 n 次幂函数。
    思路:
    当n可以被2整除时将n折半, x=x*x. 例如: 2^4 = 4^2
    当n不能被2整除时n//=2, res*=x
    :param x: float
    :param n: int
    :return: float
    """
    i, res = abs(n), 1.0
    while i != 0:
        if i % 2 != 0:
           res *= x
        x *= x
        i //= 2
    return res if n > 0 else 1/res


def myPow2(x, n):
    """
    LC50
    Pow(x,n)
    递归解法
    :param x: float
    :param n: int
    :return: float
    """
    if n == 0: return 1
    if n == 1: return x
    if n == -1: return 1/x
    res = myPow2(x, n//2)
    res *= res
    res *= myPow2(x, n-(2*n//2))
    return res


def permuteUnique(nums):
    """
    LC47
    全排列Ⅱ
    给定一个可包含重复数字的序列，返回所有不重复的全排列。
    输入: [1,1,2]
    输出:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]
    :param nums: List[int]
    :return: List[List[int]]
    """
    def inner(ns):
        cur = []
        if len(ns) == 1:
            cur.append(ns)
        else:
            for i, x in enumerate(ns):
                if i >= 1 and ns[i - 1] == ns[i]:
                    continue
                rs = ns[:i] + ns[i + 1:]
                for r in inner(rs):
                    cur.append([x] + r)
        return cur
    nums.sort()
    res = inner(nums)
    return res


def rotate(matrix):
    """
    LC48
    旋转图像
    给定一个 n × n 的二维矩阵表示一个图像。
    将图像顺时针旋转 90 度。
    你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
        给定 matrix =
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ],

    原地旋转输入矩阵，使其变为:
    [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]
    :param matrix: List[List[int]]
    :return: None
    """
    pass


def groupAnagrams(strs):
    """
    LC49
    字母异位词分组
    给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
    输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
    输出:
    [
      ["ate","eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
    所有输入均为小写字母。
    不考虑答案输出的顺序。
    :param strs:
    :return:
    """
    pass

if __name__ == "__main__":
    # a = [[1,3,1],[1,5,1],[4,2,1]]
    # r = minPathSum(a)
    # print(r)
    # r = countBits(5)
    # print(r)
    # print(threeSum2([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
    # print(strStr("aabaaabaaac", "aabaaac"))
    # a = ListNode(0)
    # b = a
    # for x in [1,2,4]:
    #     next = ListNode(x)
    #     b.next = next
    #     b = b.next
    # c = ListNode(0)
    # b = c
    # for x in [1,3,4]:
    #     next = ListNode(x)
    #     b.next = next
    #     b = b.next
    # print(mergeTwoLists(a.next, c.next))
    # print(fourSum([-7,-5,0,7,1,1,-10,-2,7,7,-2,-6,0,-10,-5,7,-8,5], 28))
    # print(fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
    # print(strStr2("abababaababda", "babaaba"))
    # print(searchInsert([1,3,5,6], 4))
    print(permuteUnique([1,1,2]))