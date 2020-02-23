# -*- coding: utf-8 -*-
# ======================================
# @File    : 5324.py
# @Time    : 2020/2/23 12:46
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Cashier(object):
    """
    [5324. 每隔 n 个顾客打折](https://leetcode-cn.com/problems/apply-discount-every-n-orders/)
    """
    def __init__(self, n, discount, products, prices):
        self.ctr = 0
        self.n = n
        self.discount = 1 - (discount / 100)
        self.d = {k:v for k, v in zip(products, prices)}


    def getBill(self, product, amount):
        self.ctr += 1
        res = 0
        for x, y in zip(product, amount):
            res += self.d[x] * y
        if self.ctr % self.n == 0:
            res *= self.discount
        return res

