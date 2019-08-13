# -*- coding:utf-8 -*-
from algorithm_utils import *

# leetcode 困难题

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
    pass


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
    fn = 0
    res = []
    pass


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


if __name__ == '__main__':
    # findIntegers(2)
    # y = crackSafe(2, 3)
    # print(y)
    # removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1])
    pass