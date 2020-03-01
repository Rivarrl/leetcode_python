# -*- coding: utf-8 -*-
# ======================================
# @File    : 5346.py
# @Time    : 2020/3/1 13:41
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [5346. 二叉树中的列表](https://leetcode-cn.com/problems/linked-list-in-binary-tree/)
    """
    @timeit
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs1(p, q):
            if not p: return True
            if not q: return False
            if p.val != q.val: return False
            return dfs1(p.next, q.left) or dfs1(p.next, q.right)
        def dfs(p, q):
            if not p: return True
            if not q: return False
            if dfs1(p, q): return True
            return dfs(p, q.left) or dfs(p, q.right)
        return dfs(head, root)


if __name__ == '__main__':
    a = Solution()
    head = construct_list_node([4,2,8])
    root = construct_tree_node([1,4,4,null,2,2,null,null,null,1,null,6,8,null,null,null,null,null,null,null,null,null,null,null,null,1,3,null,null,null,null])
    a.isSubPath(head, root)
    head = construct_list_node([1,4,2,6])
    a.isSubPath(head, root)
    head = construct_list_node([1,4,2,6,8])
    a.isSubPath(head, root)