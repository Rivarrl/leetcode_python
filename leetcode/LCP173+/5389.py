# -*- coding: utf-8 -*-
# ======================================
# @File    : 5389.py
# @Time    : 2020/4/19 11:28
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5389. 点菜展示表]()
    """
    @timeit
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d1 = {}
        fd = set()
        fn = set()
        for name, num, food in orders:
            fd.add(food)
            fn.add(int(num))
        r1 = sorted(list(fd))
        fdd = {k:v+1 for v, k in enumerate(r1)}
        fn = sorted(list(fn))
        fnn = {str(k):v+1 for v, k in enumerate(fn)}
        res = [[''] * (len(r1) + 1) for _ in range(len(fn) + 1)]
        res[0][0] = 'Table'
        for i in range(len(r1)):
            res[0][i+1] = r1[i]
        for i in range(len(fn)):
            res[i+1][0] = str(fn[i])
        for name, num, food in orders:
            if not num in d1:
                d1[num] = [0] * (len(r1) + 1)
            d1[num][fdd[food]] += 1
        for k, v in d1.items():
            for i, e in enumerate(v):
                if i == 0: continue
                res[fnn[k]][i] = str(e)
        return res


if __name__ == '__main__':
    a = Solution()
    a.displayTable(orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]])
    a.displayTable(orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]])
    a.displayTable(orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]])
