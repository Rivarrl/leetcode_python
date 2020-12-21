# -*- coding: utf-8 -*-
# ======================================
# @File    : 652.py
# @Time    : 2020/12/21 12:23 下午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [652. 寻找重复的子树](https://leetcode-cn.com/problems/find-duplicate-subtrees/)
    """
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        from collections import defaultdict
        d = defaultdict(int)
        res = []
        def f(p):
            if not p: return 'x'
            left = f(p.left)
            right = f(p.right)
            cur = '{}+{}+{}'.format(left, right, p.val)
            d[cur] += 1
            tree_node_print(p)
            if d[cur] == 2:
                res.append(p)
            return cur
        f(root)
        return res

if __name__ == '__main__':
    a = Solution()
    x = construct_tree_node([1,2,3,4,null,2,4,null,null,null,null,4])
    res = a.findDuplicateSubtrees(x)
    for r in res:
        tree_node_print(r)
    x = construct_tree_node([0,0,0,0,null,null,0,null,null,null,null,null,null,null,0])
    res = a.findDuplicateSubtrees(x)
    for r in res:
        tree_node_print(r)