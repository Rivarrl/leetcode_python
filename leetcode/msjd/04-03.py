# -*- coding: utf-8 -*-
# ======================================
# @File    : 04-03.py
# @Time    : 2020/12/13 17:38
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [面试题 04.03. 特定深度节点链表](https://leetcode-cn.com/problems/list-of-depth-lcci/)
    """
    @timeit
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        from collections import deque
        if not tree: return []
        stk = deque([[tree, 0]])
        res = []
        cursor = []
        while stk:
            p, depth = stk.pop()
            q = ListNode(p.val)
            if depth >= len(res):
                res.append(q)
                cursor.append(q)
            else:
                cursor[-1].next = q
                cursor[-1] = cursor[-1].next
            if p.left:
                stk.appendleft([p.left, depth + 1])
            if p.right:
                stk.appendleft([p.right, depth + 1])
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,3,4,5,null,7,8])
    res = a.listOfDepth(x)
    for r in res:
        list_node_print(r)