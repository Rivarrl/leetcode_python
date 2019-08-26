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
    



if __name__ == '__main__':
    board = [['X', '.', '.', 'X'], ['.', '.', '.', 'X'], ['.', '.', '.', 'X']]
    ans = countBattleships(board)
    print(ans)
    # x =removeKdigits("1432219", 3)
    # print(x)
    # ans = fractionToDecimal(45, 56)
    # print(ans)
    pass