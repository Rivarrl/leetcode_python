# -*- coding: utf-8 -*-
# ======================================
# @File    : 449.py
# @Time    : 2020/11/26 12:54 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
from collections import deque

class Codec:

    def pre_order(self, root):
        arr = []
        def f(p):
            if not p: return
            arr.append(p.val)
            f(p.left)
            f(p.right)
        f(root)
        return arr

    def mid_order(self, root):
        arr = []
        def f(p):
            if not p: return
            f(p.left)
            arr.append(p.val)
            f(p.right)
        f(root)
        return arr

    def serialize(self, root: TreeNode) -> str:
        if not root: return ''
        pre = self.pre_order(root)
        mid = self.mid_order(root)
        return str(pre) + '|' + str(mid)

    def deserialize(self, data: str) -> TreeNode:
        if data == '[]|[]': return None
        pre, mid = [list(map(int, e[1:-1].split(','))) for e in data.split('|')]
        n = len(pre)
        def _des(i1, j1, i2, j2):
            rv = pre[i1]
            root = TreeNode(rv)

        return _des(0, n-1, 0, n-1)




if __name__ == '__main__':
    a = Codec()
    x = construct_tree_node([4,2,6,1,3,5,8,null,null,null,null,null,null,7])
    xs = a.serialize(x)
    print(xs)
    xx = a.deserialize(xs)
    print(x == xx)