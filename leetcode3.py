# -*- coding: utf-8 -*-
# ======================================
# @File    : leetcode3.py
# @Time    : 2019/4/27 0:47
# @Author  : Rivarrl
# ======================================

# leetcode3

def divide(dividend, divisor):
    """
    29. 两数相除
    给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
    返回被除数 dividend 除以除数 divisor 得到的商。
    示例 1:
    输入: dividend = 10, divisor = 3
    输出: 3
    示例 2:
    输入: dividend = 7, divisor = -3
    输出: -2
    说明:
    被除数和除数均为 32 位有符号整数。
    除数不为 0。
    假设我们的环境只能存储 32 位有符号整数，其数值范围是 [-2**31,  2**31-1]。本题中，如果除法结果溢出，则返回 2**31-1。
    思路:
    用减法会超时，所以使用更快的位运算，<<1 = *2^1, >>1 = /2^1
    :param dividend: int
    :param divisor: int
    :return: int
    """
    inf = 2**31 - 1
    MAX = inf
    MIN = -inf - 1
    if dividend == 0 : return 0
    if divisor == 1: return dividend
    if dividend == MIN and divisor == -1: return MAX
    # 结果符号，两数（符号位）亦或
    f = dividend ^ divisor >= 0
    i, j = 0, 31
    a, b = abs(dividend), abs(divisor)
    res = 0
    while i < j:
        mid = (i + j) >> 1
        x = b << mid
        y = x << 1
        if y > a >= x:
            a -= x
            res += (1 << mid)
            i, j = 0, mid
        elif a < y:
            j = mid
        else:
            i = mid
    return res if f else -res


def combinationSum(candidates, target):
    """
    39. 组合总和
    给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
    candidates 中的数字可以无限制重复被选取。
    说明：
    所有数字（包括 target）都是正整数。
    解集不能包含重复的组合。
    示例 1:
    输入: candidates = [2,3,6,7], target = 7,
    所求解集为:
    [
      [7],
      [2,2,3]
    ]
    示例 2:
    输入: candidates = [2,3,5], target = 8,
    所求解集为:
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
    ]
    :param candidates: List[int]
    :param target: int
    :return: List[List[int]]
    """
    pass


def pancakeSort(A):
    """
    969. 煎饼排序
    给定数组 A，我们可以对其进行煎饼翻转：我们选择一些正整数 k <= A.length，然后反转 A 的前 k 个元素的顺序。我们要执行零次或多次煎饼翻转（按顺序一次接一次地进行）以完成对数组 A 的排序。
    返回能使 A 排序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * A.length 范围内的有效答案都将被判断为正确。
    示例 1：
    输入：[3,2,4,1]
    输出：[4,2,4,3]
    解释：
    我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
    初始状态 A = [3, 2, 4, 1]
    第一次翻转后 (k=4): A = [1, 4, 2, 3]
    第二次翻转后 (k=2): A = [4, 1, 2, 3]
    第三次翻转后 (k=4): A = [3, 2, 1, 4]
    第四次翻转后 (k=3): A = [1, 2, 3, 4]，此时已完成排序。
    :param A: List[int]
    :return: List[int]
    """
    pass


if __name__ == '__main__':
    print(divide(10,2))