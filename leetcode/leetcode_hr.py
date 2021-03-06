# -*- coding:utf-8 -*-
import collections

from algorithm_utils import *

# leetcode 困难题


def crackSafe(n, k):
    """
    753. 破解保险箱
    有一个需要密码才能打开的保险箱。密码是 n 位数, 密码的每一位是 k 位序列 0, 1, ..., k-1 中的一个 。
    你可以随意输入密码，保险箱会自动记住最后 n 位输入，如果匹配，则能够打开保险箱。
    举个例子，假设密码是 "345"，你可以输入 "012345" 来打开它，只是你输入了 6 个字符.
    请返回一个能打开保险箱的最短字符串。
    示例1:
    输入: n = 1, k = 2
    输出: "01"
    说明: "10"也可以打开保险箱。
    示例2:
    输入: n = 2, k = 2
    输出: "00110"
    说明: "01100", "10011", "11001" 也能打开保险箱。
    提示：
    n 的范围是 [1, 4]。
    k 的范围是 [1, 10]。
    k^n 最大可能为 4096。
    :param n: int
    :param k: int
    :return: str
    """
    """
    # set 67%
    res = '0' * n
    s = set()
    s.add(res)
    for i in range(k ** n + 1):
        pre = res[len(res) - n + 1:]
        for j in range(k-1, -1, -1):
            cur = pre + str(j)
            if not cur in s:
                s.add(cur)
                res += str(j)
                break
    return res
    """
    # dfs
    def dfs():
        if (len(s) == total): return True
        nonlocal res
        pre = "".join(res[len(res) - n + 1:])
        for j in range(k):
            cur = pre + str(j)
            if cur not in s:
                res.append(str(j))
                s.add(cur)
                if dfs(): return True
                res.pop()
                s.remove(cur)
    res = ["0"] * n
    total = k ** n
    s = set()
    s.add("".join(res))
    return "".join(res) if dfs() else ""


def minStickers(stickers, target):
    """
    691. 贴纸拼词
    我们给出了 N 种不同类型的贴纸。每个贴纸上都有一个小写的英文单词。
    你希望从自己的贴纸集合中裁剪单个字母并重新排列它们，从而拼写出给定的目标字符串 target。
    如果你愿意的话，你可以不止一次地使用每一张贴纸，而且每一张贴纸的数量都是无限的。
    拼出目标 target 所需的最小贴纸数量是多少？如果任务不可能，则返回 -1。
    示例 1：
    输入：
    ["with", "example", "science"], "thehat"
    输出：
    3
    解释：
    我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
    把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
    此外，这是形成目标字符串所需的最小贴纸数量。
    示例 2：
    输入：
    ["notice", "possible"], "basicbasic"
    输出：
    -1
    解释：
    我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。
    提示：
    stickers 长度范围是 [1, 50]。
    stickers 由小写英文单词组成（不带撇号）。
    target 的长度在 [1, 15] 范围内，由小写字母组成。
    在所有的测试案例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选取的，目标是两个随机单词的串联。
    时间限制可能比平时更具挑战性。预计 50 个贴纸的测试案例平均可在35ms内解决。
    :param stickers: List[str]
    :param target: str
    :return: int
    """
    pass


def findIntegers(num):
    """
    600. 不含连续1的非负整数
    给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。
    示例 1:
    输入: 5
    输出: 5
    解释:
    下面是带有相应二进制表示的非负整数<= 5：
    0 : 0
    1 : 1
    2 : 10
    3 : 11
    4 : 100
    5 : 101
    其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
    说明: 1 <= n <= 109
    :param num: int
    :return: int
    """
    """
    # 找规律发现x=位数 答案是fib(x) 5%
    def fib(n):
        if n <= 0: return 1
        if n == 1: return 2
        a, b = 1, 2
        while n >= 1:
            b, a = a + b, b
            n -= 1
        return a
    if num == 0: return 1
    if num == 1: return 2
    c = 0
    while num >> c != 0:
        c += 1
    if num >> (c - 2) == 3:
        return fib(c)
    mask = (1 << (c - 1)) - 1
    return fib(c-1) + findIntegers(num & mask)
    """
    # 斐波那契数列通项公式 a(n) = 1/√5 * ((1+√5)/2)^n + ((1-√5)/2)^n 82%
    def fib(n):
        return int((d1 ** n - d2 ** n) / sqrt5)
    sqrt5 = 5 ** 0.5
    d1 = (1 + sqrt5) / 2
    d2 = (1 - sqrt5) / 2
    ans = 1
    flag = False
    for i in range(31, -1, -1):
        if num & (1 << i):
            ans += fib(i + 2)
            if flag: return ans - 1
            flag = True
        else:
            flag = False
    return ans


def largestPalindrome(n):
    """
    479. 最大回文数乘积
    你需要找到由两个 n 位数的乘积组成的最大回文数。
    由于结果会很大，你只需返回最大回文数 mod 1337得到的结果。
    示例:
    输入: 2
    输出: 987
    解释: 99 x 91 = 9009, 9009 % 1337 = 987
    说明:
    n 的取值范围为 [1,8]。
    :param n: int
    :return: int
    """
    """
    # 超时
    a, b = 10 ** (n - 1), 10**n - 1
    for z in range(b, a, -1):
        y = int(str(z) + str(z)[::-1])
        x = b
        while x * x > y:
            if y % x == 0:
                return int(y % 1337)
            x -= 1
    return 9
    """
    if n == 1: return 9
    for z in range(2, 2 * (9 * 10 ** n) - 1):
        left = 10 ** n - z
        right = int(str(left)[::-1])
        if z ** 2 - 4 * right < 0:
            continue
        else:
            root_1 = 1 / 2 * (z + (z ** 2 - 4 * right) ** 0.5)
            root_2 = 1 / 2 * (z - (z ** 2 - 4 * right) ** 0.5)
            if root_1.is_integer() or root_2.is_integer():
                return (10 ** n * left + right) % 1337


def removeBoxes(boxes):
    """
    546. 移除盒子
    给出一些不同颜色的盒子，盒子的颜色由数字表示，即不同的数字表示不同的颜色。
    你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 k 个盒子（k >= 1），这样一轮之后你将得到 k*k 个积分。
    当你将所有盒子都去掉之后，求你能获得的最大积分和。
    示例 1：
    输入:
    [1, 3, 2, 2, 2, 3, 4, 3, 1]
    输出:
    23
    解释:
    [1, 3, 2, 2, 2, 3, 4, 3, 1]
    ----> [1, 3, 3, 4, 3, 1] (3*3=9 分)
    ----> [1, 3, 3, 3, 1] (1*1=1 分)
    ----> [1, 1] (3*3=9 分)
    ----> [] (2*2=4 分)
    提示：盒子的总数 n 不会超过 100。
    :param boxes: List[int]
    :return: int
    """
    """
    # Top-Down
    def dfs(boxes, i, j, k):
        if i > j: return 0
        if memo[i][j][k]:
            return memo[i][j][k]
        while i < j and boxes[i] == boxes[i+1]:
            i += 1
            k += 1
        ans = dfs(boxes, i+1, j, 0) + (k+1) ** 2
        for m in range(i + 1, j + 1):
            if boxes[i] == boxes[m]:
                ans = max(ans, dfs(boxes, i+1, m-1, 0) + dfs(boxes, m, j, k+1))
        memo[i][j][k] = ans
        return ans

    n = len(boxes)
    memo = [[[0] * n for _ in range(n)] for _ in range(n)]
    return dfs(boxes, 0, n-1, 0)
    """
    # Bottom-Up
    n = len(boxes)
    if n == 0: return 0
    dp = [[[0] * n for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for k in range(j+1):
            dp[j][j][k] = (k+1) * (k+1)
    for l in range(1, n):
        for j in range(l, n):
            i = j - l
            for k in range(i+1):
                res = dp[i+1][j][0] + (k+1) ** 2
                for m in range(i+1, j+1):
                    if boxes[m] == boxes[i]:
                        res = max(res, dp[i+1][m-1][0] + dp[m][j][k+1])
                dp[i][j][k] = res
    return dp[0][n-1][0]


def intersectionSizeTwo(intervals):
    """
    757.  设置交集大小至少为2
    一个整数区间 [a, b]  ( a < b ) 代表着从 a 到 b 的所有连续整数，包括 a 和 b。
    给你一组整数区间intervals，请找到一个最小的集合 S，使得 S 里的元素与区间intervals中的每一个整数区间都至少有2个元素相交。
    输出这个最小集合S的大小。
    示例 1:
    输入: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
    输出: 3
    解释:
    考虑集合 S = {2, 3, 4}. S与intervals中的四个区间都有至少2个相交的元素。
    且这是S最小的情况，故我们输出3。
    示例 2:
    输入: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
    输出: 5
    解释:
    最小的集合S = {1, 2, 3, 4, 5}.
    注意:
    intervals 的长度范围为[1, 3000]。
    intervals[i] 长度为 2，分别代表左、右边界。
    intervals[i][j] 的值是 [0, 10^8]范围内的整数。
    :param intervals: List[List[int]]
    :return: int
    """
    # 贪心算法，遍历数组。
    # 先排序，以右边界为关键字排序，右边界相同的，按左边界降序排序，先处理长度较小的区间
    # 分三种情况，1二者完全没有交集，2二者有一个数字的交集，3有两个以上的数字交集。
    intervals.sort(key=lambda x: (x[1], -x[0]))
    print(intervals)
    res = [-1, -1]
    for x in intervals:
        if x[0] <= res[-2]:
            continue
        if x[0] > res[-1]:
            res.append(x[1] - 1)
        res.append(x[1])
    print(res)
    return len(res) - 2


def removeInvalidParentheses(s):
    """
    301. 删除无效的括号
    删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
    说明: 输入可能包含了除 ( 和 ) 以外的字符。
    示例 1:
    输入: "()())()"
    输出: ["()()()", "(())()"]
    示例 2:
    输入: "(a)())()"
    输出: ["(a)()()", "(a())()"]
    示例 3:
    输入: ")("
    输出: [""]
    :param s: str
    :return: List[str]
    """
    """
    # bfs 28%
    def is_valid(string):
        # 判断括号串是否合法
        l_minus_r = 0
        for c in string:
            if c == '(':
                l_minus_r += 1
            elif c == ')':
                l_minus_r -= 1
                if l_minus_r < 0:
                    return False
        return l_minus_r == 0

    level = {s}
    while True:
        valid = list(filter(is_valid, level))
        if valid:
            return valid
        level = {s[:i] + s[i + 1:] for s in level for i in range(len(s)) if s[i] in '()'}
    """
    # dfs 98%
    def is_valid(string):
        # 判断括号串是否合法
        l_minus_r = 0
        for c in string:
            if c == '(':
                l_minus_r += 1
            elif c == ')':
                l_minus_r -= 1
                if l_minus_r < 0:
                    return False
        return l_minus_r == 0

    def dfs(s, idx, l, r):
        if l == 0 and r == 0:
            if is_valid(s):
                res.append(s)
            return
        for i in range(idx, len(s)):
            # 跳过重复括号, 减少递归次数, 因为删除哪个后s都一样
            if i > idx and s[i] == s[i-1]:
                continue
            if r > 0:
                if s[i] == ')':
                    dfs(s[:i] + s[i+1:], i, l, r-1)
            else:
                if l > 0 and s[i] == '(':
                    dfs(s[:i] + s[i+1:], i, l-1, r)
    res = []
    l, r = 0, 0
    for c in s:
        if c == '(':
            l += 1
        elif c == ')':
            if l == 0:
                r += 1
            else:
                l -= 1
    dfs(s, 0, l, r)
    print(res)
    return res


def makeArrayIncreasing(arr1, arr2):
    """
    1187. 使数组严格递增
    给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。
    每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j < arr2.length，然后进行赋值运算 arr1[i] = arr2[j]。
    如果无法让 arr1 严格递增，请返回 -1。
    示例 1：
    输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
    输出：1
    解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。
    示例 2：
    输入：arr1 = [1,5,3,6,7], arr2 = [4,3,1]
    输出：2
    解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。
    示例 3：
    输入：arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
    输出：-1
    解释：无法使 arr1 严格递增。
    提示：
    1 <= arr1.length, arr2.length <= 2000
    0 <= arr1[i], arr2[i] <= 10^9
    :param arr1: List[int]
    :param arr2: List[int]
    :return: int
    """
    """
    import collections, bisect
    dp = {-1: 0}
    arr2.sort()
    for i in arr1:
        tmp = collections.defaultdict(lambda: float('inf'))
        for key in dp:
            if i > key:
                tmp[i] = min(tmp[i], dp[key])
            loc = bisect.bisect_right(arr2, key)
            if loc < len(arr2):
                tmp[arr2[loc]] = min(tmp[arr2[loc]], dp[key] + 1)
        dp = tmp
    print(dp)
    if dp:
        return min(dp.values())
    return -1
    """
    """
    # dp
    import bisect
    n = len(arr1)
    maxV = 1000000001
    dp = [[maxV for i in range(n + 1)] for _ in range(n + 1)]
    arr2.sort()
    dp[0][0] = -1
    for i in range(1, n + 1):
        for j in range(0, i + 1):
            if arr1[i - 1] > dp[j][i - 1]:
                dp[j][i] = arr1[i - 1]
            if j > 0:
                loc = bisect.bisect_right(arr2, dp[j - 1][i - 1])
                if loc < len(arr2):
                    dp[j][i] = min(dp[j][i], arr2[loc])
            if i == n and dp[j][i] != maxV:
                return j
    return -1
    """
    # dfs
    import bisect
    def dfs(i, prev):
        if i == len(arr1):
            return 0
        if (i, prev) in memo:
            return memo[(i, prev)]
        j = bisect.bisect_right(arr2, prev)
        if arr1[i] <= prev:
            if j >= len(arr2):
                res = 2001
            else:
                res = 1 + dfs(i+1, arr2[j])
        else:
            if j >= len(arr2) or arr2[j] >= arr1[i]:
                res = dfs(i+1, arr1[i])
            else:
                res = min(1 + dfs(i+1, arr2[j]), dfs(i+1, arr1[i]))
        memo[(i, prev)] = res
        return res
    arr2.sort()
    memo = {}
    res = dfs(0, -1)
    if res > 2000:
        return -1
    return res


def numPermsDISequence(S):
    """
    903. DI 序列的有效排列
    我们给出 S，一个源于 {'D', 'I'} 的长度为 n 的字符串 。（这些字母代表 “减少” 和 “增加”。）
    有效排列 是对整数 {0, 1, ..., n} 的一个排列 P[0], P[1], ..., P[n]，使得对所有的 i：
    如果 S[i] == 'D'，那么 P[i] > P[i+1]，以及；
    如果 S[i] == 'I'，那么 P[i] < P[i+1]。
    有多少个有效排列？因为答案可能很大，所以请返回你的答案模 10^9 + 7.
    示例：
    输入："DID"
    输出：5
    解释：
    (0, 1, 2, 3) 的五个有效排列是：
    (1, 0, 3, 2)
    (2, 0, 3, 1)
    (2, 1, 3, 0)
    (3, 0, 2, 1)
    (3, 1, 2, 0)
    提示：
    1 <= S.length <= 200
    S 仅由集合 {'D', 'I'} 中的字符组成。
    :param S: str
    :return: int
    """
    # https://leetcode.com/problems/valid-permutations-for-di-sequence/discuss/168278/C%2B%2BJavaPython-DP-Solution-O(N2)
    dp = [1] * (len(S) + 1)
    for c in S:
        if c == "I":
            dp = dp[:-1]
            for i in range(1, len(dp)):
                dp[i] += dp[i - 1]
        else:
            dp = dp[1:]
            for i in range(len(dp) - 1)[::-1]:
                dp[i] += dp[i + 1]
    return dp[0] % (10 ** 9 + 7)


def longestValidParentheses(s):
    """
    32. 最长有效括号
    给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
    示例 1:
    输入: "(()"
    输出: 2
    解释: 最长有效括号子串为 "()"
    示例 2:
    输入: ")()())"
    输出: 4
    解释: 最长有效括号子串为 "()()"
    :param s: str
    :return: int
    """
    n = len(s)
    stk, rec = [], [0] * n
    for i, c in enumerate(s):
        if c == '(':
            stk.append(i)
        elif stk:
            j = stk.pop()
            rec[j], rec[i] = 1, 1
    ans, m = 0, 0
    for i in rec:
        if i == 1:
            m += 1
        else:
            ans = max(m, ans)
            m = 0
    return max(m, ans)


def shortestPalindrome(s):
    """
    214. 最短回文串
    给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
    示例 1:
    输入: "aacecaaa"
    输出: "aaacecaaa"
    示例 2:
    输入: "abcd"
    输出: "dcbabcd"
    :param s: str
    :return: str
    """
    """
    # 暴力法
    n = len(s)
    rs = s[::-1]
    for i in range(1, n):
        ns = rs[:i] + s
        if ns[::-1] == ns:
            return ns
    """
    """
    # KMP
    def fail(s, f):
        f[0] = 0
        f[1] = 0
        for i in range(1, len(s)):
            j = f[i]
            while j and s[i] != s[j]:
                j = f[j]
            f[i+1] = j+1 if s[i] == s[j] else 0
    n = len(s)
    if n <= 1: return s
    r = s[::-1]
    sr = s + "#" + r
    f = [0] * (len(sr) + 1)
    fail(sr, f)
    return r[:len(r) - f[len(sr)]] + s
    """
    # Manacher
    n = len(s)
    if n < 2: return s
    t = "$#"
    for i in range(n):
        t += s[i]
        t += "#"
    p = [0] * (len(t) + 5)
    max_i = 0
    center, right = 0, 0
    window = 1
    for i in range(1, len(t)):
        if i<right:
            p[i] = min(p[2*center - i], right - i)
        while i + p[i] < len(t) and i - p[i] >= 1 and t[i+p[i]] == t[i-p[i]]:
            p[i] += 1
        if p[i] > p[max_i]:
            max_i = i
        if i + p[i] > right:
            right = i + p[i]
            center = i
        if (max_i - p[max_i]) // 2 == 0:
            window = max(window, p[max_i] - 1)
    if window == n: return s
    return s[window:][::-1] + s


def numMusicPlaylists(N, L, K):
    """
    920. 播放列表的数量
    你的音乐播放器里有 N 首不同的歌，在旅途中，你的旅伴想要听 L 首歌（不一定不同，即，允许歌曲重复）。请你为她按如下规则创建一个播放列表：
    每首歌至少播放一次。
    一首歌只有在其他 K 首歌播放完之后才能再次播放。
    返回可以满足要求的播放列表的数量。由于答案可能非常大，请返回它模 10^9 + 7 的结果。
    示例 1：
    输入：N = 3, L = 3, K = 1
    输出：6
    解释：有 6 种可能的播放列表。[1, 2, 3]，[1, 3, 2]，[2, 1, 3]，[2, 3, 1]，[3, 1, 2]，[3, 2, 1].
    示例 2：
    输入：N = 2, L = 3, K = 0
    输出：6
    解释：有 6 种可能的播放列表。[1, 1, 2]，[1, 2, 1]，[2, 1, 1]，[2, 2, 1]，[2, 1, 2]，[1, 2, 2]
    示例 3：
    输入：N = 2, L = 3, K = 1
    输出：2
    解释：有 2 种可能的播放列表。[1, 2, 1]，[2, 1, 2]
    提示：
    0 <= K < N <= L <= 100
    :param N: int
    :param L: int
    :param K: int
    :return: int
    """
    mod = 10 ** 9 + 7
    dp = [[0] * (N+1) for _ in range(L + 1)]
    dp[0][0] = 1
    for i in range(1, L+1):
        for j in range(1, N+1):
            dp[i][j] += dp[i-1][j-1] * (N - j + 1)
            dp[i][j] += dp[i-1][j] * max(j-K, 0)
            dp[i][j] %= mod
    return dp[L][N]



def maxProfit(k, prices):
    """
    188. 买卖股票的最佳时机 IV
    给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
    设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
    注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    示例 1:
    输入: [2,4,1], k = 2
    输出: 2
    解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
    示例 2:
    输入: [3,2,6,5,0,3], k = 2
    输出: 7
    解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
         随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
    :param k: int
    :param prices: List[int]
    :return: int
    """
    n = len(prices)
    if n == 0: return 0
    if k > n // 2:
        ans = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]
        return ans
    else:
        dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            for j in range(1, k+1):
                if i == 0:
                    dp[i][j][1] = -prices[i]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[n-1][k][0]


def minKBitFlips(A, K):
    """
    995. K 连续位的最小翻转次数
    在仅包含 0 和 1 的数组 A 中，一次 K 位翻转包括选择一个长度为 K 的（连续）子数组，同时将子数组中的每个 0 更改为 1，而每个 1 更改为 0。
    返回所需的 K 位翻转的次数，以便数组没有值为 0 的元素。如果不可能，返回 -1。
    示例 1：
    输入：A = [0,1,0], K = 1
    输出：2
    解释：先翻转 A[0]，然后翻转 A[2]。
    示例 2：
    输入：A = [1,1,0], K = 2
    输出：-1
    解释：无论我们怎样翻转大小为 2 的子数组，我们都不能使数组变为 [1,1,1]。
    示例 3：
    输入：A = [0,0,0,1,0,1,1,0], K = 3
    输出：3
    解释：
    翻转 A[0],A[1],A[2]: A变成 [1,1,1,1,0,1,1,0]
    翻转 A[4],A[5],A[6]: A变成 [1,1,1,1,1,0,0,0]
    翻转 A[5],A[6],A[7]: A变成 [1,1,1,1,1,1,1,1]
    提示：
    1 <= A.length <= 30000
    1 <= K <= A.length
    :param A: List[int]
    :param K: int
    :return: int
    """
    n = len(A)
    hint = [0] * n
    flip = 0
    ans = 0
    for i in range(n):
        flip ^= hint[i]
        if A[i] == flip:
            ans += 1
            if i + K > n: return -1
            flip ^= 1
            if i + K < n: hint[i + K] ^= 1
    return ans


def maxNumber(nums1, nums2, k):
    """
    321. 拼接最大数
    给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
    求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
    说明: 请尽可能地优化你算法的时间和空间复杂度。
    示例 1:
    输入:
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    输出:
    [9, 8, 6, 5, 3]
    示例 2:
    输入:
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
    输出:
    [6, 7, 6, 0, 4]
    示例 3:
    输入:
    nums1 = [3, 9]
    nums2 = [8, 9]
    k = 3
    输出:
    [9, 8, 9]
    :param nums1: List[int]
    :param nums2: List[int]
    :param k: int
    :return: List[int]
    """


def maxSumSubmatrix(matrix, k):
    """
    363. 矩形区域不超过 K 的最大数值和
    给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。
    示例:
    输入: matrix = [[1,0,1],[0,-2,3]], k = 2
    输出: 2
    解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
    说明：
    矩阵内的矩形区域面积必须大于 0。
    如果行数远大于列数，你将如何解答呢？
    :param matrix: List[List[int]]
    :param k: int
    :return: int
    """


def sumSubseqWidths(A):
    """
    891. 子序列宽度之和
    给定一个整数数组 A ，考虑 A 的所有非空子序列。
    对于任意序列 S ，设 S 的宽度是 S 的最大元素和最小元素的差。
    返回 A 的所有子序列的宽度之和。
    由于答案可能非常大，请返回答案模 10^9+7。
    示例：
    输入：[2,1,3]
    输出：6
    解释：
    子序列为 [1]，[2]，[3]，[2,1]，[2,3]，[1,3]，[2,1,3] 。
    相应的宽度是 0，0，0，1，1，2，2 。
    这些宽度之和是 6 。
    提示：
    1 <= A.length <= 20000
    1 <= A[i] <= 20000
    :param A: List[int]
    :return: int
    """
    """
    # 先排序再计算以A[i]结尾 - 以A[i]开头的结果数 * A[i]
    mod = 10 ** 9 + 7
    A.sort()
    n = len(A)
    ans = 0
    for i in range(n):
        l, r = 2 ** i, 2 ** (n-1-i)
        ans = (ans + (l - r) * A[i]) % mod
    return ans
    """
    # https://leetcode-cn.com/problems/sum-of-subsequence-widths/solution/zi-xu-lie-kuan-du-zhi-he-by-leetcode/
    mod = 10 ** 9 + 7
    A.sort()
    n = len(A)
    ans = 0
    p = 1
    for i in range(n):
        ans = (ans + (A[i] - A[n-1-i]) * p % mod) % mod
        p = (p << 1) % mod
    return ans


def findNumOfValidWords(words, puzzles):
    """
    1178. 猜字谜
    外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。
    字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：
    单词 word 中包含谜面 puzzle 的第一个字母。
    单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
    例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。
    返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。
    示例：
    输入：
    words = ["aaaa","asas","able","ability","actt","actor","access"],
    puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
    输出：[1,1,3,2,4,0]
    解释：
    1 个单词可以作为 "aboveyz" 的谜底 : "aaaa"
    1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"
    3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"
    2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"
    4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"
    没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。
    提示：
    1 <= words.length <= 10^5
    4 <= words[i].length <= 50
    1 <= puzzles.length <= 10^4
    puzzles[i].length == 7
    words[i][j], puzzles[i][j] 都是小写英文字母。
    每个 puzzles[i] 所包含的字符都不重复。
    :param words: List[str]
    :param puzzles: List[str]
    :return: List[int]
    """
    d = collections.Counter(filter(lambda w: len(w) <= 7, map(frozenset, words)))
    def f(p):
        cbt = [p[0]]
        for c in sorted(p[1:]):
            cbt += [s + c for s in cbt]
        return sum(d[s] for s in map(frozenset, cbt) if s in d)
    return [*map(f, puzzles)]

def minRefuelStops(target, startFuel, stations):
    """
    871. 最低加油次数
    汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。
    沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1] 升汽油。
    假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。
    当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。
    为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。
    注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。
    示例 1：
    输入：target = 1, startFuel = 1, stations = []
    输出：0
    解释：我们可以在不加油的情况下到达目的地。
    示例 2：
    输入：target = 100, startFuel = 1, stations = [[10,100]]
    输出：-1
    解释：我们无法抵达目的地，甚至无法到达第一个加油站。
    示例 3：
    输入：target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
    输出：2
    解释：
    我们出发时有 10 升燃料。
    我们开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
    然后，我们从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
    并将汽油从 10 升加到 50 升。然后我们开车抵达目的地。
    我们沿途在1两个加油站停靠，所以返回 2 。
    提示：
    1 <= target, startFuel, stations[i][1] <= 10^9
    0 <= stations.length <= 500
    0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target
    :param target: int
    :param startFuel: int
    :param stations: List[List[int]]
    :return: int
    """
    """
    # 动态规划
    dp = [startFuel] + [0] * len(stations)
    for i, (location, capacity) in enumerate(stations):
        for t in range(i, -1, -1):
            if dp[t] >= location:
                dp[t + 1] = max(dp[t + 1], dp[t] + capacity)
    for i, d in enumerate(dp):
        if d >= target: return i
    return -1
    """
    # 优先队列 heapq默认最小堆，使用取两次负值来实现最大堆的效果
    import heapq
    pq = []
    stations.append((target, float('inf')))
    ans = prev = 0
    tank = startFuel
    for location, capacity in stations:
        tank -= location - prev
        while pq and tank < 0:
            tank += -heapq.heappop(pq)
            ans += 1
        if tank < 0: return -1
        heapq.heappush(pq, -capacity)
        prev = location
    return ans


def superEggDrop(K, N):
    """
    887. 鸡蛋掉落
    你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
    每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
    你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
    每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
    你的目标是确切地知道 F 的值是多少。
    无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？
    示例 1：
    输入：K = 1, N = 2
    输出：2
    解释：
    鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
    否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
    如果它没碎，那么我们肯定知道 F = 2 。
    因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
    示例 2：
    输入：K = 2, N = 6
    输出：3
    示例 3：
    输入：K = 3, N = 14
    输出：4
    提示：
    1 <= K <= 100
    1 <= N <= 10000
    :param K: int
    :param N: int
    :return: int
    """
    """
    # 暴力 超时
    # 思路，无论K是何值都可以测试出来的尝试次数，等价于求所有情况中尝试次数最多的值
    # 那么就从1-N楼分别开始扔第一颗蛋，在所有计算结果中取min+1就是答案
    # 1-N楼分别扔蛋：
    # 当我在i层楼扔了个蛋，如果在N层楼扔的时候还有K个蛋的状态记作dp[K][N]的话，会有两种情况：
    # 1. 碎了：总数K-1，i层太高，从i-1层尝试：dp[K-1][i-1]
    # 2. 没碎：蛋没碎就可以重复使用，i层低了，从dp[K][i+1 -> N]尝试，由于i+1->N又可以把i+1层视为第1层
    #         等价于在总楼层数N-i的另一栋楼扔鸡蛋，也就是dp[K][N-i]
    def helper(K, N):
        # 只有1个鸡蛋需要试N次
        if N == 0 or N == 1 or K == 1:
            return N
        ans = N
        for i in range(1, N+1):
            t = max(helper(K-1, i-1), helper(K, N-i))
            ans = min(ans, 1+t)
        return ans
    return helper(K, N)
    """
    """
    # 动态规划 + 二分查找
    memo = {}
    def dp(k, n):
        if (k, n) not in memo:
            if n == 0:
                ans = 0
            elif k == 1:
                ans = n
            else:
                lo, hi = 1, n
                # keep a gap of 2 X values to manually check later
                while lo + 1 < hi:
                    x = (lo + hi) / 2
                    t1 = dp(k - 1, x - 1)
                    t2 = dp(k, n - x)
                    if t1 < t2:
                        lo = x
                    elif t1 > t2:
                        hi = x
                    else:
                        lo = hi = x
                ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x))
                              for x in (lo, hi))
            memo[k, n] = ans
        return memo[k, n]
    return dp(K, N)
    """
    # 动态规划
    # 思路：dp[k][n]表示k个鸡蛋在n步之内可以测出多少层
    dp = [[0] * (N+1) for _ in range(K+1)]
    for n in range(1, N+1):
        for k in range(1, K+1):
            dp[k][n] = dp[k][n-1] + dp[k-1][n-1] + 1
            if dp[k][n] >= N:
                return n
    return N


def orderlyQueue(S, K):
    """
    899. 有序队列
    给出了一个由小写字母组成的字符串 S。然后，我们可以进行任意次数的移动。
    在每次移动中，我们选择前 K 个字母中的一个（从左侧开始），将其从原位置移除，并放置在字符串的末尾。
    返回我们在任意次数的移动之后可以拥有的按字典顺序排列的最小字符串。
    示例 1：
    输入：S = "cba", K = 1
    输出："acb"
    解释：
    在第一步中，我们将第一个字符（“c”）移动到最后，获得字符串 “bac”。
    在第二步中，我们将第一个字符（“b”）移动到最后，获得最终结果 “acb”。
    示例 2：
    输入：S = "baaca", K = 3
    输出："aaabc"
    解释：
    在第一步中，我们将第一个字符（“b”）移动到最后，获得字符串 “aacab”。
    在第二步中，我们将第三个字符（“c”）移动到最后，获得最终结果 “aaabc”。
    提示：
    1 <= K <= S.length <= 1000
    S 只由小写字母组成。
    :param S: str
    :param K: int
    :return: str
    """
    if K == 1:
        return min(S[i:] + S[:i] for i in range(len(S)))
    return "".join(sorted(S))


def minCut(s):
    """
    132. 分割回文串 II
    给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
    返回符合要求的最少分割次数。
    示例:
    输入: "aab"
    输出: 1
    解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
    :param s: str
    :return: int
    """
    """
    # 略暴力的dp
    n = len(s)
    dp = [i + 1 for i in range(n + 1)]
    dp[0] = -1
    for i in range(n):
        for j in range(i + 1):
            if s[j:i + 1] == s[j:i + 1][::-1]:
                dp[i+1] = min(dp[i+1], dp[j] + 1)
    return dp[-1]
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    dp2 = list(range(len(s)))
    for i in range(n):
        for j in range(i + 1):
            if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                dp[j][i] = True
                if j == 0:
                    dp2[i] = 0
                else:
                    dp2[i] = min(dp2[i], dp2[j - 1] + 1)
    return dp2[-1]


if __name__ == '__main__':
    minCut("aab")
    # orderlyQueue("kuh", 1)
    # findNumOfValidWords(["aaaa","asas","able","ability","actt","actor","access"],["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"])
    # maxProfit(2, [6,1,3,2,4,7])
    # shortestPalindrome("aacecaaa")
    # makeArrayIncreasing([1,5,3,6,7], [4,3,1])
    # removeInvalidParentheses("()())()")
    # x = intersectionSizeTwo([[2,10],[3,7],[3,15],[4,11],[6,12],[6,16],[7,8],[7,11],[7,15],[11,12]])
    # print(x)
    # a = removeBoxes([1,3,2,2,2,3,4,3,1])
    # print(a)
    # largestPalindrome(1)
    # findIntegers(2)
    # y = crackSafe(2, 3)
    # print(y)
    # removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1])
    pass