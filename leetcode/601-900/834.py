# -*- coding: utf-8 -*-
# ======================================
# @File    : 834.py
# @Time    : 2020/10/6 17:05
# @Author  : Rivarrl
# ======================================
from algorithm_utils import *

class Solution:
    """
    [834. 树中距离之和](https://leetcode-cn.com/problems/sum-of-distances-in-tree/)
    """
    @timeit
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        """
        # 分割树为两部分，一部分是子树t，另一部分是剩余的树r, r(0, child) 表示把child分割后剩余的部分
        # 例如测试样例中的:
        #      0
        #   1    2
        #      3 4 5
        # 记以p为树根时子树的答案为ans(p)，ans(2)不考虑0和1
        # 记以p为树根时子树的节点数为nodes(p)，nodes(2) = 4
        # 记以p为起始点时的答案为res(p)，res(2)考虑0和1
        # 以0为起始点计算时有公式: res(0) = ans(0) = ans(r(0, 2)) + ans(2) + nodes(2)
        # 以2为起始点计算时有公式: res(2) = ans(2) + ans(r(0, 2)) + nodes(r(0, 2))
        # 上面两式相减可以得出: res(2) = res(0) + (nodes(r(0, 2) - nodes(2))
        #                          = res(0) + (N - 2 * nodes(2))
        # 所以只需要计算ans(0)和所有节点的nodes数，就可以自顶向下的递归求解所有res值了。
        # 考虑到有多个子树，计算ans(0)时公式换成 ans(p) = sum(ans(c) + nodes(c) for c in p.children)
        # 以上为输入是正常的父子关系的树时的情况，题目说他想给个无向图，那一定有坑，比如这种以0为根的写法: [[1,0],[0,2]]
        # 所以就随便找个0作为根节点，然后递归的时候参数带着父节点，子节点遍历它的子节点时排除掉这个父节点即可。
        """
        if N == 1: return [0]
        g = {}
        for u, v in edges:
            g[u] = g.get(u, []) + [v]
            g[v] = g.get(v, []) + [u]
        nodes = [0] * N
        res = [0] * N
        ans = [-1] * N
        def f_nodes(p, parent=0):
            if nodes[p] == 0:
                nodes[p] = 1
                for child in g[p]:
                    if child == parent: continue
                    nodes[p] += f_nodes(child, p)
            return nodes[p]
        def f_ans(p, parent=0):
            if ans[p] == -1:
                ans[p] = 0
                for child in g[p]:
                    if child == parent: continue
                    ans[p] += f_ans(child, p) + nodes[child]
            return ans[p]
        def f_res(p, parent=0):
            for child in g[p]:
                if child == parent: continue
                res[child] = res[p] + N - 2 * nodes[child]
                f_res(child, p)
        f_nodes(0)
        res[0] = f_ans(0)
        f_res(0)
        return res

if __name__ == '__main__':
    a = Solution()
    a.sumOfDistancesInTree(N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]])
    a.sumOfDistancesInTree(3, [[2,0], [1,0]])