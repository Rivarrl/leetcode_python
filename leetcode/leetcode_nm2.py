# -*- coding:utf-8 -*-
from algorithm_utils import *

# leetcode 中等题


def fractionToDecimal(numerator, denominator):
    """
    166. 分数到小数
    给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
    如果小数部分为循环小数，则将循环的部分括在括号内。
    示例 1:
    输入: numerator = 1, denominator = 2
    输出: "0.5"
    示例 2:
    输入: numerator = 2, denominator = 1
    输出: "2"
    示例 3:
    输入: numerator = 2, denominator = 3
    输出: "0.(6)"
    :param numerator: int
    :param denominator: int
    :return: str
    """
    # 能化成循环小数的分数的特点：当分子和分母只有公因数1时,分母含有2和5以外的质因数
    # 字典记录被除数, 某个被除数第二次出现的时候就是循环结束的时候, 所以字典中存第一次出现时小数点后的位置
    flag = '-' if numerator * denominator < 0 else ''
    numerator, denominator = abs(numerator), abs(denominator)
    a, b = numerator // denominator, numerator % denominator
    res = [str(a)]
    if b != 0: res.append('.')
    d = {}
    while b:
        if b in d:
            res.insert(d[b], "(")
            res.append(")")
            break
        d[b] = len(res)
        a, b = (b * 10) // denominator, (b * 10) % denominator
        res.append(str(a))
    ans = flag + "".join(res)
    return ans


def removeKdigits(num, k):
    """
    402. 移掉K位数字
    给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
    注意:
    num 的长度小于 10002 且 ≥ k。
    num 不会包含任何前导零。
    示例 1 :
    输入: num = "1432219", k = 3
    输出: "1219"
    解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
    示例 2 :
    输入: num = "10200", k = 1
    输出: "200"
    解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
    示例 3 :
    输入: num = "10", k = 2
    输出: "0"
    解释: 从原数字移除所有的数字，剩余为空就是0。
    :param num: str
    :param k: int
    :return: str
    """
    """
    # 每一步去掉从左到右的第一个降序序列的最大值
    # 回溯 + 贪心
    if k == len(num): return "0"
    if k == 0: return num
    i, j = 0, 0
    while i < len(num) - 1:
        if ord(num[i]) > ord(num[i+1]):
            break
        i += 1
    num = num[:i] + num[i + 1:]
    i = 0
    while i < len(num) - 1:
        if num[i] != '0':
            break
        i += 1
    num = num[i:]
    return removeKdigits(num, k - 1)
    """
    """
    # 非递归解法
    if k == len(num): return "0"
    for i in range(k):
        j, q = 1, 0
        while j < len(num) and ord(num[j]) >= ord(num[j-1]):
            q = j
            j += 1
        num = num[:q] + num[q+1:]
        p = 0
        while p < len(num) - 1:
            if num[p] != '0': break
            p += 1
        num = num[p:]
    return num
    """
    # 单调栈
    if k == len(num): return "0"
    stk = ["0"]
    i = 0
    while i < len(num):
        while stk and stk[-1] > num[i] and k > 0:
            stk.pop()
            k -= 1
        stk.append(num[i])
        i += 1
    while k > 0:
        stk.pop()
        k -= 1
    i = 0
    while i < len(stk) - 1:
        if stk[i] != '0':
            break
        i += 1
    return str(int("".join(stk[i:])))


def countBattleships(board):
    """
    419. 甲板上的战舰
    给定一个二维的甲板， 请计算其中有多少艘战舰。 战舰用 'X'表示，空位用 '.'表示。 你需要遵守以下规则：
    给你一个有效的甲板，仅由战舰或者空位组成。
    战舰只能水平或者垂直放置。换句话说,战舰只能由 1xN (1 行, N 列)组成，或者 Nx1 (N 行, 1 列)组成，其中N可以是任意大小。
    两艘战舰之间至少有一个水平或垂直的空位分隔 - 即没有相邻的战舰。
    示例 :
    X..X
    ...X
    ...X
    在上面的甲板中有2艘战舰。
    无效样例 :
    ...X
    XXXX
    ...X
    你不会收到这样的无效甲板 - 因为战舰之间至少会有一个空位将它们分开。
    进阶:
    你可以用一次扫描算法，只使用O(1)额外空间，并且不修改甲板的值来解决这个问题吗？
    :param board: List[List[str]]
    :return: int
    """
    # ans存储最终结果, 第一行X数量直接加
    # 先从上到下对位比较决定+1, 遇到. + X就+1
    # 再从左到右对位比较决定-1, 遇到X + X就-1
    n = len(board)
    if n == 0: return 0
    m = len(board[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if i == 0 and board[i][j] == 'X':
                ans += 1
            if i > 0 and board[i-1][j] == '.' and board[i][j] == 'X':
                ans += 1
            if j > 0 and board[i][j-1] == 'X' and board[i][j] == 'X':
                ans -= 1
    return ans


def flipLights(n, m):
    """
    672. 灯泡开关 Ⅱ
    现有一个房间，墙上挂有 n 只已经打开的灯泡和 4 个按钮。在进行了 m 次未知操作后，你需要返回这 n 只灯泡可能有多少种不同的状态。
    假设这 n 只灯泡被编号为 [1, 2, 3 ..., n]，这 4 个按钮的功能如下：
    1. 将所有灯泡的状态反转（即开变为关，关变为开）
    2. 将编号为偶数的灯泡的状态反转
    3. 将编号为奇数的灯泡的状态反转
    4. 将编号为 3k+1 的灯泡的状态反转（k = 0, 1, 2, ...)
    示例 1:
    输入: n = 1, m = 1.
    输出: 2
    说明: 状态为: [开], [关]
    示例 2:
    输入: n = 2, m = 1.
    输出: 3
    说明: 状态为: [开, 关], [关, 开], [关, 关]
    示例 3:
    输入: n = 3, m = 1.
    输出: 4
    说明: 状态为: [关, 开, 关], [开, 关, 开], [关, 关, 关], [关, 开, 开].
    注意： n 和 m 都属于 [0, 1000].
    :param n: int
    :param m: int
    :return: int
    """
    # 每个按钮按下都会影响到第i + 6k个灯泡
    # 只需要考虑前6个灯泡即可
    # 设4个操作为a,b,c,d 前6个灯泡的决定因素就是:
    # L1 = (a,c,d); L2 = (a,b); L3 = (a,c);
    # L4 = (a,b,d); L5 = (a,c); L6 = (a,b);
    # 初始灯泡为111111, 分别对其做a,b,c,d操作得到000000, 101010, 010101, 011011
    # 由此可知, 前3个灯就可以唯一确定序列的其余部分, n>3等价于n=3, 解空间为[0,2^3]
    # 初始状态为111, 四种操作可以看作与当前状态做111, 010, 101, 100异或
    # m=0时, 结果只有111, 答案是1
    # m=1时, 结果有000, 010, 101, 011; n的答案就是看前n位有几种状态, 对于n=1,2,3; 答案是2,3,4
    # m=2时, 结果有除了011外的7个状态, 对于n=1,2,3; 答案是2,4,7
    # m>2时, 可以得到所有状态, 对于n=1,2,3; 答案是2,4,8
    n = min(n, 3)
    if m == 0: return 1
    if m == 1: return [2,3,4][n-1]
    if m == 2: return [2,4,7][n-1]
    return [2,4,8][n-1]


def canIWin(maxChoosableInteger, desiredTotal):
    """
    464. 我能赢吗
    在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到 100 的玩家，即为胜者。
    如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？
    例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。
    给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？
    你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。
    示例：
    输入：
    maxChoosableInteger = 10
    desiredTotal = 11
    输出：
    false
    解释：
    无论第一个玩家选择哪个整数，他都会失败。
    第一个玩家可以选择从 1 到 10 的整数。
    如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
    第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
    同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
    :param maxChoosableInteger: int
    :param desiredTotal: int
    :return: bool
    """
    # 直接选就赢
    if maxChoosableInteger >= desiredTotal: return True
    # 全选完都不够
    if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal: return False
    # 常规情况, 用dfs
    # cur用二进制实现一个visit数组的作用, 记录选过第几个数字
    def dfs(mci, dt, cur):
        if cur in record:
            return record[cur]
        for i in range(1, mci+1):
            msk = 1 << i
            if cur & msk == 0:
                if dt <= i or not dfs(mci, dt-i, cur | msk):
                    record[cur] = True
                    return True
        record[cur] = False
        return False
    record = {}
    return dfs(maxChoosableInteger, desiredTotal, 0)


def updateMatrix(matrix):
    """
    542. 01 矩阵
    给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
    两个相邻元素间的距离为 1 。
    示例 1:
    输入:
    0 0 0
    0 1 0
    0 0 0
    输出:
    0 0 0
    0 1 0
    0 0 0
    示例 2:
    输入:
    0 0 0
    0 1 0
    1 1 1
    输出:
    0 0 0
    0 1 0
    1 2 1
    注意:
    给定矩阵的元素个数不超过 10000。
    给定矩阵中至少有一个元素是 0。
    矩阵中的元素只在四个方向上相邻: 上、下、左、右。
    :param matrix: List[List[int]]
    :return: List[List[int]]
    """
    """
    # bfs 77%
    n = len(matrix)
    m = len(matrix[0])
    dist = [[0] * m for _ in range(n)]
    stk = [(i, j) for i in range(n) for j in range(m) if matrix[i][j]]
    step = 0
    dij = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while stk:
        step += 1
        next_stk, cur = [], []
        for i, j in stk:
            z = 0
            for di, dj in dij:
                x, y = i + di, j + dj
                if 0 <= x < n and 0 <= y < m and matrix[x][y] == 0:
                    z += 1
                    break
            if z:
                dist[i][j] = step
                cur.append((i, j))
            else:
                next_stk.append((i, j))
        for x, y in cur:
            matrix[x][y] = 0
        stk = next_stk
    print(dist)
    return dist
    """
    # dp
    n = len(matrix)
    m = len(matrix[0])
    dp = [[float('inf')] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if matrix[i][j] == 0:
                dp[i][j] = 0
            else:
                if i < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                if j < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)
    return dp


def checkValidString(s):
    """
    678. 有效的括号字符串
    给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：
    任何左括号 ( 必须有相应的右括号 )。
    任何右括号 ) 必须有相应的左括号 ( 。
    左括号 ( 必须在对应的右括号之前 )。
    * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
    一个空字符串也被视为有效字符串。
    示例 1:
    输入: "()"
    输出: True
    示例 2:
    输入: "(*)"
    输出: True
    示例 3:
    输入: "(*))"
    输出: True
    注意:
    字符串大小将在 [1，100] 范围内。
    :param s: str
    :return: bool
    """
    """
    # dfs超时
    def dfs(s, i, l):
        if not s: return True
        if l < 0 or i + l > len(s): return False
        if i == n:
            if l == 0:
                return True
            return False
        if s[i] == '(':
            return dfs(s, i+1, l+1)
        elif s[i] == ')':
            return dfs(s, i+1, l-1)
        else:
            return dfs(s, i+1, l-1) or dfs(s, i+1, l) or dfs(s, i+1, l+1)
    n = len(s)
    return dfs(s, 0, 0)
    """
    """
    # 栈分别存储(和*
    stk = []
    stk2 = []
    for i, c in enumerate(s):
        if c == '(':
            stk.append(i)
        elif c == '*':
            stk2.append(i)
        else:
            if not stk and not stk2:
                return False
            if stk:
                stk.pop()
            else:
                stk2.pop()
    while stk and stk2:
        if stk[-1] > stk2[-1]:
            return False
        stk.pop()
        stk2.pop()
    return len(stk) == 0
    """
    # 双指针l, h 分别代表'*'代表')'和'*'代表'('时的'('数
    l, h = 0, 0
    for c in s:
        if c == '(':
            l += 1
            h += 1
        elif c == ')':
            if l > 0:
                l -= 1
            h -= 1
        else:
            if l > 0:
                l -= 1
            h += 1
        # '*'代表'(', 还是没有')'多
        if h < 0:
            return False
    print(l, h)
    # 大于0说明就算把能替换的'*'都替换成')', 还是没有'('多
    return l == 0


def stoneGame(piles):
    """
    877. 石子游戏
    亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。
    游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。
    亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。
    假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。
    示例：
    输入：[5,3,4,5]
    输出：true
    解释：
    亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
    假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
    如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
    如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
    这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
    提示：
    2 <= piles.length <= 500
    piles.length 是偶数。
    1 <= piles[i] <= 500
    sum(piles) 是奇数。
    :param piles: List[int]
    :return: bool
    """
    # 由于这个比赛非输即赢，是零和博弈，先手永远可以让自己赢
    # return True
    # 分别记录所有可能情况的先后手，由于每次只能从头或者尾取数，所以不存在只有中间的数被选走的情况
    col = len(piles)
    dp = [[[0, 0] for _ in range(col)] for _ in range(col)]
    for i in range(col):
        dp[i][i][0] = piles[i]

    # 斜着遍历数组
    for k in range(2, col+1):
        for i in range(0, col-1):
            j = k + i - 1
            if j == col:
                break
            left = piles[i] + dp[i+1][j][1]
            right = piles[j] + dp[i][j-1][1]
            if left > right:
                dp[i][j][0] = left
                dp[i][j][1] = dp[i+1][j][0]
            else:
                dp[i][j][0] = right
                dp[i][j][1] = dp[i][j-1][0]

    res = dp[0][col-1]
    return res[0] - res[1]


def lenLongestFibSubseq(A):
    """
    873. 最长的斐波那契子序列的长度
    如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
    n >= 3
    对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
    给定一个严格递增的正整数数组形成序列，找到 A 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
    （回想一下，子序列是从原序列 A 中派生出来的，它从 A 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）
    示例 1：
    输入: [1,2,3,4,5,6,7,8]
    输出: 5
    解释:
    最长的斐波那契式子序列为：[1,2,3,5,8] 。
    示例 2：
    输入: [1,3,7,11,12,14,18]
    输出: 3
    解释:
    最长的斐波那契式子序列有：
    [1,11,12]，[3,11,14] 以及 [7,11,18] 。
    提示：
    3 <= A.length <= 1000
    1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
    （对于以 Java，C，C++，以及 C# 的提交，时间限制被减少了 50%）
    :param A: List[int]
    :return: int
    """
    """
    # set
    s = set(A)
    n = len(A)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            cur = 2
            a, b = A[i], A[j]
            while a + b in s:
                cur += 1
                a, b = b, a+b
                ans = max(ans, cur)
    return ans
    """
    # dp
    n = len(A)
    if n < 3: return 0
    dp = [[2] * n for _ in range(n)]
    ans = 0
    for i in range(n):
        l, r = 0, i-1
        while l < r:
            s = A[l] + A[r]
            if s == A[i]:
                dp[r][i] = max(dp[r][i], dp[l][r] + 1)
                ans = max(ans, dp[r][i])
                l += 1
                r -= 1
            elif s < A[i]:
                l += 1
            else:
                r -= 1
    return ans


def uniquePathsWithObstacles(obstacleGrid):
    """
    63. 不同路径 II
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
    网格中的障碍物和空位置分别用 1 和 0 来表示。
    说明：m 和 n 的值均不超过 100。
    示例 1:
    输入:
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    输出: 2
    解释:
    3x3 网格的正中间有一个障碍物。
    从左上角到右下角一共有 2 条不同的路径：
    1. 向右 -> 向右 -> 向下 -> 向下
    2. 向下 -> 向下 -> 向右 -> 向右
    :param obstacleGrid: List[List[int]]
    :return: int
    """
    n = len(obstacleGrid)
    if n == 0: return 0
    m = len(obstacleGrid[0])
    dp = [[0] * m for _ in range(n)]
    i = 0
    while i < m and obstacleGrid[0][i] == 0:
        dp[0][i] = 1
        i += 1
    i = 0
    while i < n and obstacleGrid[i][0] == 0:
        dp[i][0] = 1
        i += 1
    for i in range(1, n):
        for j in range(1, m):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]


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
    说明:
    为什么返回数值是整数，但输出的答案是数组呢?
    请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
    你可以想象内部操作如下:
    // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
    int len = removeDuplicates(nums);
    // 在函数里修改输入数组对于调用者是可见的。
    // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }
    :param nums: List[int]
    :return: None
    """
    pass


def maximumSum(arr):
    """
    1186. 删除一次得到子数组最大和
    给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。
    换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。
    注意，删除一个元素后，子数组 不能为空。
    请看示例：
    示例 1：
    输入：arr = [1,-2,0,3]
    输出：4
    解释：我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1, 0, 3]，和最大。
    示例 2：
    输入：arr = [1,-2,-2,3]
    输出：3
    解释：我们直接选出 [3]，这就是最大和。
    示例 3：
    输入：arr = [-1,-1,-1,-1]
    输出：-1
    解释：最后得到的子数组不能为空，所以我们不能选择 [-1] 并从中删去 -1 来得到 0。
         我们应该直接选择 [-1]，或者选择 [-1, -1] 再从中删去一个 -1。
    提示：
    1 <= arr.length <= 10^5
    -10^4 <= arr[i] <= 10^4
    :param arr: List[int]
    :return: int
    """
    """
    # 左右两侧求最大子串和取max(left[i-1], right[i+1])
    n = len(arr)
    left, right = [0] * n, [0] * n
    left[0] = arr[0]
    right[-1] = arr[-1]
    ans = max(left[0], right[-1])
    for i in range(1, n):
        left[i] = arr[i]
        if left[i-1] > 0:
            left[i] += left[i-1]
        ans = max(ans, left[i])
    for i in range(n-2, -1, -1):
        right[i] = arr[i]
        if right[i+1] > 0:
            right[i] += right[i+1]
        ans = max(ans, right[i])
    for i in range(1, n-1):
        ans = max(ans, left[i-1] + right[i+1])
    return ans
    """
    # dp
    n = len(arr)
    res = arr[0]
    f, g = [0] * n, [0] * n
    f[0] = arr[0]
    for i in range(1, n):
        # 如果上一步是负值就不带上一步的结果
        f[i] = max(f[i-1] + arr[i], arr[i])
        # g[i]是删除出现在i-1以前的最大值和删除i的最大值的最大值
        g[i] = max(g[i-1] + arr[i], f[i-1])
        res = max(res, f[i], g[i])
    return res


def findNumberOfLIS(nums):
    """
    673. 最长递增子序列的个数
    给定一个未排序的整数数组，找到最长递增子序列的个数。
    示例 1:
    输入: [1,3,5,4,7]
    输出: 2
    解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
    示例 2:
    输入: [2,2,2,2,2]
    输出: 5
    解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
    注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
    :param nums: List[int]
    :return: int
    """
    n = len(nums)
    if n == 0:
        return 0
    dp = [1] * n
    dp_num = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    dp_num[i] = dp_num[j]
                elif dp[j] + 1 == dp[i]:
                    dp_num[i] += dp_num[j]
    print(dp)
    print(dp_num)
    ans = 0
    lis = max(dp)
    for i in range(n):
        if dp[i] == lis:
            ans += dp_num[i]
    return ans


def findLength(A, B):
    """
    718. 最长重复子数组
    给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
    示例 1:
    输入:
    A: [1,2,3,2,1]
    B: [3,2,1,4,7]
    输出: 3
    解释:
    长度最长的公共子数组是 [3, 2, 1]。
    说明:
    1 <= len(A), len(B) <= 1000
    0 <= A[i], B[i] < 100
    :param A: List[int]
    :param B: List[int]
    :return: int
    """
    n, m = len(A), len(B)
    dp = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if A[i] == B[j]:
                if i == n - 1 or j == m - 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j+1] + 1
                ans = max(ans, dp[i][j])
    return ans


def rangeBitwiseAnd(m, n):
    """
    201. 数字范围按位与
    给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
    示例 1: 
    输入: [5,7]
    输出: 4
    示例 2:
    输入: [0,1]
    输出: 0
    :param m: int
    :param n: int
    :return: int
    """
    i = 0
    while m != n:
        n >>= 1
        m >>= 1
        i += 1
    return m << i


def numTilePossibilities(tiles):
    """
    1079. 活字印刷
    你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
    示例 1：
    输入："AAB"
    输出：8
    解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
    示例 2：
    输入："AAABBC"
    输出：188
    提示：
    1 <= tiles.length <= 7
    tiles 由大写英文字母组成
    :param tiles: str
    :return: int
    """
    def helper(s):
        if len(s) == 0: return 0
        cur = set()
        ans = 0
        for i in range(len(s)):
            if not s[i] in cur:
                cur.add(s[i])
                ans += helper(s[:i] + s[i+1:]) + 1
        return ans
    return helper(tiles)


def addNegabinary(arr1, arr2):
    """
    1073. 负二进制数相加
    给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。
    数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1,1,0,1] 表示数字 (-2)^3 + (-2)^2 + (-2)^0 = -3。数组形式 的数字也同样不含前导零：以 arr 为例，这意味着要么 arr == [0]，要么 arr[0] == 1。
    返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。
    示例：
    输入：arr1 = [1,1,1,1,1], arr2 = [1,0,1]
    输出：[1,0,0,0,0]
    解释：arr1 表示 11，arr2 表示 5，输出表示 16 。
    提示：
    1 <= arr1.length <= 1000
    1 <= arr2.length <= 1000
    arr1 和 arr2 都不含前导零
    arr1[i] 为 0 或 1
    arr2[i] 为 0 或 1
    :param arr1: List[int]
    :param arr2: List[int]
    :return: List[int]
    """
    n1, n2 = len(arr1), len(arr2)
    if n1 < n2:
        n1, n2 = n2, n1
        arr1, arr2 = arr2, arr1
    for i in range(n1):
        i1, i2 = n1 - 1 - i, n2 - 1 - i
        if i2 >= 0:
            arr1[i1] += arr2[i2]
        if arr1[i1] >= 2:
            arr1[i1] %= 2
            if i1 > 0:
                arr1[i1 - 1] -= 1
            else:
                arr1.insert(0, -1)
        if arr1[i1] == -1:
            if i1 > 0:
                arr1[i1] = 1
                arr1[i1 - 1] += 1
            else:
                arr1[i1] = 1
                arr1.insert(0, 1)
    while arr1 and arr1[0] == 0:
        arr1.pop(0)
    print(arr1)
    return arr1 if arr1 else [0]


def largestDivisibleSubset(nums):
    """
    368. 最大整除子集
    给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。
    如果有多个目标子集，返回其中任何一个均可。
    示例 1:
    输入: [1,2,3]
    输出: [1,2] (当然, [1,3] 也正确)
    示例 2:
    输入: [1,2,4,8]
    输出: [1,2,4,8]
    :param nums: List[int]
    :return: List[int]
    """
    if not nums: return []
    nums.sort()
    n = len(nums)
    dp = [1] * n
    pre = [-1] * n
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] % nums[j] == 0:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pre[i] = j
    max_index = dp.index(max(dp))
    res = []
    while max_index != -1:
        res.append(nums[max_index])
        max_index = pre[max_index]
    return res


def getMoneyAmount(n):
    """
    375. 猜数字大小 II
    我们正在玩一个猜数游戏，游戏规则如下：
    我从 1 到 n 之间选择一个数字，你来猜我选了哪个数字。
    每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。
    然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。
    示例:
    n = 10, 我选择了8.
    第一轮: 你猜我选择的数字是5，我会告诉你，我的数字更大一些，然后你需要支付5块。
    第二轮: 你猜是7，我告诉你，我的数字更大一些，你支付7块。
    第三轮: 你猜是9，我告诉你，我的数字更小一些，你支付9块。
    游戏结束。8 就是我选的数字。
    你最终要支付 5 + 7 + 9 = 21 块钱。
    给定 n ≥ 1，计算你至少需要拥有多少现金才能确保你能赢得这个游戏。
    :param n: int
    :return: int
    """
    dp = [[0] * (n+1) for _ in range(n+1)]
    for k in range(2, n+1):
        for i in range(1, n-k+2):
            ans = float('inf')
            for j in range(i, i+k-1):
                cur = j + max(dp[i][j-1], dp[j+1][i+k-1])
                ans = min(ans, cur)
            dp[i][i+k-1] = ans
    return dp[1][n]


def generateTrees(n):
    """
    95. 不同的二叉搜索树 II
    给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
    示例:
    输入: 3
    输出:
    [
      [1,null,3,2],
      [3,2,null,1],
      [3,1,null,null,2],
      [2,1,3],
      [1,null,2,null,3]
    ]
    解释:
    以上的输出对应以下 5 种不同结构的二叉搜索树：

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3
    :param n: int
    :return: List[TreeNode]
    """
    def helper(l, r):
        res = []
        if l > r:
            res.append(None)
        for i in range(l, r+1):
            left = helper(l, i-1)
            right = helper(i+1, r)

            for j in range(len(left)):
                for k in range(len(right)):
                    cur = TreeNode(i)
                    cur.left = left[j]
                    cur.right = right[k]
                    res.append(cur)
        return res
    if n == 0: return []
    return helper(1, n)


def combinationSum4(nums, target):
    """
    377. 组合总和 Ⅳ
    给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。
    示例:
    nums = [1, 2, 3]
    target = 4
    所有可能的组合为：
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)
    请注意，顺序不同的序列被视作不同的组合。
    因此输出为 7。
    进阶：
    如果给定的数组中含有负数会怎么样？
    问题会产生什么变化？
    我们需要在题目中添加什么限制来允许负数的出现？
    :param nums: List[int]
    :param target: int
    :return: int
    """
    # 完全背包
    nums = [i for i in nums if i <= target]
    n = len(nums)
    if n == 0 or target <= 0:
        return 0
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for j in range(n):
            if i >= nums[j]:
                dp[i] += dp[i - nums[j]]
    return dp[-1]


def longestArithSeqLength(A):
    """
    1027. 最长等差数列
    给定一个整数数组 A，返回 A 中最长等差子序列的长度。
    回想一下，A 的子序列是列表 A[i_1], A[i_2], ..., A[i_k] 其中 0 <= i_1 < i_2 < ... < i_k <= A.length - 1。并且如果 B[i+1] - B[i]( 0 <= i < B.length - 1) 的值都相同，那么序列 B 是等差的。
    示例 1：
    输入：[3,6,9,12]
    输出：4
    解释：
    整个数组是公差为 3 的等差数列。
    示例 2：
    输入：[9,4,7,2,10]
    输出：3
    解释：
    最长的等差子序列是 [4,7,10]。
    示例 3：
    输入：[20,1,15,3,10,5,8]
    输出：4
    解释：
    最长的等差子序列是 [20,15,10,5]。
    提示：
    2 <= A.length <= 2000
    0 <= A[i] <= 10000
    :param A: List[int]
    :return: int
    """
    n = len(A)
    arr = [{} for _ in range(n)]
    ans = 1
    for i in range(1, n):
        for j in range(i):
            k = A[i] - A[j]
            x = arr[j].get(k, 1) + 1
            arr[i][k] = x
        ans = max(ans, max(arr[i].values()))
    return ans


def numTilings(N):
    """
    790. 多米诺和托米诺平铺
    有两种形状的瓷砖：一种是 2x1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。
    XX  <- 多米诺
    XX  <- "L" 托米诺
    X
    给定 N 的值，有多少种方法可以平铺 2 x N 的面板？返回值 mod 10^9 + 7。
    （平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。）
    示例:
    输入: 3
    输出: 5
    解释:
    下面列出了五种不同的方法，不同字母代表不同瓷砖：
    XYZ XXZ XYY XXY XYY
    XYZ YYZ XZZ XYY XXY
    提示：
    N  的范围是 [1, 1000]
    :param N: int
    :return: int
    """
    """
    # 发现递推式：dp[i] = dp[i-1] * 2 + dp[i-3]
    if N <= 2: return N
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 5
    for i in range(4, N + 1):
        dp[i] = (dp[i-3] + dp[i-1] * 2) % (10**9+7)
    return dp[N]
    """
    # 不能推出递推式，辅助数组来解决, 辅助数组h[i]为2i-1大小的地板时的平铺种类
    if N <= 2: return N
    mod = 10 ** 9 + 7
    dp = [0] * (N + 1)
    h = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N+1):
        h[i] += h[i-1]
        if i > 1:
            h[i] += dp[i-2]
        dp[i] += dp[i-1]
        dp[i] += (h[i-1] * 2)
        if i > 1:
            dp[i] += dp[i-2]
        h[i] %= mod
        dp[i] %= mod
    return dp[N]


def soupServings(N):
    """
    808. 分汤
    有 A 和 B 两种类型的汤。一开始每种类型的汤有 N 毫升。有四种分配操作：
    提供 100ml 的汤A 和 0ml 的汤B。
    提供 75ml 的汤A 和 25ml 的汤B。
    提供 50ml 的汤A 和 50ml 的汤B。
    提供 25ml 的汤A 和 75ml 的汤B。
    当我们把汤分配给某人之后，汤就没有了。每个回合，我们将从四种概率同为0.25的操作中进行分配选择。如果汤的剩余量不足以完成某次操作，我们将尽可能分配。当两种类型的汤都分配完时，停止操作。
    注意不存在先分配100 ml汤B的操作。
    需要返回的值： 汤A先分配完的概率 + 汤A和汤B同时分配完的概率 / 2。
    示例:
    输入: N = 50
    输出: 0.625
    解释:
    如果我们选择前两个操作，A将首先变为空。对于第三个操作，A和B会同时变为空。对于第四个操作，B将首先变为空。
    所以A变为空的总概率加上A和B同时变为空的概率的一半是 0.25 *(1 + 1 + 0.5 + 0)= 0.625。
    注释:
    0 <= N <= 10^9。
    返回值在 10^-6 的范围将被认为是正确的。
    :param N: int
    :return: float
    """
    """
    # 带备忘的dfs
    def dfs(x, y):
        if (x, y) in rec:
            return rec[(x, y)]
        ans = 0
        if x <= 0 and y > 0:
            ans = 1
        elif x <= 0 and y <= 0:
            ans = 0.5
        elif x > 0 and y <= 0:
            ans = 0
        else:
            ans = 0.25 * (dfs(x-100, y) + dfs(x-75, y-25) + dfs(x-50, y-50) + dfs(x-25, y-75))
        rec[(x, y)] = ans
        return ans
    if N > 4800: return 1.0
    rec = dict()
    return dfs(N, N)
    """
    # dp
    def fix(i):
        return max(i, 0)
    if N >= 4800: return 1.0
    n = N//25
    if N % 25 > 0:
        n += 1
    dp = [[0] * (n+1) for _ in range(n+1)]
    dp[0][0] = 0.5
    for i in range(1, n+1):
        dp[i][0] = 0
        dp[0][i] = 1
    for i in range(1, n+1):
        a1, a2, a3, a4 = fix(i-4), fix(i-3), fix(i-2), fix(i-1)
        for j in range(1, n+1):
            b1, b2, b3, b4 = fix(j), fix(j-1), fix(j-2), fix(j-3)
            dp[i][j] = 0.25 * (dp[a1][b1] + dp[a2][b2] + dp[a3][b3] + dp[a4][b4])
    return dp[n][n]


def numIslands(grid):
    """
    200. 岛屿数量
    给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。
    示例 1:
    输入:
    11110
    11010
    11000
    00000
    输出: 1
    示例 2:
    输入:
    11000
    11000
    00100
    00011
    输出: 3
    :param grid: List[List[str]]
    :return: int
    """
    def dfs(i, j):
        if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == '0':
            return False
        if visited[i][j]: return False
        visited[i][j] = True
        for dx, dy in dxy:
            dfs(i + dx, j + dy)
        return True
    n = len(grid)
    if n == 0: return 0
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]
    dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
    ans = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and dfs(i, j):
                ans += 1
    return ans


if __name__ == '__main__':
    addNegabinary([1,0,1], [1,0,1])
    # numTilePossibilities("AAB")
    # A = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    # B = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    # findLength(A, B)
    # x = [3,1,2]
    # findNumberOfLIS(x)
    # x = [[0,0,0], [0,1,0], [0,0,0]]
    # uniquePathsWithObstacles(x)
    # x = stoneGame([5,3,4,5])
    # print(x)
    # b = checkValidString("(*()*))(()")
    # print(b)
    # updateMatrix([[0,1,1],[1,1,1],[1,1,1]])
    # b = canIWin(4, 6)
    # print(b)
    # board = [['X', '.', '.', 'X'], ['.', '.', '.', 'X'], ['.', '.', '.', 'X']]
    # ans = countBattleships(board)
    # print(ans)
    # x =removeKdigits("1432219", 3)
    # print(x)
    # ans = fractionToDecimal(45, 56)
    # print(ans)
    pass