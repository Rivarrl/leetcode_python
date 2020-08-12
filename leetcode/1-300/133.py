# -*- coding: utf-8 -*-
# ======================================
# @File    : 133.py
# @Time    : 2020/8/12 10:00 上午
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    """
    [133. 克隆图](https://leetcode-cn.com/problems/clone-graph/)
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import deque
        if not node: return node
        q = deque([node])
        d = {}
        seen = {node}
        res = None
        while q:
            p = q.popleft()
            c = Node(p.val)
            if not res: res = c
            d[p.val] = [c, []]
            for e in p.neighbors:
                if not e in seen:
                    seen.add(e)
                    q.append(e)
                d[p.val][-1].append(e.val)
        for k, v in d.items():
            v[0].neighbors = [d[e][0] for e in v[1]]
        return res

if __name__ == '__main__':
    a = Solution()
    x1, x2, x3, x4 = Node(1), Node(2), Node(3), Node(4)
    x1.neighbors = [x2, x4]
    x2.neighbors = [x1, x3]
    x3.neighbors = [x2, x4]
    x4.neighbors = [x1, x3]
    c1 = a.cloneGraph(x1)
