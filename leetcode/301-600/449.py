# -*- coding: utf-8 -*-
# ======================================
# @File    : 449.py
# @Time    : 2020/11/26 12:54 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
import bisect

class Codec:
    """
    [449. 序列化和反序列化二叉搜索树](https://leetcode-cn.com/problems/serialize-and-deserialize-bst/)
    """
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
        if not data or data == '[]|[]': return None
        pre, mid = [list(map(int, e[1:-1].split(','))) for e in data.split('|')]
        def _des(pre, mid):
            if not pre: return
            rv = pre[0]
            root = TreeNode(rv)
            j = bisect.bisect_left(mid, rv)
            root.left = _des(pre[1:j+1], mid[:j])
            root.right = _des(pre[j+1:], mid[j+1:])
            return root
        return _des(pre, mid)


if __name__ == '__main__':
    a = Codec()
    x = construct_tree_node([4,2,6,1,3,5,8,null,null,null,null,null,null,7])
    xs = a.serialize(x)
    print(xs)
    xx = a.deserialize(xs)
    tree_node_print(x)
    tree_node_print(xx)