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
        if x == 0: return 0
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
        return a + self.ng(b)

    def multiply(self, a: int, b: int) -> int:
        # 写一种b大于0时的情况，然后配合取反函数适应所有情况，快速乘得用右移，只能递归了
        if a == 0 or b == 0: return 0
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
        if b == 1: return a
        if a < 0: return self.ng(self.divide(self.ng(a), b))
        if b < 0: return self.ng(self.divide(a, self.ng(b)))
        if a < b: return 0
        mask = cur = i = 0
        base = b
        while cur + base <= a and i < 30:
            mask += self.pos[i]
            cur += base
            base += base
            i += 1
        res = mask + self.divide(self.minus(a, cur), b)
        return res

if __name__ == '__main__':
    a = Operations()
    x = a.divide(1, -109883727)
    print(x) # 0
    x = a.divide(-13969484, -5)
    print(x) # 2793896
    x = a.divide(-11954206, 5401)
    print(x) # -221
    x = a.divide(404385, -263)
    print(x) # -1537