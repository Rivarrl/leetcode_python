# -*- coding: utf-8 -*-
# ======================================
# @File    : RedBlackBST.py
# @Time    : 2019/11/1 16:59
# @Author  : Rivarrl
# ======================================

RED = True
BLACK = False

class Node:
    """
    红黑树节点
    """
    def __init__(self, key = None, val = None, size = 0, color = None, left = None, right = None):
        self.key = key
        self.val = val
        self.size = size
        self.color = color
        self.left = left
        self.right = right

class RedBlackBST:
    """
    红黑树
    """
    def __init__(self, root = None):
        self.root = root

    # Node相关方法
    def is_empty(self):
        return self.root == None

    @staticmethod
    def is_red(x):
        if x == None: return False
        return x.color == RED

    @staticmethod
    def size(x):
        if x == None: return 0
        return x.size

    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        x.size = h.size
        h.size = 1 + self.size(h.left) + self.size(h.right)
        return x

    def rotate_right(self, h):
        x = h.left
        h.left = x.left
        x.right = h
        x.color = h.color
        h.color = RED
        x.size = h.size
        h.size = 1 + self.size(h.left) + self.size(h.right)
        return x

    @staticmethod
    def flip_colors(h):
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    def min(self):
        return self._min(self.root)

    def max(self):
        return self._max(self.root)

    def _min(self, h):
        if h.left == None: return h
        return self._min(h.left)

    def _max(self, h):
        if h.right == None: return h
        return self._max(h.right)

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, h, key):
        if h == None: return None
        cmp = key - h.key
        if cmp > 0: return self._get(h.right, key)
        elif cmp < 0: return self._get(h.left, key)
        else: return h.val

    def contains(self, key):
        return self.get(key) != None

    # 插入节点
    def put(self, key, val):
        if key == None:
            raise AttributeError("Key is None")
        if val == None:
            self.delete(key)
            return
        self.root = self._put(self.root, key, val)
        self.root.color = BLACK

    def _put(self, h, key, val):
        if h == None:
            return Node(key, val, 1, RED)
        cmp = self.compare(key, h.key)
        if cmp < 0: h.left = self._put(h.left, key, val)
        elif cmp > 0: h.right = self._put(h.right, key, val)
        else: h.val = val

        if self.is_red(h.right) and not self.is_red(h.left):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)
        h.size = 1 + self.size(h.left) + self.size(h.right)
        return h

    @staticmethod
    def compare(k1, k2):
        if type(k1) != type(k2): raise ValueError("Two keys got different type")
        if isinstance(k1, int) or isinstance(k1, float):
            return k1 - k2
        elif isinstance(k1, str):
            if k1 == k2: return 0
            k3 = max(k1, k2)
            return 1 if k3 == k1 else -1
        else:
            raise ValueError("Can't support this key type")

    def delete_min(self):
        if self.is_empty(): raise KeyError("BST underflow")
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = RED
        self.root = self._delete_min(self.root)
        if not self.is_empty(): self.root.color = BLACK

    def _delete_min(self, h):
        if h.left == None: return None
        if not self.is_red(h.left) and not self.is_red(h.right):
            h = self.move_red_left(h)
        h.left = self._delete_min(h.left)
        return self.balance(h)

    def delete_max(self):
        if self.is_empty(): raise KeyError("BST underflow")
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = RED
        self.root = self._delete_max(self.root)
        if not self.is_empty(): self.root.color = BLACK

    def _delete_max(self, h):
        if self.is_red(h.left): h = self.rotate_right(h)
        if h.right == None: return None
        if not self.is_red(h.right) and not self.is_red(h.right.left):
            h = self.move_red_right(h)
        h.right = self._delete_max(h.right)
        return self.balance(h)

    def delete(self, key):
        if not self.contains(key): return
        if not self.is_red(self.root.right) and not self.is_red(self.root.left):
            self.root.color = RED
        self.root = self._delete(self.root, key)
        if not self.is_empty(): self.root.color = BLACK

    def _delete(self, h, key):
        cmp = key - h.key
        if cmp < 0:
            if not self.is_red(h.left) and not self.is_red(h.left.left):
                h = self.move_red_left(h)
            h.left = self._delete(h.left, key)
        else:
            if self.is_red(h.left):
                h = self.rotate_right(h)
            if cmp == 0 and h.right == None: return None
            if not self.is_red(h.right) and not self.is_red(h.right.left):
                h = self.move_red_left(h)
            if cmp == 0:
                x = self._min(h.right)
                h.key, h.val = x.key, x.val
                h.right = self._delete_min(h.right)
            else:
                h.right = self._delete(h.right, key)
        return self.balance(h)

    def move_red_left(self, h):
        self.flip_colors(h)
        if self.is_red(h.right.left):
            h.right = self.rotate_right(h.right)
            h = self.rotate_left(h)
            self.flip_colors(h)
        return h

    def move_red_right(self, h):
        self.flip_colors(h)
        if self.is_red(h.left.left):
            h = self.rotate_right(h)
            self.flip_colors(h)
        return h

    def balance(self, h):
        if self.is_red(h.right): h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left): h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right): self.flip_colors(h)
        h.size = self.size(h.left) + self.size(h.right) + 1
        return h



if __name__ == '__main__':
    tree = RedBlackBST()
    tree.put(4, 'D')
    tree.put(2, 'B')
    tree.put(1, 'A')
    tree.put(11, 'K')
    tree.put(3, 'C')
    tree.put(6, 'F')
    tree.put(25, 'Y')
    tree.put(21, 'U')
    tree.put(7, 'G')
    tree.put(9, 'I')
    tree.put(10, 'J')
    tree.put(8, 'H')
    tree.put(13, 'M')
    tree.put(14, 'N')
    tree.put(15, 'O')
    tree.put(16, 'P')
    tree.put(5, 'E')
    tree.put(19, 'S')
    tree.put(12, 'L')
    tree.put(20, 'T')
    tree.put(17, 'Q')
    tree.put(22, 'V')
    tree.put(18, 'R')
    tree.put(23, 'W')
    tree.put(24, 'X')
    tree.put(26, 'Z')

    tree.delete(24)
    t = tree.get(24)
    print(t)