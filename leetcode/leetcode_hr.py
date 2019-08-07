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


if __name__ == '__main__':
    y = crackSafe(2, 3)
    print(y)
    # removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1])
    pass