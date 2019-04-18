# -*-coding:utf-8-*-
# leetcode.py 内容太杂了，新起一个leetcode2.py

# 数数字，1->11->21->1211->.....
# 1 -> 11(1个1)
# 11 -> 21(2个1)
def counting_nums(t):
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
    for _ in range(t - 1):
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
    pass


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

if __name__ == "__main__":
    # a = [[1,3,1],[1,5,1],[4,2,1]]
    # r = minPathSum(a)
    # print(r)
    # r = countBits(5)
    # print(r)
    print(twoSum([-1, 0], -1))