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


if __name__ == '__main__':
    fractionToDecimal(45, 56)
    pass