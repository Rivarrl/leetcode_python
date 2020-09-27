# -*- coding: utf-8 -*-
# ======================================
# @File    : 16-09.py
# @Time    : 2020/9/25 12:49 下午
# @Author  : Rivarrl
# ======================================
class Operations:
    """
    [面试题 16.09. 运算](https://leetcode-cn.com/problems/operations-lcci)
    """
    def __init__(self):
        self.pos = [1]
        self.neg = [-1]
        for i in range(30):
            self.pos += [self.pos[-1] + self.pos[-1]]
            self.neg += [self.neg[-1] + self.neg[-1]]

    def ng(self, x: int):
        if not x: return x
        if x > 0:
            p, n, op = self.pos, self.neg, lambda x, y: x >= y
        else:
            p, n, op = self.neg, self.pos, lambda x, y: x <= y
        res = 0
        i = 30
        while x:
            if op(x, p[i]):
                x += n[i]
                res += n[i]
            i += self.neg[0]
        return res

    def minus(self, a: int, b: int) -> int:
        # 写一种都是正数的情况，然后配合取反函数适应所有情况
        if not b: return a
        if a < 0 and b < 0: return self.minus(self.ng(b), self.ng(a))
        if a < 0 and b > 0: return self.ng(self.ng(a) + b)
        if a > 0 and b < 0: return a + self.ng(b)
        res = 0
        i = 30
        while i >= 0 and (a > 0 or b > 0):
            if a >= self.pos[i]:
                a += self.neg[i]
                res += self.pos[i]
            if b >= self.pos[i]:
                b += self.neg[i]
                res += self.neg[i]
            i += self.neg[0]
        return res

    def multiply(self, a: int, b: int) -> int:
        # 写一种b大于0时的情况，然后配合取反函数适应所有情况，快速乘得用右移，只能递归了
        if not a or not b: return 0
        if a == 1: return b
        if b == 1: return a
        if b < 0: return self.ng(self.multiply(a, self.ng(b)))
        mask = res = i = 0
        base = a
        while mask < b and i < 30:
            mask += self.pos[i]
            res += base
            base += base
            i += 1
        res = self.minus(res, self.multiply(a, self.minus(mask, b)))
        return res

    def divide(self, a: int, b: int) -> int:
        if not a: return 0
        if b == 1: return a
        if a < 0: return self.ng(self.divide(self.ng(a), b))
        if b < 0: return self.ng(self.divide(a, self.ng(b)))
        mask = res = i = 0
        base = b
        while res < a and i < 30:
            mask += self.pos[i]
            res += base
            base += base
            i += 1

if __name__ == '__main__':
    a = Operations()
    # x = a.minus(5, 3)
    # print(x, 2)
    # x = a.minus(-5, 3)
    # print(x, -8)
    # x = a.minus(5, -3)
    # print(x, 8)
    # x = a.minus(-5, -3)
    # print(x, -2)
    x = a.multiply(3, 5)
    print(x)
    x = a.multiply(-3, 5)
    print(x)
    x = a.multiply(5, -3)
    print(x)
    x = a.multiply(-5, -3)
    print(x)