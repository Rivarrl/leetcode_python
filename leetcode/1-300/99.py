# -*- coding: utf-8 -*-
# ======================================
# @File    : 99.py
# @Time    : 2020/8/8 0:15
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [99. 恢复二叉搜索树](https://leetcode-cn.com/problems/recover-binary-search-tree/)
    """
    def recoverTree(self, root: TreeNode) -> None:
        # 只有两个点被交换，所以用p、q找到这两个点然后交换val就行
        stk = []
        p, q, pre = None, None, TreeNode(-(1<<64))
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if root.val < pre.val:
                if not p:
                    p = pre
                q = root
            pre = root
            root = root.right
        p.val, q.val = q.val, p.val

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,3,null, null, 2])
    a.recoverTree(x)
    tree_node_print(x)
    x = construct_tree_node([3,1,4,null,null,2])
    a.recoverTree(x)
    tree_node_print(x)
