# -*- coding: utf-8 -*-
# ======================================
# @File    : 677.py
# @Time    : 2020/10/13 1:24 下午
# @Author  : Rivarrl
# ======================================

class MapSum:
    """
    [677. 键值映射](https://leetcode-cn.com/problems/map-sum-pairs/)
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict_tree = {}

    def _insert(self, i, n, d, key, value):
        c = key[i]
        if c not in d:
            d[c] = [0, 0, {}]
        if i == n - 1:
            diff = value - d[c][0]
            d[c][0] = value
        else:
            nd = d[c][-1]
            diff = self._insert(i+1, n, nd, key, value)
        d[c][1] += diff
        return diff

    def insert(self, key: str, val: int) -> None:
        n = len(key)
        if n == 0: return
        d = self.dict_tree
        self._insert(0, n, d, key, val)

    def sum(self, prefix: str) -> int:
        d = self.dict_tree
        n = len(prefix)
        for i in range(n):
            c = prefix[i]
            if c not in d: break
            if i == n - 1:
                return d[c][1]
            d = d[c][-1]
        return 0

if __name__ == '__main__':
    a = MapSum()
    a.insert("apple", 3)
    r = a.sum("ap")
    print(r)
    a.insert("app", 2)
    r = a.sum("ap")
    print(r)
