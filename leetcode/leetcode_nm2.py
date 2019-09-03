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


if __name__ == '__main__':
    b = checkValidString("(*()*))(()")
    print(b)
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