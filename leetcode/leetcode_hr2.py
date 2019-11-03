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
        if nums[m] > nums[j]:
            i = m + 1
        elif nums[m] < nums[j]:
            j = m
        else:
            j -= 1
    return nums[i]


def maxPoints(points: List[List[int]]) -> int:
    """
    149. 直线上最多的点数
    给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
    示例 1:
    输入: [[1,1],[2,2],[3,3]]
    输出: 3
    解释:
    ^
    |
    |        o
    |     o
    |  o  
    +------------->
    0  1  2  3  4
    示例 2:
    输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    输出: 4
    解释:
    ^
    |
    |  o
    |     o        o
    |        o
    |  o        o
    +------------------->
    0  1  2  3  4  5  6
    """
    # 先把重复的点统计出来，再对不重复的每个点分别用字典存储斜率和次数，记录整体点数最高者
    def gcd(x, y):
        if x == 0: return y
        return gcd(y%x, x)
    from collections import Counter, defaultdict
    ctr = Counter(tuple(point) for point in points)
    unique_points = list(ctr.keys())
    n = len(unique_points)
    if n == 1: return ctr[unique_points[0]]
    res = 0
    for i in range(n-1):
        x1, y1 = unique_points[i]
        d = defaultdict(int)
        for j in range(i+1, n):
            x2, y2 = unique_points[j]
            dx, dy = x1 - x2, y1 - y2
            key = "inf"
            if dx != 0:
                g = gcd(dx, dy)
                key = "{}/{}".format(dy//g, dx//g)
            d[key] += ctr[unique_points[j]]
        # 加上自身重复的点数
        res = max(res, max(d.values()) + ctr[unique_points[i]])
        print(res)
    return res


def lastSubstring(s: str) -> str:
    """
    1163. 按字典序排在最后的子串
    给你一个字符串 s，找出它的所有子串并按字典序排列，返回排在最后的那个子串。
    示例 1：
    输入："abab"
    输出："bab"
    解释：我们可以找出 7 个子串 ["a", "ab", "aba", "abab", "b", "ba", "bab"]。按字典序排在最后的子串是 "bab"。
    示例 2：
    输入："leetcode"
    输出："tcode"
    提示：
    1 <= s.length <= 10^5
    s 仅含有小写英文字符。
    """
    # 找最大后缀字符串
    # left找全局最大字典序子串的起始点，right尝试找比left更大的字典序作为新起始点
    n, left, right, step = len(s), 0, 1, 0
    while right + step < n:
        if s[right + step] > s[left + step]:
            left, right, step = right, right + 1, 0
        elif s[right + step] < s[left + step]:
            right, step = right + step + 1, 0
        else:
            step += 1
    return s[left:]


def sortItems(n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
    """
    1203. 项目管理
    公司共有 n 个项目和  m 个小组，每个项目要不没有归属，要不就由其中的一个小组负责。
    我们用 group[i] 代表第 i 个项目所属的小组，如果这个项目目前无人接手，那么 group[i] 就等于 -1。（项目和小组都是从零开始编号的）
    请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：
    同一小组的项目，排序后在列表中彼此相邻。
    项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个项目左侧）应该完成的所有项目。
    结果要求：
    如果存在多个解决方案，只需要返回其中任意一个即可。
    如果没有合适的解决方案，就请返回一个 空列表。
    示例 1：
    输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
    输出：[6,3,4,1,5,2,0,7]
    示例 2：
    输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
    输出：[]
    解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。
    提示：
    1 <= m <= n <= 3*10^4
    group.length == beforeItems.length == n
    -1 <= group[i] <= m-1
    0 <= beforeItems[i].length <= n-1
    0 <= beforeItems[i][j] <= n-1
    i != beforeItems[i][j]
    """
    # 项目间有依赖关系，可以用拓扑排序解决
    # 但由于项目属于不同分组，最后要求同组项目相邻，也就是每组也有依赖关系
    # 分别对组间依赖和组内依赖做拓扑排序即可，任一环节出现环就返回空数组
    # 由于无组的项目可以随意被依赖，可视为每个项目单独一组
    for i in range(n):
        if group[i] == -1:
            group[i] = m
            m += 1
    indegree_group = [0 for _ in range(m)] # 组间入度
    indegree_item = [0 for _ in range(n)]
    graph_group = [set() for _ in range(m)]
    graph_item = [set() for _ in range(n)]
    group_data = [set() for _ in range(m)]
    # 存放组与项目的关系
    for i in range(n):
        group_data[group[i]].add(i)

    work_group = [i for i in range(m) if len(group_data[i]) > 0]

    # 以组和项目为单位分别构图并计算各节点入度
    for i in range(n):
        for j in beforeItems[i]:
            if group[i] == group[j]:
                # 属于组内图
                indegree_item[i] += 1
                graph_item[j].add(i)
            else:
                # 属于组间图
                if not group[i] in graph_group[group[j]]:
                    indegree_group[group[i]] += 1
                    graph_group[group[j]].add(group[i])
    # 组间拓扑排序
    q = [i for i in range(m) if indegree_group[i] == 0]
    print(q)
    # 判断有无环
    if len(q) == 0: return []
    seq = []
    while q:
        p = q.pop()
        seq.append(p)
        for i in graph_group[p]:
            indegree_group[i] -= 1
            if indegree_group[i] == 0:
                q.insert(0, i)
    print(seq)
    print(indegree_group)
    # 判断有无环
    if len(seq) < len(indegree_group): return []

    # 各组组内拓扑排序
    for k in work_group:
        q = [i for i in group_data[k] if indegree_item[i] == 0]
        # 判断有无环
        if len(q) == 0: return []
        _seq = []
        while q:
            p = q.pop()
            _seq.append(p)
            for i in graph_item[p]:
                indegree_item[i] -= 1
                if indegree_item[i] == 0:
                    q.insert(0, i)
        # 判断有无环
        if len(_seq) < len(group_data[k]): return []
        group_data[k] = _seq
    res = []
    for i in range(m):
        res += group_data[seq[i]]
    return res


def minimumMoves(grid: List[List[int]]) -> int:
    """
    1210. 穿过迷宫的最少移动次数
    你还记得那条风靡全球的贪吃蛇吗？
    我们在一个 n*n 的网格上构建了新的迷宫地图，蛇的长度为 2，也就是说它会占去两个单元格。蛇会从左上角（(0, 0) 和 (0, 1)）开始移动。我们用 0 表示空单元格，用 1 表示障碍物。蛇需要移动到迷宫的右下角（(n-1, n-2) 和 (n-1, n-1)）。
    每次移动，蛇可以这样走：
    如果没有障碍，则向右移动一个单元格。并仍然保持身体的水平／竖直状态。
    如果没有障碍，则向下移动一个单元格。并仍然保持身体的水平／竖直状态。
    如果它处于水平状态并且其下面的两个单元都是空的，就顺时针旋转 90 度。蛇从（(r, c)、(r, c+1)）移动到 （(r, c)、(r+1, c)）。
    如果它处于竖直状态并且其右面的两个单元都是空的，就逆时针旋转 90 度。蛇从（(r, c)、(r+1, c)）移动到（(r, c)、(r, c+1)）。
    返回蛇抵达目的地所需的最少移动次数。
    如果无法到达目的地，请返回 -1。
    示例 1：
    输入：grid = [[0,0,0,0,0,1],
                 [1,1,0,0,1,0],
                 [0,0,0,0,1,1],
                 [0,0,1,0,1,0],
                 [0,1,1,0,0,0],
                 [0,1,1,0,0,0]]
    输出：11
    解释：
    一种可能的解决方案是 [右, 右, 顺时针旋转, 右, 下, 下, 下, 下, 逆时针旋转, 右, 下]。
    示例 2：
    输入：grid = [[0,0,1,1,1,1],
                 [0,0,0,0,1,1],
                 [1,1,0,0,0,1],
                 [1,1,1,0,0,1],
                 [1,1,1,0,0,1],
                 [1,1,1,0,0,0]]
    输出：9
    提示：
    2 <= n <= 100
    0 <= grid[i][j] <= 1
    蛇保证从空单元格开始出发。
    """
    def no_barrier(*args):
        for x, y in args:
            if grid[x][y] == 1:
                return False
        return True
    n = len(grid)
    if grid[n-1][n-1] == 1 or grid[n-1][n-2] == 1: return -1
    snake_pos = (0, 0, 0, 1)
    stk = [[snake_pos, 0]]
    dxy = ((0, 1), (1, 0))
    end = (n-1, n-2, n-1, n-1)
    visit = {snake_pos}
    while stk:
        place, step = stk.pop()
        x1, y1, x2, y2 = place
        if place == end: return step
        # 平移
        for dx, dy in dxy:
            m1, m2 = (x1 + dx, y1 + dy), (x2 + dx, y2 + dy)
            move = m1 + m2
            if n > move[0] >= 0 and n > move[1] >= 0 and n > move[2] >= 0 and n > move[3] >= 0 and not move in visit and no_barrier(m1, m2):
                visit.add(move)
                stk.insert(0, [move, step+1])
        # 旋转
        if x1 == x2:
            move = (x1, y1, x1 + 1, y1)
            if not move in visit and x1 + 1 < n and no_barrier((x1+1, y1), (x2+1, y2)):
                visit.add(move)
                stk.insert(0, [move, step+1])
        else:
            move = (x1, y1, x1, y1 + 1)
            if not move in visit and y1 + 1 < n and no_barrier((x1, y1+1), (x2, y2+1)):
                visit.add(move)
                stk.insert(0, [move, step+1])
    return -1


def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
    """
    1192. 查找集群内的「关键连接」
    力扣数据中心有 n 台服务器，分别按从 0 到 n-1 的方式进行了编号。
    它们之间以「服务器到服务器」点对点的形式相互连接组成了一个内部集群，其中连接 connections 是无向的。
    从形式上讲，connections[i] = [a, b] 表示服务器 a 和 b 之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器。
    「关键连接」是在该集群中的重要连接，也就是说，假如我们将它移除，便会导致某些服务器无法访问其他服务器。
    请你以任意顺序返回该集群内的所有 「关键连接」。
    示例 1：
    输入：n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
    输出：[[1,3]]
    解释：[[3,1]] 也是正确的。
    提示：
    1 <= n <= 10^5
    n-1 <= connections.length <= 10^5
    connections[i][0] != connections[i][1]
    不存在重复的连接
    """
    # dfs记录环, 超时
    from collections import defaultdict
    def dfs(u, depth, connections):
        if rank[u] >= 0: return rank[u]
        rank[u] = depth
        m_rank = ld
        for v in d[u]:
            if rank[v] + 1 == rank[u]: continue
            t_rank = dfs(v, depth+1, connections)
            if t_rank <= rank[u]:
                if [u, v] in connections:
                    connections.remove([u, v])
                if [v, u] in connections:
                    connections.remove([v, u])
            m_rank = min(m_rank, t_rank)
        rank[u] = ld
        return m_rank

    d = defaultdict(list)
    for i in range(len(connections)):
        d[connections[i][0]].append(connections[i][1])
        d[connections[i][1]].append(connections[i][0])
    ld = len(d)
    rank = [-2] * n
    dfs(0, 0, connections)
    return connections


if __name__ == '__main__':
    res = criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])
    print(res)
    # res = minimumMoves([[0,0,0,0,0,0,0,0,0,1],
    #                     [0,1,0,0,0,0,0,1,0,1],
    #                     [1,0,0,1,0,0,1,0,1,0],
    #                     [0,0,0,1,0,1,0,1,0,0],
    #                     [0,0,0,0,1,0,0,0,0,1],
    #                     [0,0,1,0,0,0,0,0,0,0],
    #                     [1,0,0,1,0,0,0,0,0,0],
    #                     [0,0,0,0,0,0,0,0,0,0],
    #                     [0,0,0,0,0,0,0,0,0,0],
    #                     [1,1,0,0,0,0,0,0,0,0]])
    # print(res)
    # res = sortItems(5, 5, [2,0,-1,3,0], [[2,1,3],[2,4],[],[],[]])
    # print(res)
    # res = lastSubstring("cacacb")
    # print(res)
    # r = maxPoints([[0,0],[94911151,94911150],[94911152,94911151]])
    # print(r)
    # r = tilingRectangle(11, 13)
    # print(r)
    # x = findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    # print(x)
    # x = countVowelPermutation(5)
    # print(x)
    # jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70])
    # maximizeSweetness([8,13,20,1,16], 3)
    # numberToWords(1000)
    pass
