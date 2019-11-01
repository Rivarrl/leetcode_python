# -*- coding: utf-8 -*-
# ======================================
# @File    : BST.py
# @Time    : 2019/11/1 18:56
# @Author  : Rivarrl
# ======================================

class Node:
    def __init__(self, key=None, val=None, size=0, left=None, right=None):
        self.key = key
        self.val = val
        self.size = size
        self.left = left
        self.right = right


class BST:

    def __init__(self, root=None):
        self.root = root

    @staticmethod
    def size(h):
        if h == None: return 0
        return h.size

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, h, key, val):
        if h == None: return Node(key, val, 1)
        cmp = key - h.key
        if cmp > 0: h.right = self._put(h.right, key, val)
        elif cmp < 0: h.left = self._put(h.left, key, val)
        else: h.val = val
        h.size = self.size(h.left) + self.size(h.right) + 1
        return h

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, h, key):
        if h == None: return None
        cmp = key - h.key
        if cmp > 0: return self._get(h.right, key)
        elif cmp < 0: return self._get(h.left, key)
        else: return h.val

    def delete(self, key):
        self._delete(self.root, key)

    def _delete(self, h, key):
        if h == None: return None
        cmp = key - h.key
        if cmp > 0: h.right = self._delete(h.right, key)
        elif cmp < 0: h.left = self._delete(h.left, key)
        else:
            if h.left == None: return h.right
            if h.right == None: return h.left
            x = h
            h = self._min(x.right)
            h.right = self.delete_min(x.right)
            h.left = x.left

    def min(self):
        self._min(self.root)

    def max(self):
        self._max(self.root)

    def _min(self, x):
        if x.left == None: return x
        return self._min(x.left)

    def _max(self, x):
        if x.right == None: return x
        return self._min(x.right)

    def delete_min(self, x):
        if x.left == None: return x.right
        x.left = self.delete_min(x.left)
        x.size = 1 + self.size(x.left) + self.size(x.right)
        return x

    def delete_max(self, x):
        if x.right == None: return x.left
        x.right = self.delete_max(x.right)
        x.size = 1 + self.size(x.left) + self.size(x.right)
        return x

    def floor(self, key):
        return self._floor(self.root, key)

    def _floor(self, x, key):
        if x == None: return None
        cmp = key - x.key
        if cmp == 0: return x
        if cmp < 0: return self._floor(x.left, key)
        t = self._floor(x.right, key)
        if t == None: return x
        return t

    def ceil(self, key):
        return self._ceil(self.root, key)

    def _ceil(self, x, key):
        if x == None: return None
        cmp = key - x.key
        if cmp == 0: return x
        if cmp > 0: return self._ceil(x.right, key)
        t = self._ceil(x.left, key)
        if t == None: return x
        return t

    def floor2(self, key):
        return self._floor2(self.root, key, None)

    def _floor2(self, x, key, best):
        if x == None: return best
        cmp = key - x.key
        if cmp < 0: return self._floor2(x.left, key, best)
        elif cmp > 0: return self._floor2(x.right, key, x.key)
        else: return x.key

if __name__ == '__main__':
    tree = BST()
    tree.put(2, 'B')
    tree.put(1, 'A')
    tree.put(3, 'C')
    a = tree.ceil(0)
    print(a.val)
    x = tree.get(2)
    print(x)
    tree.delete(1)
    c = tree.ceil(0)
    print(c.val)
    b = tree.floor(4)
    print(b.val)
