from typing import List

from algorithm_utils import *

# leetcode困难题2

def numberToWords(num):
    """
    273. 整数转换英文表示
    将非负整数转换为其对应的英文表示。可以保证给定输入小于 231 - 1 。
    示例 1:
    输入: 123
    输出: "One Hundred Twenty Three"
    示例 2:
    输入: 12345
    输出: "Twelve Thousand Three Hundred Forty Five"
    示例 3:
    输入: 1234567
    输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    示例 4:
    输入: 1234567891
    输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
    :param num: int
    :return: str
    """
    twenty = " One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split(' ')
    ty = "  Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split(' ')
    hundred = "Hundred"
    unit = " Thousand Million Billion".split(' ')
    if num == 0: return "Zero"
    def recur(n, t):
        if n < 20:
            return [twenty[n], unit[t]]
        elif 20 <= n < 100:
            return [ty[n//10]] + recur(n%10, t)
        elif 100 <= n < 1000:
            return [twenty[n//100], hundred] + recur(n%100, t)
        else:
            return recur(n//1000, t+1) + recur(n%1000, t)
    res = [e for e in recur(num, 0) if e]
    j = len(res) - 1
    while j > 0:
        if res[j] in unit and res[j-1] in unit:
            res.pop(j)
        j -= 1
    print(res)
    return ' '.join(res)


def maximizeSweetness(sweetness: List[int], K: int) -> int:
    """
    5111. 分享巧克力
    你有一大块巧克力，它由一些甜度不完全相同的小块组成。我们用数组 sweetness 来表示每一小块的甜度。
    你打算和 K 名朋友一起分享这块巧克力，所以你需要将切割 K 次才能得到 K+1 块，每一块都由一些 连续 的小块组成。
    为了表现出你的慷慨，你将会吃掉 总甜度最小 的一块，并将其余几块分给你的朋友们。
    请找出一个最佳的切割策略，使得你所分得的巧克力 总甜度最大，并返回这个 最大总甜度。
    示例 1：
    输入：sweetness = [1,2,3,4,5,6,7,8,9], K = 5
    输出：6
    解释：你可以把巧克力分成 [1,2,3], [4,5], [6], [7], [8], [9]。
    示例 2：
    输入：sweetness = [5,6,7,8,9,1,2,3,4], K = 8
    输出：1
    解释：只有一种办法可以把巧克力分成 9 块。
    示例 3：
    输入：sweetness = [1,2,2,1,2,2,1,2,2], K = 2
    输出：5
    解释：你可以把巧克力分成 [1,2,2], [1,2,2], [1,2,2]。
    提示：
    0 <= K < sweetness.length <= 10^4
    1 <= sweetness[i] <= 10^5
    """
    n = len(sweetness)
    if K == n - 1: return min(sweetness)
    dp = [[[0] * (K+1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i][0] = sweetness[i]
        for j in range(i+1, n):
            dp[i][j][0] += dp[i][j-1][0] + sweetness[j]
    # for i in range(n):
    #     for j in range(i, n):
    #         print(dp[i][j][0], end=' ')
    #     print()
    for k in range(1, K+1):
        for left in range(n-k):
            for right in range(left, n):
                for i in range(left, right):
                    for w in range(k):
                        dp[left][right][k] = max(dp[left][right][k], min(dp[left][i][w], dp[i+1][right][k-w-1]))
    print(dp[0][n-1][K])
    return dp[0][n-1][K]




def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    """
    1235. 规划兼职工作
    你打算利用空闲时间来做兼职工作赚些零花钱。
    这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。
    给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。
    注意，时间上出现重叠的 2 份工作不能同时进行。
    如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。
    示例 1：
    输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
    输出：120
    解释：
    我们选出第 1 份和第 4 份工作，
    时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。
    示例 2：
    输入：startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
    输出：150
    解释：
    我们选择第 1，4，5 份工作。
    共获得报酬 150 = 20 + 70 + 60。
    示例 3：
    输入：startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
    输出：6
    提示：
    1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
    1 <= startTime[i] < endTime[i] <= 10^9
    1 <= profit[i] <= 10^4
    """
    arr = sorted(map(list, zip(startTime, endTime, profit)))
    n = len(arr)
    dp = [0] * n
    k, m = 0, 0
    res = 0
    for i in range(n):
        for j in range(k, i):
            if arr[i][0] >= arr[j][1]:
                # 保证m = max(m, dp[j])中所有的dp[j]只比较一次
                if j == k: k += 1
                m = max(m, dp[j])
        dp[i] = m + arr[i][2]
        res = max(res, dp[i])
    print(dp)
    return res


def countVowelPermutation(n: int) -> int:
    """
    1220. 统计元音字母序列的数目
    给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：
    字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
    每个元音 'a' 后面都只能跟着 'e'
    每个元音 'e' 后面只能跟着 'a' 或者是 'i'
    每个元音 'i' 后面 不能 再跟着另一个 'i'
    每个元音 'o' 后面只能跟着 'i' 或者是 'u'
    每个元音 'u' 后面只能跟着 'a'
    由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。
    示例 1：
    输入：n = 1
    输出：5
    解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
    示例 2：
    输入：n = 2
    输出：10
    解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。
    示例 3：
    输入：n = 5
    输出：68
    提示：
    1 <= n <= 2 * 10^4
    """
    mod = 10 ** 9 + 7
    a, e, i, o, u = 1, 1, 1, 1, 1
    for _ in range(2, n+1):
        a, e, i, o, u = (e+i+u) % mod, (i+a) % mod, (o+e) % mod, i, (i+o) % mod
    return sum((a,e,i,o,u)) % mod


def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    """
    126. 单词接龙 II
    给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
    每次转换只能改变一个字母。
    转换过程中的中间单词必须是字典中的单词。
    说明:
    如果不存在这样的转换序列，返回一个空列表。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
    示例 1:
    输入:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]
    输出:
    [
      ["hit","hot","dot","dog","cog"],
      ["hit","hot","lot","log","cog"]
    ]
    示例 2:
    输入:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    输出: []
    解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
    """
    from collections import defaultdict
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return []
    # 构造下一步的字典，将每个字符替换成*在wordList查找模式串相匹配的所有单词
    d = defaultdict(list)
    l = len(beginWord)
    for w in wordList:
        for i in range(l):
            d[w[:i] + '*' + w[i+1:]].append(w)
    # 双向bfs求解res数组
    stk_start = {beginWord: [[beginWord]]}
    stk_end = {endWord: [[endWord]]}
    # 初始值为(begin -> end):2
    step = 2
    vis = set()
    res = []
    while stk_start:
        # 每次进入循环是一个step
        # 如果对向分支更少，则优先执行对向的step
        if len(stk_end) < len(stk_start):
            stk_end, stk_start = stk_start, stk_end
        tmp = {}
        while stk_start:
            word, paths = stk_start.popitem()
            vis.add(word)
            for i in range(l):
                c = word[:i] + '*' + word[i+1:]
                for e in d[c]:
                    if e in stk_end:
                        # 通过path的首元素是否为beginWord判断当前是正向还是反向
                        if paths[0][0] == beginWord: # forward
                            res.extend(head + tail[::-1] for head in paths for tail in stk_end[e])
                        else: # backward
                            res.extend(head + tail[::-1] for tail in paths for head in stk_end[e])
                    # bfs特性，被访问过的step一定当前step小
                    if not e in vis:
                        tmp[e] = tmp.get(e, []) + [path + [e] for path in paths]
        step += 1
        if res and step > len(res[0]): break
        stk_start = tmp
    return res


def tilingRectangle(n: int, m: int) -> int:
    """
    5241. 铺瓷砖
    你是一位施工队的工长，根据设计师的要求准备为一套设计风格独特的房子进行室内装修。
    房子的客厅大小为 n x m，为保持极简的风格，需要使用尽可能少的 正方形 瓷砖来铺盖地面。
    假设正方形瓷砖的规格不限，边长都是整数。
    请你帮设计师计算一下，最少需要用到多少块方形瓷砖？
    示例 1：
    输入：n = 2, m = 3
    输出：3
    解释：3 块地砖就可以铺满卧室。
         2 块 1x1 地砖
         1 块 2x2 地砖
    示例 2：
    输入：n = 5, m = 8
    输出：5
    示例 3：
    输入：n = 11, m = 13
    输出：6
    提示：
    1 <= n <= 13
    1 <= m <= 13
    """
    def fit(x, y, size):
        xs, ys = x + size, y + size
        for i in range(x, xs+1):
            for j in range(y, ys+1):
                if table[i] & (1 << j) != 0:
                    return False
        return True

    def dfs(table, count):
        nonlocal res
        # 剪枝
        if count >= res: return
        # 找本次需要拼图的左上角坐标
        x, y = -1, -1
        flag = False
        for i in range(n):
            for j in range(m):
                if table[i] & (1 << j) == 0:
                    x, y = i, j
                    flag = True
                    break
            if flag: break
        if flag == False:
            res = min(res, count)
            return
        # 找能放的最大块
        k = 0
        while x + k < n and y + k < m and fit(x, y, k):
            k += 1
        k -= 1
        # 通常选择较大的块容易先得到最优解，所以从大到小尝试，方便剪枝
        while k >= 0:
            # 放入瓷砖
            for i in range(x, x+k+1):
                for j in range(y, y+k+1):
                    table[i] |= (1 << j)
            # 递归
            dfs(table, count+1)
            # 回溯，取下瓷砖
            for i in range(x, x+k+1):
                for j in range(y, y+k+1):
                    table[i] -= (1 << j)
            k -= 1

    table = [0] * n
    # 13*13=169
    res = 170
    dfs(table, 0)
    return res


def findMin(nums: List[int]) -> int:
    """
    154. 寻找旋转排序数组中的最小值 II
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
    请找出其中最小的元素。
    注意数组中可能存在重复的元素。
    示例 1：
    输入: [1,3,5]
    输出: 1
    示例 2：
    输入: [2,2,2,0,1]
    输出: 0
    说明：
    这道题是 寻找旋转排序数组中的最小值 的延伸题目。
    允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
    """
    i, j = 0, len(nums) - 1
    while i < j:
        m = i + (j - i) // 2
        if nums[i] <= nums[m] <= nums[j]:
            i = m + 1
        else:
            j = m
    return nums[i]


if __name__ == '__main__':
    r = tilingRectangle(11, 13)
    print(r)
    # x = findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    # print(x)
    # x = countVowelPermutation(5)
    # print(x)
    # jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70])
    # maximizeSweetness([8,13,20,1,16], 3)
    # numberToWords(1000)
    pass
