# -*- coding: utf-8 -*-
# ======================================
# @File    : 297.py
# @Time    : 2020/5/7 1:23
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *
class Codec:
    """
    [面试题37. 序列化二叉树](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/)
    """
    def serialize(self, root):
        res = []
        if root:
            stk = [root]
            while stk:
                x = stk.pop()
                res.append(' ')
                if x:
                    res.append(str(x.val))
                    stk.insert(0, x.left)
                    stk.insert(0, x.right)
                else:
                    res.append('None')
        return ''.join(res)

    def deserialize(self, data):
        if not data: return None
        tree_data = data.strip().split()
        if tree_data[0] == 'None': return None
        root = TreeNode(int(tree_data[0]))
        stk = [root]
        i = 1
        while stk:
            x = stk.pop()
            if not x:
                continue
            x.left = TreeNode(int(tree_data[i])) if tree_data[i] != "None" else None
            x.right = TreeNode(int(tree_data[i+1])) if tree_data[i+1] != "None" else None
            i += 2
            stk.insert(0, x.left)
            stk.insert(0, x.right)
        return root

